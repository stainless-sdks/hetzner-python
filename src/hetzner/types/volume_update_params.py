# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["VolumeUpdateParams"]


class VolumeUpdateParams(TypedDict, total=False):
    name: Required[str]
    """New Volume name"""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""
