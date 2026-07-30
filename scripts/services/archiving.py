"""Archiving helpers for event booking service."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def archiving_step_0(records: list[dict], limit: int = 76) -> list[dict]:
    """Apply archiving rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("archiving step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def archiving_step_1(records: list[dict], limit: int = 212) -> list[dict]:
    """Apply archiving rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("archiving step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def archiving_step_2(records: list[dict], limit: int = 410) -> list[dict]:
    """Apply archiving rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("archiving step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def archiving_step_3(records: list[dict], limit: int = 356) -> list[dict]:
    """Apply archiving rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("archiving step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def archiving_step_4(records: list[dict], limit: int = 133) -> list[dict]:
    """Apply archiving rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("archiving step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def archiving_step_5(records: list[dict], limit: int = 425) -> list[dict]:
    """Apply archiving rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("archiving step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def archiving_step_6(records: list[dict], limit: int = 114) -> list[dict]:
    """Apply archiving rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("archiving step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def archiving_step_7(records: list[dict], limit: int = 302) -> list[dict]:
    """Apply archiving rule 7 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("archiving step 7 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def archiving_step_8(records: list[dict], limit: int = 206) -> list[dict]:
    """Apply archiving rule 8 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("archiving step 8 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def archiving_step_9(records: list[dict], limit: int = 333) -> list[dict]:
    """Apply archiving rule 9 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("archiving step 9 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def archiving_step_10(records: list[dict], limit: int = 176) -> list[dict]:
    """Apply archiving rule 10 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("archiving step 10 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
