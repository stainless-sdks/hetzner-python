# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PlacementGroupCreateParams"]


class PlacementGroupCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the PlacementGroup"""

    type: Required[Literal["spread"]]
    """Define the Placement Group Type."""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""
