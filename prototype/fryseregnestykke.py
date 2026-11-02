# Copyright (c) 2026 Markemus-byte and Debt.alarm contributors
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Worked estimate of what a fee freeze costs (docs/fortjeneste-og-frist.md).

Two parts:
1. One silent consumer debtor: what is added to the debt over 12 months,
   with no flag and with a silence flag set after 30, 45, 60 or 90 days.
2. The whole industry: an upper bound on what a 6-month freeze could cost
   creditors and collectors, for different shares of silent debtors.

Fee figures are Finanstilsynet's 2026 table (inkassosats 750 kr, creditor
with VAT deduction). Days and shares marked ASSUMPTION are ours.
Uses only the Python standard library. Run: python3 fryseregnestykke.py
"""

from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal
from typing import Optional

from stilleflagg import MAX_FREEZE_DAYS, SILENCE_DAYS

INKASSOVARSEL = 38  # kr, 2026
# Light salær ("lett sats") by principal, consumer, creditor with VAT deduction, 2026.
# Heavy salær ("tung sats") is double.
SALAER_LETT = [(500, 187.5), (1_000, 262.5), (2_500, 300), (10_000, 600),
               (50_000, 1_200), (250_000, 2_700), (float("inf"), 5_400)]
RETTSGEBYR = 1_345  # kr, 2026; goes to the state, not the collector
RENTE = 0.1225  # forsinkelsesrente from 1 July 2026

# Timeline in days after the collection notice (inkassovarsel = day 0).
DAY_DUE = -14  # ASSUMPTION: invoice fell due 14 days before the notice
DAY_PAYMENT_DEMAND = 14  # betalingsoppfordring with light salær
DAY_DEADLINE = 28  # at least 14 days to pay
DAY_HEAVY = DAY_DEADLINE + 29  # heavy salær allowed when the deadline is overrun by more than 28 days
DAY_LEGAL = 180  # ASSUMPTION: first legal step (one rettsgebyr; legal salær left out)
FREEZE_DAYS = MAX_FREEZE_DAYS  # the proposal's maximum freeze, shared with stilleflagg.py
WELFARE_CHECK_DAY = SILENCE_DAYS + 90  # day 150: welfare check for a flag set on day 60
HORIZON = 365


def light_salaer(principal: float) -> float:
    for limit, fee in SALAER_LETT:
        if principal <= limit:
            return fee
    raise ValueError(principal)


@dataclass
class Added:
    salaer: float  # to the collector
    varsel: float  # to the collector
    rettsgebyr: float  # to the state
    rente: float  # to the creditor (the collector when it owns the claim)

    @property
    def total(self) -> float:
        return self.salaer + self.varsel + self.rettsgebyr + self.rente


def silent_debtor(principal: float, flag_day: Optional[int] = None,
                  heavy_needs_flag: bool = True, horizon: int = HORIZON) -> Added:
    """What has been added by day `horizon` when the debtor never answers.

    A flag freezes new fees, interest and legal steps for FREEZE_DAYS; a fee
    that falls inside the freeze is moved to the day the freeze ends.
    heavy_needs_flag follows the proposal: a collector must set the flag
    before it can move a silent debtor to heavy salær or legal steps.
    """
    start, end = (flag_day, flag_day + FREEZE_DAYS) if flag_day is not None else (None, None)

    def charged(day: int) -> bool:
        if start is not None and start <= day < end:
            day = end
        return day < horizon

    heavy_day = DAY_HEAVY
    if start is not None and heavy_needs_flag and start > DAY_HEAVY:
        heavy_day = start  # held back until the flag is set, which then freezes it
    light = light_salaer(principal)
    salaer = light * (charged(DAY_PAYMENT_DEMAND) + charged(heavy_day))
    rettsgebyr = RETTSGEBYR if charged(DAY_LEGAL) else 0

    interest_days = horizon - DAY_DUE
    if start is not None:
        interest_days -= max(0, min(end, horizon) - min(start, horizon))
    rente = principal * RENTE * interest_days / 365
    return Added(salaer, INKASSOVARSEL, rettsgebyr, rente)


# Finanstilsynet, inkassostatistikk for 2024 (latest year with the split), billion kr.
COLLECTED_INTEREST_2024 = 3.281
COLLECTED_OUT_OF_COURT_2024 = 2.929
COLLECTED_LEGAL_2024 = 0.720
FIRM_INCOME_2024 = 5.09
FIRM_COSTS_2024 = 4.89


def industry_upper_bound(silent_share: float) -> dict:
    """Upper bound, billion kr per year, if silent_share of all money paid by
    debtors came from people who would be flagged (ASSUMPTION; real share unknown).

    Interest during the freeze is lost. Fees are not lost, only delayed by
    up to six months; the delay is valued at the late-payment rate.
    """
    lost_interest = silent_share * COLLECTED_INTEREST_2024 * FREEZE_DAYS / 365
    fees = silent_share * (COLLECTED_OUT_OF_COURT_2024 + COLLECTED_LEGAL_2024)
    delay_cost = fees * RENTE * FREEZE_DAYS / 365
    return {
        "lost_interest": lost_interest,
        "delay_cost_fees": delay_cost,
        "total": lost_interest + delay_cost,
        "share_of_firm_income": delay_cost / FIRM_INCOME_2024,
    }


def _kr(x: float) -> str:
    whole = Decimal(str(x)).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    return f"{whole:,}".replace(",", " ")


def _row(label, a: Added) -> str:
    return (f"| {label} | {_kr(a.salaer)} | {_kr(a.varsel)} | {_kr(a.rettsgebyr)}"
            f" | {_kr(a.rente)} | {_kr(a.total)} |")


if __name__ == "__main__":
    for horizon in (WELFARE_CHECK_DAY, HORIZON):
        for principal in (1_000, 5_000, 20_000):
            print(f"\nKrav {_kr(principal)} kr, stille skyldner, påløpt ved dag {horizon}")
            print("| flagg | salær | varsel | rettsgebyr | rente | sum |")
            print("|---|---|---|---|---|---|")
            for f in (None, 30, 45, SILENCE_DAYS, 90):
                print(_row(f"dag {f}" if f else "ingen", silent_debtor(principal, f, horizon=horizon)))
            for f in (60, 90):
                print(_row(f"dag {f}, uten regelen", silent_debtor(principal, f, False, horizon)))

    print("\nBransjen, øvre grense per år (mrd kr)")
    print("| andel stille | tapt rente | kostnad av utsatte gebyrer | sum | utsettelse som andel av foretakenes inntekt |")
    print("|---|---|---|---|---|")
    for s in (0.05, 0.10, 0.20):
        r = industry_upper_bound(s)
        print(f"| {s:.0%} | {r['lost_interest']:.3f} | {r['delay_cost_fees']:.3f}"
              f" | {r['total']:.3f} | {r['share_of_firm_income']:.2%} |")
