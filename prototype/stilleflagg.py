# Copyright (c) 2026 Markemus-byte and Debt.alarm contributors
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Reference model of the Silence Flag rules (docs/forslag.md, docs/teknisk-konsept.md).

This is a prototype for discussion, not a production service. It keeps
everything in memory and uses only the Python standard library.
"""

import hashlib
import hmac
from dataclasses import dataclass
from datetime import date, timedelta
from enum import Enum
from typing import Optional

# Time limits from the proposal. All are starting points for discussion.
SILENCE_DAYS = 60  # days without contact or payment after the collection notice
WELFARE_CHECK_DAYS = 90  # days with an open silence flag before a welfare check
MAX_FREEZE_DAYS = 182  # fee freeze lasts at most about 6 months
RETENTION_DAYS = 365  # closed flags are deleted after 12 months


class FlagType(Enum):
    SILENCE = "silence"  # set by a collector after 60 days of silence
    PAUSE = "pause"  # set by health services, NAV or a guardian, no reason given


@dataclass
class Flag:
    person: str  # pseudonym, never the national ID number
    type: FlagType
    set_by: str
    set_on: date
    closed_on: Optional[date] = None
    welfare_check_issued: bool = False

    @property
    def is_open(self) -> bool:
        return self.closed_on is None


class FlagService:
    def __init__(self, secret_key: bytes):
        self._key = secret_key
        self._flags: list[Flag] = []
        self.audit_log: list[tuple[date, str, str, str]] = []

    def pseudonym(self, national_id: str) -> str:
        return hmac.new(self._key, national_id.encode(), hashlib.sha256).hexdigest()

    def _log(self, today: date, action: str, org: str, person: str) -> None:
        self.audit_log.append((today, action, org, person))

    def _open_flags(self, person: str) -> list[Flag]:
        return [f for f in self._flags if f.person == person and f.is_open]

    def set_silence_flag(
        self,
        national_id: str,
        collector: str,
        notice_sent_on: date,
        last_contact_on: Optional[date],
        today: date,
    ) -> Flag:
        """Set a silence flag once 60 days have passed with no contact or payment."""
        silent_since = max(notice_sent_on, last_contact_on or notice_sent_on)
        if (today - silent_since).days < SILENCE_DAYS:
            raise ValueError(f"Fewer than {SILENCE_DAYS} days of silence")

        person = self.pseudonym(national_id)
        for flag in self._open_flags(person):
            if flag.type is FlagType.SILENCE:
                # The flag belongs to the person, so one is enough across creditors.
                return flag

        flag = Flag(person, FlagType.SILENCE, collector, today)
        self._flags.append(flag)
        self._log(today, "set_silence", collector, person)
        return flag

    def set_pause_flag(self, national_id: str, org: str, today: date) -> Flag:
        person = self.pseudonym(national_id)
        flag = Flag(person, FlagType.PAUSE, org, today)
        self._flags.append(flag)
        self._log(today, "set_pause", org, person)
        return flag

    def close_pause_flag(self, national_id: str, org: str, today: date) -> None:
        person = self.pseudonym(national_id)
        for flag in self._open_flags(person):
            if flag.type is FlagType.PAUSE and flag.set_by == org:
                flag.closed_on = today
                self._log(today, "close_pause", org, person)

    def record_contact(self, national_id: str, org: str, today: date) -> None:
        """Contact with the person was made, so silence flags end."""
        person = self.pseudonym(national_id)
        for flag in self._open_flags(person):
            if flag.type is FlagType.SILENCE:
                flag.closed_on = today
                self._log(today, "contact", org, person)

    def fee_freeze_until(self, national_id: str, today: date) -> Optional[date]:
        """The last day of the fee freeze, or None if fees are not frozen."""
        person = self.pseudonym(national_id)
        ends = [
            f.set_on + timedelta(days=MAX_FREEZE_DAYS) for f in self._open_flags(person)
        ]
        active = [end for end in ends if today <= end]
        return max(active) if active else None

    def lookup(
        self, national_id: str, collector: str, has_active_case: bool, today: date
    ) -> dict:
        """What a collector may see: yes/no and the freeze date, nothing else."""
        if not has_active_case:
            raise PermissionError("Lookups are only allowed for active cases")
        person = self.pseudonym(national_id)
        self._log(today, "lookup", collector, person)
        freeze_until = self.fee_freeze_until(national_id, today)
        return {"active": freeze_until is not None, "freeze_until": freeze_until}

    def due_welfare_checks(self, today: date) -> list[str]:
        """Pseudonyms whose silence flag has been open for 90 days, each issued once."""
        due = []
        for flag in self._flags:
            if (
                flag.is_open
                and flag.type is FlagType.SILENCE
                and not flag.welfare_check_issued
                and (today - flag.set_on).days >= WELFARE_CHECK_DAYS
            ):
                flag.welfare_check_issued = True
                self._log(today, "welfare_check", "flag-service", flag.person)
                due.append(flag.person)
        return due

    def purge(self, today: date) -> None:
        """Delete flags that were closed more than 12 months ago."""
        self._flags = [
            f
            for f in self._flags
            if f.is_open or (today - f.closed_on).days <= RETENTION_DAYS
        ]


def costs_to_cancel(
    costs: list[tuple[date, int]], date_of_death: date
) -> list[tuple[date, int]]:
    """Collection costs and interest added after the date of death fall away."""
    return [(day, amount) for day, amount in costs if day > date_of_death]
