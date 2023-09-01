# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .shared import ResponseMeta
from .._models import BaseModel

__all__ = ["NetworkListResponse", "Network", "NetworkProtection", "NetworkRoute", "NetworkSubnet"]


class NetworkProtection(BaseModel):
    delete: bool
    """
    If true, prevents the Resource from being deleted | If true, prevents the
    Network from being deleted
    """


class NetworkRoute(BaseModel):
    destination: str
    """Destination network or host of this route.

    Must not overlap with an existing ip_range in any subnets or with any
    destinations in other routes or with the first IP of the networks ip_range or
    with 172.31.1.1. Must be one of the private IPv4 ranges of RFC1918.
    """

    gateway: str
    """Gateway for the route.

    Cannot be the first IP of the networks ip_range and also cannot be 172.31.1.1 as
    this IP is being used as a gateway for the public network interface of Servers.
    | Gateway for the route. Cannot be the first IP of the networks ip_range, an IP
    behind a vSwitch or 172.31.1.1, as this IP is being used as a gateway for the
    public network interface of Servers.
    """


class NetworkSubnet(BaseModel):
    gateway: str
    """Gateway for Servers attached to this subnet.

    For subnets of type Server this is always the first IP of the network IP range.
    """

    network_zone: str
    """Name of Network zone.

    The Location object contains the `network_zone` property each Location belongs
    to.
    """

    type: Literal["cloud", "server", "vswitch"]
    """Type of Subnetwork"""

    ip_range: Optional[str] = None
    """Range to allocate IPs from.

    Must be a Subnet of the ip_range of the parent network object and must not
    overlap with any other subnets or with any destinations in routes. Minimum
    Network size is /30. We suggest that you pick a bigger Network with a /24
    netmask.
    """

    vswitch_id: Optional[int] = None
    """ID of the robot vSwitch if the subnet is of type vswitch."""


class Network(BaseModel):
    id: int
    """ID of the Network"""

    created: str
    """Point in time when the Network was created (in ISO-8601 format)"""

    expose_routes_to_vswitch: bool
    """
    Indicates if the routes from this network should be exposed to the vSwitch
    connection. The exposing only takes effect if a vSwitch connection is active.

    Currently the default route 0.0.0.0/0 is not exposed to the vSwitch connection.
    We are aware of the issue and are working on a solution.
    """

    ip_range: str
    """IPv4 prefix of the whole Network"""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    name: str
    """Name of the Network"""

    protection: NetworkProtection
    """Protection configuration for the Resource"""

    routes: List[NetworkRoute]
    """Array of routes set in this Network"""

    servers: List[int]
    """Array of IDs of Servers attached to this Network"""

    subnets: List[NetworkSubnet]
    """Array subnets allocated in this Network"""

    load_balancers: Optional[List[int]] = None
    """Array of IDs of Load Balancers attached to this Network"""


class NetworkListResponse(BaseModel):
    networks: List[Network]

    meta: Optional[ResponseMeta] = None
    """Metadata contained in the response"""
