# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["PrimaryIPUpdateParams"]


class PrimaryIPUpdateParams(TypedDict, total=False):
    auto_delete: bool
    """Delete this Primary IP when the resource it is assigned to is deleted"""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    name: str
    """New unique name to set"""
