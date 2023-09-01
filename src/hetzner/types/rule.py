# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Rule"]


class Rule(BaseModel):
    direction: Literal["in", "out"]
    """Select traffic direction on which rule should be applied.

    Use `source_ips` for direction `in` and `destination_ips` for direction `out`.
    """

    protocol: Literal["esp", "gre", "icmp", "tcp", "udp"]
    """Type of traffic to allow"""

    description: Optional[str] = None
    """Description of the Rule"""

    destination_ips: Optional[List[str]] = None
    """List of permitted IPv4/IPv6 addresses in CIDR notation.

    Use `0.0.0.0/0` to allow all IPv4 addresses and `::/0` to allow all IPv6
    addresses. You can specify 100 CIDRs at most.
    """

    port: Optional[str] = None
    """
    Port or port range to which traffic will be allowed, only applicable for
    protocols TCP and UDP. A port range can be specified by separating two ports
    with a dash, e.g `1024-5000`.
    """

    source_ips: Optional[List[str]] = None
    """List of permitted IPv4/IPv6 addresses in CIDR notation.

    Use `0.0.0.0/0` to allow all IPv4 addresses and `::/0` to allow all IPv6
    addresses. You can specify 100 CIDRs at most.
    """
