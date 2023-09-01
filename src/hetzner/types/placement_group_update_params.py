# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["PlacementGroupUpdateParams"]


class PlacementGroupUpdateParams(TypedDict, total=False):
    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    name: str
    """New PlacementGroup name"""
