# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, TypedDict

from ..types import shared_params
from .load_balancer_target_ip_param import LoadBalancerTargetIPParam
from .load_balancer_service_model_param import LoadBalancerServiceModelParam

__all__ = [
    "LoadBalancerCreateParams",
    "Algorithm",
    "Target",
    "TargetLabelSelector",
    "TargetServer",
    "TargetTarget",
    "TargetTargetServer",
]


class LoadBalancerCreateParams(TypedDict, total=False):
    algorithm: Required[Algorithm]
    """
    Algorithm of the Load Balancer | Request for POST
    https://api.hetzner.cloud/v1/load_balancers/{id}/actions/change_algorithm
    """

    load_balancer_type: Required[str]
    """ID or name of the Load Balancer type this Load Balancer should be created with"""

    name: Required[str]
    """Name of the Load Balancer"""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    location: str
    """ID or name of Location to create Load Balancer in"""

    network: int
    """ID of the network the Load Balancer should be attached to on creation"""

    network_zone: str
    """Name of network zone"""

    public_interface: bool
    """Enable or disable the public interface of the Load Balancer"""

    services: List[LoadBalancerServiceModelParam]
    """Array of services"""

    targets: List[Target]
    """Array of targets"""


class Algorithm(TypedDict, total=False):
    type: Required[Literal["least_connections", "round_robin"]]
    """Type of the algorithm | Algorithm of the Load Balancer"""


class TargetLabelSelector(TypedDict, total=False):
    selector: Required[str]
    """Label selector"""


class TargetServer(TypedDict, total=False):
    id: Required[int]
    """ID of the Resource | ID of the Server"""


class TargetTargetServer(TypedDict, total=False):
    id: Required[int]
    """ID of the Resource | ID of the Server"""


class TargetTarget(TypedDict, total=False):
    health_status: List[shared_params.HealthStatus]
    """List of health statuses of the services on this target.

    Only present for target types "server" and "ip".
    """

    server: TargetTargetServer
    """ID of the Resource"""

    type: str
    """Type of the resource. Here always "server"."""

    use_private_ip: bool
    """Use the private network IP instead of the public IP.

    Default value is false. Only present for target types "server" and
    "label_selector".
    """


class Target(TypedDict, total=False):
    type: Required[Literal["ip", "label_selector", "server"]]
    """Type of the resource"""

    health_status: List[shared_params.HealthStatus]
    """List of health statuses of the services on this target.

    Only present for target types "server" and "ip".
    """

    ip: LoadBalancerTargetIPParam
    """IP targets where the traffic should be routed to.

    It is only possible to use the (Public or vSwitch) IPs of Hetzner Online Root
    Servers belonging to the project owner. IPs belonging to other users are
    blocked. Additionally IPs belonging to services provided by Hetzner Cloud
    (Servers, Load Balancers, ...) are blocked as well. Only present for target type
    "ip".
    """

    label_selector: TargetLabelSelector
    """Configuration for type LabelSelector, required if type is `label_selector`"""

    server: TargetServer
    """ID of the Resource"""

    targets: List[TargetTarget]
    """List of resolved label selector target Servers.

    Only present for type "label_selector".
    """

    use_private_ip: bool
    """Use the private network IP instead of the public IP.

    Default value is false. Only present for target types "server" and
    "label_selector".
    """
