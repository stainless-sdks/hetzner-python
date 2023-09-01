# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PlacementGroup"]


class PlacementGroup(BaseModel):
    id: int
    """ID of the Resource"""

    created: str
    """Point in time when the Resource was created (in ISO-8601 format)"""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    name: str
    """Name of the Resource. Must be unique per Project."""

    servers: List[int]
    """Array of IDs of Servers that are part of this Placement Group"""

    type: Literal["spread"]
    """Type of the Placement Group"""
