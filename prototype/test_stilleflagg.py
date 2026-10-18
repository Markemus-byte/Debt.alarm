# Copyright (c) 2026 Markemus-byte and Debt.alarm contributors
# SPDX-License-Identifier: AGPL-3.0-or-later
import unittest
from datetime import date, timedelta

from stilleflagg import (
    MAX_FREEZE_DAYS,
    FlagService,
    FlagType,
    costs_to_cancel,
)

PERSON = "01017012345"  # made-up test number, not a real person
NOTICE = date(2026, 1, 1)


def day(n: int) -> date:
    return NOTICE + timedelta(days=n)


class SilenceFlagTest(unittest.TestCase):
    def setUp(self):
        self.service = FlagService(secret_key=b"test-key")

    def test_flag_needs_60_days_of_silence(self):
        with self.assertRaises(ValueError):
            self.service.set_silence_flag(PERSON, "collector-a", NOTICE, None, day(59))
        flag = self.service.set_silence_flag(PERSON, "collector-a", NOTICE, None, day(60))
        self.assertIs(flag.type, FlagType.SILENCE)

    def test_recent_contact_restarts_the_count(self):
        with self.assertRaises(ValueError):
            self.service.set_silence_flag(PERSON, "collector-a", NOTICE, day(30), day(60))

    def test_flag_is_shared_across_creditors(self):
        first = self.service.set_silence_flag(PERSON, "collector-a", NOTICE, None, day(60))
        second = self.service.set_silence_flag(PERSON, "collector-b", NOTICE, None, day(61))
        self.assertIs(first, second)

    def test_flag_stores_no_national_id(self):
        flag = self.service.set_silence_flag(PERSON, "collector-a", NOTICE, None, day(60))
        self.assertNotIn(PERSON, flag.person)
        self.assertEqual(len(flag.person), 64)

    def test_fees_are_frozen_for_at_most_six_months(self):
        self.service.set_silence_flag(PERSON, "collector-a", NOTICE, None, day(60))
        self.assertEqual(
            self.service.fee_freeze_until(PERSON, day(61)), day(60 + MAX_FREEZE_DAYS)
        )
        self.assertIsNone(self.service.fee_freeze_until(PERSON, day(61 + MAX_FREEZE_DAYS)))

    def test_contact_ends_the_freeze(self):
        self.service.set_silence_flag(PERSON, "collector-a", NOTICE, None, day(60))
        self.service.record_contact(PERSON, "collector-a", day(70))
        self.assertIsNone(self.service.fee_freeze_until(PERSON, day(71)))


class PauseFlagTest(unittest.TestCase):
    def setUp(self):
        self.service = FlagService(secret_key=b"test-key")

    def test_pause_flag_freezes_fees_without_a_reason(self):
        self.service.set_pause_flag(PERSON, "nav-oslo", day(0))
        result = self.service.lookup(PERSON, "collector-a", True, day(1))
        self.assertEqual(result, {"active": True, "freeze_until": day(MAX_FREEZE_DAYS)})

    def test_contact_with_collector_does_not_lift_a_pause_flag(self):
        self.service.set_pause_flag(PERSON, "nav-oslo", day(0))
        self.service.record_contact(PERSON, "collector-a", day(5))
        self.assertIsNotNone(self.service.fee_freeze_until(PERSON, day(6)))

    def test_only_the_setter_can_close_a_pause_flag(self):
        self.service.set_pause_flag(PERSON, "nav-oslo", day(0))
        self.service.close_pause_flag(PERSON, "collector-a", day(5))
        self.assertIsNotNone(self.service.fee_freeze_until(PERSON, day(6)))
        self.service.close_pause_flag(PERSON, "nav-oslo", day(7))
        self.assertIsNone(self.service.fee_freeze_until(PERSON, day(8)))


class LookupTest(unittest.TestCase):
    def setUp(self):
        self.service = FlagService(secret_key=b"test-key")

    def test_lookup_requires_an_active_case(self):
        with self.assertRaises(PermissionError):
            self.service.lookup(PERSON, "collector-a", False, day(1))

    def test_lookup_shows_only_yes_no_and_date(self):
        result = self.service.lookup(PERSON, "collector-a", True, day(1))
        self.assertEqual(result, {"active": False, "freeze_until": None})

    def test_every_lookup_is_logged(self):
        self.service.lookup(PERSON, "collector-a", True, day(1))
        self.assertEqual(self.service.audit_log[-1][1:3], ("lookup", "collector-a"))


class WelfareCheckTest(unittest.TestCase):
    def setUp(self):
        self.service = FlagService(secret_key=b"test-key")
        self.service.set_silence_flag(PERSON, "collector-a", NOTICE, None, day(60))

    def test_check_is_due_after_90_days_and_issued_once(self):
        self.assertEqual(self.service.due_welfare_checks(day(149)), [])
        due = self.service.due_welfare_checks(day(150))
        self.assertEqual(due, [self.service.pseudonym(PERSON)])
        self.assertEqual(self.service.due_welfare_checks(day(151)), [])

    def test_no_check_after_contact(self):
        self.service.record_contact(PERSON, "collector-a", day(100))
        self.assertEqual(self.service.due_welfare_checks(day(150)), [])


class DeathTest(unittest.TestCase):
    def test_costs_after_the_date_of_death_fall_away(self):
        costs = [(day(10), 750), (day(40), 38), (day(80), 2240)]
        self.assertEqual(costs_to_cancel(costs, day(40)), [(day(80), 2240)])


class RetentionTest(unittest.TestCase):
    def test_closed_flags_are_deleted_after_12_months(self):
        service = FlagService(secret_key=b"test-key")
        service.set_silence_flag(PERSON, "collector-a", NOTICE, None, day(60))
        service.record_contact(PERSON, "collector-a", day(70))
        service.purge(day(70 + 365))
        self.assertEqual(len(service._flags), 1)
        service.purge(day(70 + 366))
        self.assertEqual(len(service._flags), 0)


if __name__ == "__main__":
    unittest.main()
