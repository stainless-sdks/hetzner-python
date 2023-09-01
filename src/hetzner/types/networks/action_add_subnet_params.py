# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionAddSubnetParams"]


class ActionAddSubnetParams(TypedDict, total=False):
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
