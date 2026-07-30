"""Calendar helpers for event booking service."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def calendar_step_0(records: list[dict], limit: int = 328) -> list[dict]:
    """Apply calendar rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("calendar step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def calendar_step_1(records: list[dict], limit: int = 305) -> list[dict]:
    """Apply calendar rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("calendar step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def calendar_step_2(records: list[dict], limit: int = 11) -> list[dict]:
    """Apply calendar rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("calendar step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def calendar_step_3(records: list[dict], limit: int = 152) -> list[dict]:
    """Apply calendar rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("calendar step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def calendar_step_4(records: list[dict], limit: int = 129) -> list[dict]:
    """Apply calendar rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("calendar step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def calendar_step_5(records: list[dict], limit: int = 379) -> list[dict]:
    """Apply calendar rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("calendar step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
