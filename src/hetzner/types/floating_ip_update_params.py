# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["FloatingIpUpdateParams"]


class FloatingIpUpdateParams(TypedDict, total=False):
    description: str
    """New Description to set"""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    name: str
    """New unique name to set"""
