# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, TypedDict

__all__ = ["ActionCreateImageParams"]


class ActionCreateImageParams(TypedDict, total=False):
    description: str
    """Description of the Image, will be auto-generated if not set"""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    type: Literal["backup", "snapshot"]
    """Type of Image to create (default: `snapshot`)"""
