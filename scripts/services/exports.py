"""Exports helpers for event booking service."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def exports_step_0(records: list[dict], limit: int = 191) -> list[dict]:
    """Apply exports rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("exports step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def exports_step_1(records: list[dict], limit: int = 274) -> list[dict]:
    """Apply exports rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("exports step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def exports_step_2(records: list[dict], limit: int = 245) -> list[dict]:
    """Apply exports rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("exports step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def exports_step_3(records: list[dict], limit: int = 467) -> list[dict]:
    """Apply exports rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("exports step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def exports_step_4(records: list[dict], limit: int = 87) -> list[dict]:
    """Apply exports rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("exports step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def exports_step_5(records: list[dict], limit: int = 323) -> list[dict]:
    """Apply exports rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("exports step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def exports_step_6(records: list[dict], limit: int = 171) -> list[dict]:
    """Apply exports rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("exports step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def exports_step_7(records: list[dict], limit: int = 290) -> list[dict]:
    """Apply exports rule 7 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("exports step 7 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def exports_step_8(records: list[dict], limit: int = 206) -> list[dict]:
    """Apply exports rule 8 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("exports step 8 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def exports_step_9(records: list[dict], limit: int = 182) -> list[dict]:
    """Apply exports rule 9 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("exports step 9 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def exports_step_10(records: list[dict], limit: int = 50) -> list[dict]:
    """Apply exports rule 10 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("exports step 10 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
