# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionAttachToNetworkParams"]


class ActionAttachToNetworkParams(TypedDict, total=False):
    network: Required[int]
    """ID of an existing network to attach the Load Balancer to"""

    ip: str
    """
    IP to request to be assigned to this Load Balancer; if you do not provide this
    then you will be auto assigned an IP address
    """
