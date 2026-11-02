# Copyright (c) 2026 Markemus-byte and Debt.alarm contributors
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Worked estimate of what happens to folketrygd old-age pension at death
(docs/pensjon-og-arv.md).

For one example earner it computes:
1. the pension balance (pensjonsbeholdning) at 67 and the yearly pension,
2. how much of the balance is never paid out because the person dies first,
3. what different guarantees for the family would cost, as a share of
   expected pension payments.

Mortality is Statistics Norway's period life table for 2025 (SSB, Tabell 6
on https://www.ssb.no/befolkning/fodte-og-dode/statistikk/dode, kildetabell
07902). Two bases are used:
- "ssb": the 2025 table as published.
- "lengre_liv": the same table with every death rate 20 % lower, because
  people retiring in the 2030s will likely live longer than today's table
  shows (ASSUMPTION, a sensitivity, not a forecast).

The yearly pension is the balance divided by the official divisor 16.11.
The divisor is lower than an annuity factor on the SSB table. Part of the gap
is that the divisor shares out the balances of those who die before 62 to the
survivors of the cohort (arvegevinst, Innst. O. nr. 67 (2008-2009) ch. 5);
the rest is not explained here (Nav uses ten years of observed mortality,
fixed when the cohort turns 61, not the 2025 table).

