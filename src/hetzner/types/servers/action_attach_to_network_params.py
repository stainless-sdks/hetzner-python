# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ActionAttachToNetworkParams"]


class ActionAttachToNetworkParams(TypedDict, total=False):
    network: Required[int]
    """ID of an existing network to attach the Server to"""

    alias_ips: List[str]
    """Additional IPs to be assigned to this Server"""

    ip: str
    """
    IP to request to be assigned to this Server; if you do not provide this then you
    will be auto assigned an IP address
    """
