# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FloatingIPCreateParams"]


class FloatingIPCreateParams(TypedDict, total=False):
    type: Required[Literal["ipv4", "ipv6"]]
    """The type of the IP"""

    description: str

    home_location: str
    """Home Location (routing is optimized for that Location).

    Only optional if Server argument is passed.
    """

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    name: str

    server: int
    """ID of the Server to assign the Floating IP to"""