Pension in payment is indexed with the average of wage and price growth,
modelled as wage growth minus 0.75 % a year (true if real wage growth is
1.5 %). All amounts, including "paid out", are in today's wage level, so a
krone paid at 80 counts for less than one paid at 67 (ASSUMPTION, see
INDEXATION_GAP).
Figures are estimates, not Nav's own calculations.
Uses only the Python standard library. Run: python3 pensjonsregnestykke.py
"""

from typing import Callable, Dict, List

ACCRUAL_RATE = 0.181  # 18.1 % of income, for people born 1963 or later (SNL)
CEILING_G = 7.1  # income above 7.1 G earns nothing
G_2026 = 136_549  # grunnbeløp from 1 May 2026 (Stortinget, Meld. St. 10 (2025-2026))
DELINGSTALL_1963_67 = 16.11  # divisor at 67 for the 1963 cohort (Smarte Penger)
INDEXATION_GAP = 0.0075  # ASSUMPTION: average of wage and price growth = wage growth minus 0.75 %
SALARY = 600_000  # ASSUMPTION: example salary, today's kroner
WORK_YEARS = 45  # ASSUMPTION: from age 22 to 66
START_AGE = 22
PENSION_AGE = 67
ARVEGEVINST_AGE = 62  # deaths before 62 are shared out through the divisor
LONGER_LIFE_SCALE = 0.8  # ASSUMPTION: death rates 20 % below the 2025 table
OLD_AGE_SPENDING_2025 = 334e9  # folketrygd old-age pension, NOK (Pensjonspolitisk arbeidsgruppe 2026)
G_LUMP_SUM = G_2026  # proposal: one G to the family
STEP = 1 / 12  # monthly steps

# lx, survivors per 100 000 at exact age x, SSB 2025 (both sexes, men, women).
_LX_ROWS = """
0 100000 100000 100000|1 99754 99729 99781|2 99739 99706 99774|3 99730 99692 99770
4 99723 99685 99763|5 99718 99678 99759|6 99714 99675 99756|7 99707 99665 99752
8 99701 99662 99742|9 99694 99649 99742|10 99688 99643 99735|11 99682 99634 99732
12 99677 99628 99729|13 99674 99625 99726|14 99665 99616 99716|15 99653 99602 99707
16 99640 99582 99701|17 99624 99557 99695|18 99601 99526 99680|19 99551 99456 99653
20 99530 99432 99634|21 99506 99397 99622|22 99471 99347 99603|23 99439 99293 99594
24 99420 99270 99579|25 99387 99224 99561|26 99341 99153 99541|27 99293 99086 99512
28 99254 99028 99493|29 99212 98973 99466|30 99177 98927 99442|31 99124 98854 99410
32 99070 98774 99384|33 99015 98701 99348|34 98963 98637 99308|35 98918 98582 99273
36 98868 98511 99246|37 98805 98443 99188|38 98736 98348 99146|39 98679 98266 99115
40 98617 98210 99048|41 98530 98091 98994|42 98471 98016 98952|43 98390 97894 98914
44 98286 97772 98828|45 98193 97652 98764|46 98098 97553 98674|47 97984 97416 98583
48 97866 97292 98473|49 97725 97120 98364|50 97587 96940 98270|51 97448 96763 98169
52 97287 96571 98043|53 97083 96352 97854|54 96874 96093 97698|55 96642 95824 97504
56 96412 95567 97303|57 96128 95203 97102|58 95848 94870 96880|59 95511 94469 96610
60 95130 93998 96326|61 94672 93497 95913|62 94221 92954 95558|63 93720 92309 95210
64 93104 91591 94701|65 92527 90939 94203|66 91859 90127 93689|67 91092 89257 93028
68 90247 88266 92333|69 89368 87260 91582|70 88317 86068 90677|71 87259 84817 89813
72 86013 83425 88713|73 84620 81759 87597|74 83125 80060 86316|75 81445 78198 84825
76 79605 76060 83292|77 77734 73967 81654|78 75618 71697 79692|79 73241 69006 77633
80 70479 65874 75237|81 67695 62873 72671|82 64512 59529 69645|83 61112 55825 66528
84 57389 51842 63028|85 53748 47905 59654|86 49727 43666 55809|87 45518 39542 51479
88 41061 34865 47174|89 36617 30315 42766|90 32033 26012 37856|91 27461 21873 32812
92 22891 17764 27729|93 18881 14128 23306|94 15267 11080 19105|95 11720 8253 14857
96 8782 5951 11310|97 6289 4122 8205|98 4358 2731 5771|99 3030 1930 3990
100 2025 1238 2702|101 1316 787 1766|102 801 508 1058|103 450 228 612
104 254 146 337|105 168 107 217|106 91 71 109
"""


def _parse() -> Dict[str, List[float]]:
    cols: Dict[str, List[float]] = {"begge": [], "menn": [], "kvinner": []}
    for cell in _LX_ROWS.replace("\n", "|").split("|"):
        if not cell.strip():
            continue
        age, both, men, women = (int(v) for v in cell.split())
        assert age == len(cols["begge"]), age
        for key, value in zip(cols, (both, men, women)):
            cols[key].append(float(value))
    return cols


LX = _parse()
MAX_AGE = len(LX["begge"]) - 1  # 106; everyone is assumed dead one year later


def lx_at(sex: str, age: float) -> float:
    """Survivors at a fractional age, log-linear between whole ages."""
    if age >= MAX_AGE + 1:
        return 0.0
    lo = int(age)
    frac = age - lo
    a = LX[sex][lo]
    b = LX[sex][lo + 1] if lo + 1 <= MAX_AGE else 0.0
    if b <= 0:
        return a * (1 - frac)
    return a * (b / a) ** frac


def survival(sex: str, scale: float = 1.0, start: float = PENSION_AGE) -> Callable[[float], float]:
    """P(alive at start + t | alive at start); death rates multiplied by scale."""
    base = lx_at(sex, start)
    return lambda t: (lx_at(sex, start + t) / base) ** scale


def life_expectancy(sex: str, age: int) -> float:
    s = survival(sex, start=age)
    n = int((MAX_AGE + 1 - age) / STEP)
    return sum((s(k * STEP) + s((k + 1) * STEP)) / 2 * STEP for k in range(n))


def balance_at_67(salary: float = SALARY, years: int = WORK_YEARS) -> float:
    return ACCRUAL_RATE * min(salary, CEILING_G * G_2026) * years


def _grid(surv: Callable[[float], float]):
    n = int((MAX_AGE + 1 - PENSION_AGE) / STEP)
    alive = [surv(k * STEP) for k in range(n + 1)]
    pay = [(1 - INDEXATION_GAP) ** (k * STEP) * STEP for k in range(n)]  # paid at start of month
    return n, alive, pay


def annuity_factor(surv: Callable[[float], float]) -> float:
    n, alive, pay = _grid(surv)
    return sum(alive[k] * pay[k] for k in range(n))


def basis(name: str, sex: str = "begge") -> Callable[[float], float]:
    if name == "ssb":
        return survival(sex)
    if name == "lengre_liv":
        return survival(sex, LONGER_LIFE_SCALE)
    raise ValueError(name)


def divisor_with_arvegevinst(sex: str = "begge") -> float:
    """Annuity factor at 67 on the SSB table, lowered so that the balance
    earned from 22 to 61 by people who die before 62 is shared out to those
    alive at 62. Each year's accrual is weighted by who was alive to earn it.
    A rough check on the official divisor, not Nav's formula."""
    years_before = ARVEGEVINST_AGE - START_AGE
    years_total = PENSION_AGE - START_AGE
    earned = sum(lx_at(sex, a + 0.5) for a in range(START_AGE, ARVEGEVINST_AGE))
    held = lx_at(sex, ARVEGEVINST_AGE) * years_before
    boost = years_before / years_total * earned / held + (years_total - years_before) / years_total
    return annuity_factor(survival(sex)) / boost


