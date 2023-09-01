# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionDeleteRouteParams"]


class ActionDeleteRouteParams(TypedDict, total=False):
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
