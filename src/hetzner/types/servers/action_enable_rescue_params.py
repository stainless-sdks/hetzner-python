# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ActionEnableRescueParams"]


class ActionEnableRescueParams(TypedDict, total=False):
    ssh_keys: List[int]
    """Array of SSH key IDs which should be injected into the rescue system."""

    type: Literal["linux32", "linux64"]
    """Type of rescue system to boot (default: `linux64`)"""
