# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .shared import ResponseMeta
from .._models import BaseModel

__all__ = ["ISOListResponse", "ISO"]


class ISO(BaseModel):
    id: int
    """ID of the Resource"""

    architecture: Optional[Literal["arm", "x86"]]
    """Type of cpu architecture this iso is compatible with.

    Null indicates no restriction on the architecture (wildcard).
    """

    deprecated: Optional[str]
    """ISO 8601 timestamp of deprecation, null if ISO is still available.

    After the deprecation time it will no longer be possible to attach the ISO to
    Servers.
    """

    description: str
    """Description of the ISO"""

    name: Optional[str]
    """Unique identifier of the ISO. Only set for public ISOs"""

    type: Literal["private", "public"]
    """Type of the ISO"""


class ISOListResponse(BaseModel):
    isos: List[ISO]

    meta: Optional[ResponseMeta] = None
    """Metadata contained in the response"""
