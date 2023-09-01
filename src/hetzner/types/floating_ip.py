# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FloatingIP", "DNSPtr", "HomeLocation", "Protection"]


class DNSPtr(BaseModel):
    dns_ptr: str
    """DNS pointer for the specific IP address"""

    ip: str
    """
    Single IPv4 or IPv6 address | Single IPv6 address of this Server for which the
    reverse DNS entry has been set up
    """


class HomeLocation(BaseModel):
    id: int
    """ID of the Location"""

    city: str
    """City the Location is closest to"""

    country: str
    """ISO 3166-1 alpha-2 code of the country the Location resides in"""

    description: str
    """Description of the Location"""

    latitude: float
    """Latitude of the city closest to the Location"""

    longitude: float
    """Longitude of the city closest to the Location"""

    name: str
    """Unique identifier of the Location"""

    network_zone: str
    """Name of network zone this Location resides in"""


class Protection(BaseModel):
    delete: bool
    """
    If true, prevents the Resource from being deleted | If true, prevents the
    Network from being deleted
    """


class FloatingIP(BaseModel):
    id: int
    """ID of the Resource"""

    blocked: bool
    """Whether the IP is blocked"""

    created: str
    """Point in time when the Resource was created (in ISO-8601 format)"""

    description: Optional[str]
    """Description of the Resource"""

    dns_ptr: List[DNSPtr]
    """Array of reverse DNS entries"""

    home_location: HomeLocation
    """Location the Floating IP was created in.

    Routing is optimized for this Location. | Location of the Volume. Volume can
    only be attached to Servers in the same Location.
    """

    ip: str
    """IP address"""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    name: str
    """Name of the Resource. Must be unique per Project."""

    protection: Protection
    """Protection configuration for the Resource"""

    server: Optional[int]
    """
    ID of the Server the Floating IP is assigned to, null if it is not assigned at
    all
    """

    type: Literal["ipv4", "ipv6"]
    """The type of the IP"""
