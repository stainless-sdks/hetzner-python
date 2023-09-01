# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ServerPublicNet", "Ipv4", "Ipv6", "Ipv6DNSPtr", "Firewall"]


class Ipv4(BaseModel):
    blocked: bool
    """If the IP is blocked by our anti abuse dept"""

    dns_ptr: str
    """Reverse DNS PTR entry for the IPv4 addresses of this Server"""

    ip: str
    """IP address (v4) of this Server"""

    id: Optional[int] = None
    """ID of the Resource"""


class Ipv6DNSPtr(BaseModel):
    dns_ptr: str
    """DNS pointer for the specific IP address"""

    ip: str
    """
    Single IPv4 or IPv6 address | Single IPv6 address of this Server for which the
    reverse DNS entry has been set up
    """


class Ipv6(BaseModel):
    blocked: bool
    """If the IP is blocked by our anti abuse dept"""

    dns_ptr: Optional[List[Ipv6DNSPtr]]
    """
    Reverse DNS PTR entries for the IPv6 addresses of this Server, `null` by default
    """

    ip: str
    """IP address (v6) of this Server"""

    id: Optional[int] = None
    """ID of the Resource"""


class Firewall(BaseModel):
    id: Optional[int] = None
    """ID of the Resource"""

    status: Optional[Literal["applied", "pending"]] = None
    """Status of the Firewall on the Server"""


class ServerPublicNet(BaseModel):
    floating_ips: List[int]
    """IDs of Floating IPs assigned to this Server"""

    ipv4: Optional[Ipv4]
    """IP address (v4) and its reverse DNS entry of this Server"""

    ipv6: Optional[Ipv6]
    """IPv6 network assigned to this Server and its reverse DNS entry"""

    firewalls: Optional[List[Firewall]] = None
    """Firewalls applied to the public network interface of this Server"""