def outcomes(surv: Callable[[float], float], divisor: float = DELINGSTALL_1963_67) -> Dict[str, float]:
    """Per unit of balance, for someone alive at 67 who draws balance/divisor a year."""
    n, alive, pay = _grid(surv)
    yearly = 1 / divisor
    paid = 0.0
    unpaid = 0.0
    payments = 0.0
    breakeven = None
    for k in range(n):
        paid += yearly * pay[k]
        payments += alive[k] * yearly * pay[k]
        died = alive[k] - alive[k + 1]  # died during month k, after its payment
        unpaid += died * max(0.0, 1 - paid)
        if breakeven is None and paid >= 1:
            breakeven = k * STEP  # month k's payment is made at the start of month k
    assert breakeven is not None
    share_before = 1 - surv(breakeven)
    return {
        "payments": payments,  # expected payments, as a share of the balance
        "unpaid": unpaid,  # expected balance never paid out
        "breakeven_age": PENSION_AGE + breakeven,
        "die_before_breakeven": share_before,
        "unpaid_if_die_before": unpaid / share_before,
    }


def guarantee_cost(surv: Callable[[float], float], years: float,
                   divisor: float = DELINGSTALL_1963_67) -> float:
    """Extra cost of paying the rest of a guaranteed period to the family,
    as a share of expected pension payments."""
    n, alive, pay = _grid(surv)
    m = int(round(years / STEP))
    yearly = 1 / divisor
    tail = [0.0] * (m + 1)  # tail[k] = payments due from month k to month m
    for k in range(m - 1, -1, -1):
        tail[k] = tail[k + 1] + yearly * pay[k]
    extra = sum((alive[k] - alive[k + 1]) * tail[k + 1] for k in range(min(m, n)))
    return extra / outcomes(surv, divisor)["payments"]


def refund_cost(surv: Callable[[float], float], divisor: float = DELINGSTALL_1963_67) -> float:
    """Extra cost of paying the unused balance to the heirs at death after 67,
    as a share of expected pension payments."""
    o = outcomes(surv, divisor)
    return o["unpaid"] / o["payments"]


def death_before_pension(sex: str = "begge", start: int = START_AGE) -> float:
    """Share of those alive at the start of working life who die before 67."""
    return 1 - lx_at(sex, PENSION_AGE) / lx_at(sex, start)


def _scale(name: str) -> float:
    return {"ssb": 1.0, "lengre_liv": LONGER_LIFE_SCALE}[name]


def _working_life(name: str, sex: str = "begge"):
    """Balance left at death before 67 per person alive at 22 (in units of a
    full balance at 67; it grows evenly over the working years, ASSUMPTION),
    and the share alive at 67."""
    s = survival(sex, _scale(name), start=START_AGE)
    years = PENSION_AGE - START_AGE
    left = sum((s(t) - s(t + 1)) * (t + 0.5) / years for t in range(years))
    return left, s(years)


