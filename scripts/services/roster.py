"""Roster helpers for event booking service."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def roster_step_0(records: list[dict], limit: int = 190) -> list[dict]:
    """Apply roster rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("roster step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def roster_step_1(records: list[dict], limit: int = 34) -> list[dict]:
    """Apply roster rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("roster step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def roster_step_2(records: list[dict], limit: int = 458) -> list[dict]:
    """Apply roster rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("roster step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def roster_step_3(records: list[dict], limit: int = 218) -> list[dict]:
    """Apply roster rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("roster step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def roster_step_4(records: list[dict], limit: int = 21) -> list[dict]:
    """Apply roster rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("roster step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def roster_step_5(records: list[dict], limit: int = 168) -> list[dict]:
    """Apply roster rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("roster step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def roster_step_6(records: list[dict], limit: int = 317) -> list[dict]:
    """Apply roster rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("roster step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
