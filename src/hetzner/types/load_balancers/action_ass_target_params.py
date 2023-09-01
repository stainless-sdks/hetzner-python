# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..load_balancer_target_ip_param import LoadBalancerTargetIPParam

__all__ = ["ActionAssTargetParams", "LabelSelector", "Server"]


class ActionAssTargetParams(TypedDict, total=False):
    type: Required[Literal["ip", "label_selector", "server"]]
    """Type of the resource"""

    ip: LoadBalancerTargetIPParam
    """IP targets where the traffic should be routed to.

    It is only possible to use the (Public or vSwitch) IPs of Hetzner Online Root
    Servers belonging to the project owner. IPs belonging to other users are
    blocked. Additionally IPs belonging to services provided by Hetzner Cloud
    (Servers, Load Balancers, ...) are blocked as well. Only present for target type
    "ip".
    """

    label_selector: LabelSelector
    """Configuration for type LabelSelector, required if type is `label_selector`"""

    server: Server
    """Configuration for type Server, required if type is `server`"""

    use_private_ip: bool
    """
    Use the private network IP instead of the public IP of the Server, requires the
    Server and Load Balancer to be in the same network. Default value is false.
    """


class LabelSelector(TypedDict, total=False):
    selector: Required[str]
    """Label selector"""


class Server(TypedDict, total=False):
    id: Required[int]
    """ID of the Server"""