def pre_pension_refund_cost(name: str, sex: str = "begge") -> float:
    """Extra cost of giving the family the balance of someone who dies between
    22 and 67, as a share of the cohort's expected pension payments."""
    left, at_67 = _working_life(name, sex)
    return left / (at_67 * outcomes(basis(name, sex))["payments"])


def cohort_payout_ratio(name: str, sex: str = "begge") -> float:
    """Expected pension paid to a cohort followed from 22, divided by all the
    balance its members earned, including those who die before 67."""
    left, at_67 = _working_life(name, sex)
    return at_67 * outcomes(basis(name, sex))["payments"] / (at_67 + left)


def cut_for_full_refund(surv: Callable[[float], float],
                        divisor: float = DELINGSTALL_1963_67) -> float:
    """How much lower every pension must be for the unused balance to be paid
    to the heirs at no extra cost. A lower pension leaves more unused balance,
    so the cut is larger than refund_cost."""
    budget = outcomes(surv, divisor)["payments"]
    lo, hi = 0.0, 1.0  # share of today's pension that is kept
    for _ in range(60):
        keep = (lo + hi) / 2
        o = outcomes(surv, divisor / keep)
        if o["payments"] + o["unpaid"] > budget:
            hi = keep
        else:
            lo = keep
    return 1 - (lo + hi) / 2


def lump_sum_cost_per_1000_deaths(amount: float = G_LUMP_SUM) -> float:
    return amount * 1000


def _kr(x: float) -> str:
    return f"{x:,.0f}".replace(",", " ")


def _pct(x: float) -> str:
    return f"{100 * x:.1f} %"


def main() -> None:
    b = balance_at_67()
    print(f"Balance at 67: {_kr(b)} kr, yearly pension {_kr(b / DELINGSTALL_1963_67)} kr")
    print(f"Life expectancy at 67 from the table: {life_expectancy('begge', 67):.2f} years "
          f"(SSB publishes 19.17)")
    print(f"Die between {START_AGE} and 67: {_pct(death_before_pension())} "
          f"(men {_pct(death_before_pension('menn'))}, women {_pct(death_before_pension('kvinner'))})")
    print(f"Annuity factor at 67 on the SSB 2025 table: {annuity_factor(basis('ssb')):.2f}, "
          f"with deaths before 62 shared out: {divisor_with_arvegevinst():.2f} "
          f"(official divisor {DELINGSTALL_1963_67})")
    print(f"Survival from {START_AGE} to {ARVEGEVINST_AGE}: "
          f"{_pct(lx_at('begge', ARVEGEVINST_AGE) / lx_at('begge', START_AGE))}")
    for name in ("ssb", "lengre_liv"):
        s = basis(name)
        o = outcomes(s)
        print(f"\nBasis: {name}")
        print(f"  expected payments: {_pct(o['payments'])} of the balance")
        print(f"  whole cohort from {START_AGE}: paid {_pct(cohort_payout_ratio(name))} of all balance earned")
        print(f"  never paid out: {_pct(o['unpaid'])} of the balance ({_kr(o['unpaid'] * b)} kr)")
        print(f"  payments reach the balance at age {o['breakeven_age']:.1f}; "
              f"{_pct(o['die_before_breakeven'])} die before that, "
              f"losing {_pct(o['unpaid_if_die_before'])} on average ({_kr(o['unpaid_if_die_before'] * b)} kr)")
        for years in (5, 10):
            c = guarantee_cost(s, years)
            print(f"  {years}-year guarantee: {_pct(c)} ({OLD_AGE_SPENDING_2025 * c / 1e9:.0f} bn kr)")
        c = pre_pension_refund_cost(name)
        print(f"  balance to family on death 22-66: {_pct(c)} ({OLD_AGE_SPENDING_2025 * c / 1e9:.0f} bn kr)")
        c = refund_cost(s)
        print(f"  unused balance to heirs after 67: {_pct(c)} ({OLD_AGE_SPENDING_2025 * c / 1e9:.0f} bn kr), "
              f"or every pension {_pct(cut_for_full_refund(s))} lower")
    print(f"\nOne G to the family: {_kr(lump_sum_cost_per_1000_deaths() / 1e6)} million kr per 1 000 deaths")


if __name__ == "__main__":
    main()
