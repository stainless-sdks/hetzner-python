# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, TypedDict

__all__ = ["ImageUpdateParams"]


class ImageUpdateParams(TypedDict, total=False):
    description: str
    """New description of Image"""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    type: Literal["snapshot"]
    """Destination Image type to convert to"""
