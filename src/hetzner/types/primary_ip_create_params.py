# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PrimaryIpCreateParams"]


class PrimaryIpCreateParams(TypedDict, total=False):
    assignee_type: Required[Literal["server"]]
    """Resource type the Primary IP can be assigned to"""

    name: Required[str]

    type: Required[Literal["ipv4", "ipv6"]]
    """The type of the IP"""

    assignee_id: int
    """ID of the resource the Primary IP should be assigned to.

    Omitted if it should not be assigned.
    """

    auto_delete: bool
    """Delete the Primary IP when the Server it is assigned to is deleted.

    If omitted defaults to `false`.
    """

    datacenter: str
    """ID or name of Datacenter the Primary IP will be bound to.

    Needs to be omitted if `assignee_id` is passed.
    """

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""
