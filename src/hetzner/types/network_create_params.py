# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["NetworkCreateParams", "Route", "Subnet"]


class NetworkCreateParams(TypedDict, total=False):
    ip_range: Required[str]
    """IP range of the whole network which must span all included subnets.

    Must be one of the private IPv4 ranges of RFC1918. Minimum network size is /24.
    We highly recommend that you pick a larger network with a /16 netmask.
    """

    name: Required[str]
    """Name of the network"""

    expose_routes_to_vswitch: bool
    """
    Indicates if the routes from this network should be exposed to the vSwitch
    connection. The exposing only takes effect if a vSwitch connection is active.

    Currently the default route 0.0.0.0/0 is not exposed to the vSwitch connection.
    We are aware of the issue and are working on a solution.
    """

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    routes: List[Route]
    """Array of routes set in this network.

    The destination of the route must be one of the private IPv4 ranges of RFC1918.
    The gateway must be a subnet/IP of the ip_range of the network object. The
    destination must not overlap with an existing ip_range in any subnets or with
    any destinations in other routes or with the first IP of the networks ip_range
    or with 172.31.1.1. The gateway cannot be the first IP of the networks ip_range
    and also cannot be 172.31.1.1.
    """

    subnets: List[Subnet]
    """Array of subnets allocated."""


class Route(TypedDict, total=False):
    destination: Required[str]
    """Destination network or host of this route.

    Must not overlap with an existing ip_range in any subnets or with any
    destinations in other routes or with the first IP of the networks ip_range or
    with 172.31.1.1. Must be one of the private IPv4 ranges of RFC1918.
    """

    gateway: Required[str]
    """Gateway for the route.

    Cannot be the first IP of the networks ip_range and also cannot be 172.31.1.1 as
    this IP is being used as a gateway for the public network interface of Servers.
    | Gateway for the route. Cannot be the first IP of the networks ip_range, an IP
    behind a vSwitch or 172.31.1.1, as this IP is being used as a gateway for the
    public network interface of Servers.
    """


class Subnet(TypedDict, total=False):
    network_zone: Required[str]
    """Name of Network zone.

    The Location object contains the `network_zone` property each Location belongs
    to.
    """

    type: Required[Literal["cloud", "server", "vswitch"]]
    """Type of Subnetwork"""

    ip_range: str
    """Range to allocate IPs from.

    Must be a Subnet of the ip_range of the parent network object and must not
    overlap with any other subnets or with any destinations in routes. Minimum
    Network size is /30. We suggest that you pick a bigger Network with a /24
    netmask. | Range to allocate IPs from. Must be a Subnet of the ip_range of the
    parent network object and must not overlap with any other subnets or with any
    destinations in routes. If the Subnet is of type vSwitch, it also can not
    overlap with any gateway in routes. Minimum Network size is /30. We suggest that
    you pick a bigger Network with a /24 netmask.
    """

    vswitch_id: int
    """ID of the robot vSwitch. Must be supplied if the subnet is of type vswitch."""
