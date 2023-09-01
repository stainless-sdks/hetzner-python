# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PrimaryIP", "Datacenter", "DatacenterLocation", "DatacenterServerTypes", "DNSPtr", "Protection"]


class DatacenterLocation(BaseModel):
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


class DatacenterServerTypes(BaseModel):
    available: List[int]
    """
    IDs of Server types that are supported and for which the Datacenter has enough
    resources left
    """

    available_for_migration: List[int]
    """
    IDs of Server types that are supported and for which the Datacenter has enough
    resources left
    """

    supported: List[int]
    """IDs of Server types that are supported in the Datacenter"""


class Datacenter(BaseModel):
    id: int
    """ID of the Resource"""

    description: str
    """Description of the Datacenter"""

    location: DatacenterLocation
    """Location the Floating IP was created in.

    Routing is optimized for this Location. | Location of the Volume. Volume can
    only be attached to Servers in the same Location.
    """

    name: str
    """Unique identifier of the Datacenter"""

    server_types: DatacenterServerTypes
    """The Server types the Datacenter can handle"""


class DNSPtr(BaseModel):
    dns_ptr: str
    """DNS pointer for the specific IP address"""

    ip: str
    """
    Single IPv4 or IPv6 address | Single IPv6 address of this Server for which the
    reverse DNS entry has been set up
    """


class Protection(BaseModel):
    delete: bool
    """
    If true, prevents the Resource from being deleted | If true, prevents the
    Network from being deleted
    """


class PrimaryIP(BaseModel):
    id: int
    """ID of the Resource"""

    assignee_id: Optional[int]
    """
    ID of the resource the Primary IP is assigned to, null if it is not assigned at
    all
    """

    assignee_type: Literal["server"]
    """Resource type the Primary IP can be assigned to"""

    auto_delete: bool
    """Delete this Primary IP when the resource it is assigned to is deleted"""

    blocked: bool
    """Whether the IP is blocked"""

    created: str
    """Point in time when the Resource was created (in ISO-8601 format)"""

    datacenter: Datacenter
    """
    Datacenter this Primary IP is located at | Datacenter this Resource is located
    at
    """

    dns_ptr: List[DNSPtr]
    """Array of reverse DNS entries"""

    ip: str
    """IP address"""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    name: str
    """Name of the Resource. Must be unique per Project."""

    protection: Protection
    """Protection configuration for the Resource"""

    type: Literal["ipv4", "ipv6"]
    """The type of the IP"""
