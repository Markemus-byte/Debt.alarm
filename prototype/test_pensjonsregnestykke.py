# Copyright (c) 2026 Markemus-byte and Debt.alarm contributors
# SPDX-License-Identifier: AGPL-3.0-or-later
import unittest

from pensjonsregnestykke import (DELINGSTALL_1963_67, LX,
                                 OLD_AGE_SPENDING_2025, annuity_factor,
                                 balance_at_67, basis, cohort_payout_ratio,
                                 cut_for_full_refund, death_before_pension,
                                 divisor_with_arvegevinst, guarantee_cost,
                                 life_expectancy, lump_sum_cost_per_1000_deaths,
                                 lx_at, outcomes, pre_pension_refund_cost,
                                 refund_cost)


class LifeTableTest(unittest.TestCase):
    """The typed-in SSB table must reproduce SSB's own published figures."""

    def test_table_is_complete_and_decreasing(self):
        for sex, col in LX.items():
            self.assertEqual(col[0], 100_000, sex)
            self.assertEqual(len(col), 107, sex)
            self.assertTrue(all(a >= b for a, b in zip(col, col[1:])), sex)

    def test_life_expectancy_matches_ssb(self):
        # SSB 2025: 19.17 (both), 18.09 (men), 20.17 (women) at 67; 23.45 at 62.
        self.assertAlmostEqual(life_expectancy("begge", 67), 19.17, delta=0.05)
        self.assertAlmostEqual(life_expectancy("begge", 67), 19.15, delta=0.005)
        self.assertAlmostEqual(life_expectancy("menn", 67), 18.09, delta=0.05)
        self.assertAlmostEqual(life_expectancy("kvinner", 67), 20.17, delta=0.05)
        self.assertAlmostEqual(life_expectancy("begge", 62), 23.45, delta=0.05)


def bn(share):
    return round(OLD_AGE_SPENDING_2025 * share / 1e9)


class PensionAtDeathTest(unittest.TestCase):
    """Pins the computed figures quoted in docs/pensjon-og-arv.md."""

    def test_example_balance_and_pension(self):
        self.assertEqual(round(balance_at_67()), 4_887_000)
        self.assertEqual(round(balance_at_67() / DELINGSTALL_1963_67, -3), 303_000)
        self.assertEqual(round(lump_sum_cost_per_1000_deaths() / 1e6), 137)

    def test_deaths_before_67(self):
        self.assertAlmostEqual(death_before_pension(), 0.084, delta=0.0005)
        self.assertAlmostEqual(death_before_pension("menn"), 0.102, delta=0.0005)
        self.assertAlmostEqual(death_before_pension("kvinner"), 0.066, delta=0.0005)

    def test_divisor_check(self):
        # The SSB table alone gives 17.67; sharing out the balances of those who
        # die before 62 lowers it to about 17.1. The official 16.11 is about 6 %
        # lower still, which this model does not explain.
        self.assertAlmostEqual(annuity_factor(basis("ssb")), 17.67, delta=0.01)
        self.assertAlmostEqual(divisor_with_arvegevinst(), 17.06, delta=0.01)
        self.assertAlmostEqual(lx_at("begge", 62) / lx_at("begge", 22), 0.947, delta=0.0005)
        self.assertAlmostEqual(divisor_with_arvegevinst() / DELINGSTALL_1963_67, 1.06, delta=0.005)

    def test_survivors_get_more_than_their_own_balance(self):
        self.assertAlmostEqual(outcomes(basis("ssb"))["payments"], 1.097, delta=0.001)
        self.assertAlmostEqual(outcomes(basis("lengre_liv"))["payments"], 1.179, delta=0.001)

    def test_whole_cohort_gets_back_at_least_what_it_earned(self):
        self.assertAlmostEqual(cohort_payout_ratio("ssb"), 1.026, delta=0.001)
        self.assertAlmostEqual(cohort_payout_ratio("lengre_liv"), 1.117, delta=0.001)

    def test_unpaid_share_range(self):
        self.assertAlmostEqual(outcomes(basis("ssb"))["unpaid"], 0.136, delta=0.001)
        self.assertAlmostEqual(outcomes(basis("lengre_liv"))["unpaid"], 0.111, delta=0.001)

    def test_unpaid_in_kroner(self):
        b = balance_at_67()
        self.assertEqual(round(outcomes(basis("ssb"))["unpaid"] * b, -4), 660_000)
        self.assertEqual(round(outcomes(basis("lengre_liv"))["unpaid"] * b, -4), 540_000)

    def test_breakeven_and_who_loses(self):
        for name, share in (("ssb", 0.377), ("lengre_liv", 0.315)):
            o = outcomes(basis(name))
            self.assertAlmostEqual(o["breakeven_age"], 84.17, delta=0.005)
            self.assertAlmostEqual(o["die_before_breakeven"], share, delta=0.001)
            self.assertTrue(0.35 <= o["unpaid_if_die_before"] <= 0.365)
            self.assertTrue(1_700_000 <= o["unpaid_if_die_before"] * balance_at_67() <= 1_800_000)

    def test_guarantees(self):
        self.assertAlmostEqual(guarantee_cost(basis("ssb"), 5), 0.007, delta=0.0005)
        self.assertAlmostEqual(guarantee_cost(basis("lengre_liv"), 5), 0.005, delta=0.0005)
        self.assertAlmostEqual(guarantee_cost(basis("ssb"), 10), 0.033, delta=0.0005)
        self.assertAlmostEqual(guarantee_cost(basis("lengre_liv"), 10), 0.025, delta=0.0005)
        self.assertEqual(bn(guarantee_cost(basis("ssb"), 5)), 2)
        self.assertEqual(bn(guarantee_cost(basis("lengre_liv"), 5)), 2)
        self.assertEqual((bn(guarantee_cost(basis("lengre_liv"), 10)), bn(guarantee_cost(basis("ssb"), 10))), (8, 11))

    def test_longer_guarantee_costs_more(self):
        s = basis("ssb")
        self.assertLess(guarantee_cost(s, 5), guarantee_cost(s, 10))
        self.assertLess(guarantee_cost(s, 10), refund_cost(s))

    def test_refund_before_and_after_67(self):
        self.assertAlmostEqual(pre_pension_refund_cost("ssb"), 0.063, delta=0.0005)
        self.assertAlmostEqual(pre_pension_refund_cost("lengre_liv"), 0.047, delta=0.0005)
        self.assertEqual((bn(pre_pension_refund_cost("lengre_liv")), bn(pre_pension_refund_cost("ssb"))), (16, 21))
        self.assertAlmostEqual(refund_cost(basis("ssb")), 0.124, delta=0.0005)
        self.assertAlmostEqual(refund_cost(basis("lengre_liv")), 0.094, delta=0.0005)
        self.assertEqual((bn(refund_cost(basis("lengre_liv"))), bn(refund_cost(basis("ssb")))), (32, 41))

    def test_full_refund_paid_by_cutting_pensions(self):
        # Cost-neutral: payments plus refunds after the cut equal today's payments.
        for name, cut in (("ssb", 0.176), ("lengre_liv", 0.120)):
            s = basis(name)
            c = cut_for_full_refund(s)
            self.assertAlmostEqual(c, cut, delta=0.001)
            after = outcomes(s, DELINGSTALL_1963_67 / (1 - c))
            self.assertAlmostEqual(after["payments"] + after["unpaid"], outcomes(s)["payments"], places=6)
            self.assertGreater(c, refund_cost(s))

if __name__ == "__main__":
    unittest.main()
