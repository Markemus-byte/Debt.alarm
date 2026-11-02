# Copyright (c) 2026 Markemus-byte and Debt.alarm contributors
# SPDX-License-Identifier: AGPL-3.0-or-later
import unittest

from fryseregnestykke import (DAY_HEAVY, FREEZE_DAYS, RETTSGEBYR,
                              WELFARE_CHECK_DAY, _kr, industry_upper_bound,
                              light_salaer, silent_debtor)
from stilleflagg import MAX_FREEZE_DAYS


class FreezeEstimateTest(unittest.TestCase):
    def test_salaer_bands(self):
        self.assertEqual(light_salaer(500), 187.5)
        self.assertEqual(light_salaer(5_000), 600)
        self.assertEqual(light_salaer(300_000), 5_400)

    def test_no_flag_charges_heavy_salaer_and_legal_step(self):
        a = silent_debtor(5_000)
        self.assertEqual(a.salaer, 1_200)
        self.assertEqual(a.rettsgebyr, RETTSGEBYR)

    def test_flag_before_heavy_day_holds_back_doubling(self):
        a = silent_debtor(5_000, flag_day=DAY_HEAVY - 1, horizon=150)
        self.assertEqual(a.salaer, 600)

    def test_late_flag_without_rule_lets_doubling_through(self):
        a = silent_debtor(5_000, flag_day=90, heavy_needs_flag=False, horizon=150)
        self.assertEqual(a.salaer, 1_200)

    def test_freeze_stops_interest(self):
        flagged = silent_debtor(5_000, flag_day=60)
        unflagged = silent_debtor(5_000)
        self.assertLess(flagged.rente, unflagged.rente)

    def test_fees_are_delayed_not_deleted_within_a_year(self):
        self.assertEqual(silent_debtor(5_000, 60).salaer, silent_debtor(5_000).salaer)

    def test_industry_bound_grows_with_share(self):
        self.assertLess(industry_upper_bound(0.05)["total"], industry_upper_bound(0.2)["total"])


    def test_heavy_salaer_day(self):
        # Payment demand on day 14, at least 14 days to pay, then more than 28 days overrun.
        self.assertEqual(DAY_HEAVY, 57)

    def test_freeze_matches_the_rules_prototype(self):
        self.assertEqual(FREEZE_DAYS, MAX_FREEZE_DAYS)
        self.assertEqual(WELFARE_CHECK_DAY, 150)

    def test_rounding_is_half_up(self):
        self.assertEqual(_kr(262.5), "263")
        self.assertEqual(_kr(14_423.4), "14 423")


class DocumentFiguresTest(unittest.TestCase):
    """The figures quoted in docs/fortjeneste-og-frist.md. If a rule or rate
    changes, these fail, and the document must be updated with the new output."""

    def total(self, principal, flag_day=None, heavy_needs_flag=True, horizon=WELFARE_CHECK_DAY):
        return round(silent_debtor(principal, flag_day, heavy_needs_flag, horizon).total)

    def test_one_debtor_at_welfare_check(self):
        self.assertEqual(self.total(5_000), 1_513)
        self.assertEqual([self.total(5_000, d) for d in (30, 45, 60, 90)], [712, 737, 762, 813])
        self.assertEqual(self.total(5_000, 60, heavy_needs_flag=False), 1_362)
        self.assertEqual((self.total(20_000), self.total(20_000, 60)), (3_539, 1_735))
        self.assertEqual((self.total(1_000), self.total(1_000, 60)), (618, 325))

    def test_one_debtor_after_a_year(self):
        self.assertEqual(self.total(5_000, horizon=365), 3_219)
        self.assertEqual(self.total(5_000, 60, horizon=365), 2_914)

    def test_day_30_versus_day_90(self):
        self.assertEqual(self.total(5_000, 90) - self.total(5_000, 30), 101)
        self.assertEqual(self.total(20_000, 90) - self.total(20_000, 30), 403)

    def test_industry_table(self):
        rows = [industry_upper_bound(s) for s in (0.05, 0.10, 0.20)]
        self.assertEqual([round(r["lost_interest"], 2) for r in rows], [0.08, 0.16, 0.33])
        self.assertEqual([round(r["delay_cost_fees"], 2) for r in rows], [0.01, 0.02, 0.04])
        self.assertEqual([round(r["total"], 2) for r in rows], [0.09, 0.19, 0.37])
        self.assertEqual([round(r["share_of_firm_income"] * 100, 1) for r in rows], [0.2, 0.4, 0.9])


if __name__ == "__main__":
    unittest.main()
