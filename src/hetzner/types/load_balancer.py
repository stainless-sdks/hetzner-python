# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .price import Price
from .shared import HealthStatus
from .._models import BaseModel
from .load_balancer_target_ip import LoadBalancerTargetIp
from .load_balancer_service_model import LoadBalancerServiceModel

__all__ = [
    "LoadBalancer",
    "Algorithm",
    "LoadBalancerType",
    "LoadBalancerTypePrice",
    "Location",
    "PrivateNet",
    "Protection",
    "PublicNet",
    "PublicNetIpv4",
    "PublicNetIpv6",
    "Target",
    "TargetLabelSelector",
    "TargetServer",
    "TargetTarget",
    "TargetTargetServer",
]


class Algorithm(BaseModel):
    type: Literal["least_connections", "round_robin"]
    """Type of the algorithm | Algorithm of the Load Balancer"""


class LoadBalancerTypePrice(BaseModel):
    location: str
    """Name of the Location the price is for"""

    price_hourly: Price
    """
    Hourly costs for a Resource in this Location | Monthly costs for a Resource in
    this Location | Monthly costs for a Floating IP type in this Location | Hourly
    costs for a Load Balancer type in this network zone | Monthly costs for a Load
    Balancer type in this network zone | Hourly costs for a Primary IP type in this
    Location | Monthly costs for a Primary IP type in this Location | Hourly costs
    for a Server type in this Location | Monthly costs for a Server type in this
    Location
    """

    price_monthly: Price
    """
    Hourly costs for a Resource in this Location | Monthly costs for a Resource in
    this Location | Monthly costs for a Floating IP type in this Location | Hourly
    costs for a Load Balancer type in this network zone | Monthly costs for a Load
    Balancer type in this network zone | Hourly costs for a Primary IP type in this
    Location | Monthly costs for a Primary IP type in this Location | Hourly costs
    for a Server type in this Location | Monthly costs for a Server type in this
    Location
    """


class LoadBalancerType(BaseModel):
    id: int
    """ID of the Load Balancer type"""

    deprecated: Optional[str]
    """Point in time when the Load Balancer type is deprecated (in ISO-8601 format)"""

    description: str
    """Description of the Load Balancer type"""

    max_assigned_certificates: int
    """Number of SSL Certificates that can be assigned to a single Load Balancer"""

    max_connections: int
    """Number of maximum simultaneous open connections"""

    max_services: int
    """Number of services a Load Balancer of this type can have"""

    max_targets: int
    """Number of targets a single Load Balancer can have"""

    name: str
    """Unique identifier of the Load Balancer type"""

    prices: List[LoadBalancerTypePrice]
    """Prices in different network zones"""


class Location(BaseModel):
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


class PrivateNet(BaseModel):
    ip: Optional[str] = None
    """IP address (v4) of this Load Balancer in this Network"""

    network: Optional[int] = None
    """ID of the Network"""


class Protection(BaseModel):
    delete: bool
    """
    If true, prevents the Resource from being deleted | If true, prevents the
    Network from being deleted
    """


class PublicNetIpv4(BaseModel):
    dns_ptr: Optional[str] = None
    """Reverse DNS PTR entry for the IPv4 address of this Load Balancer"""

    ip: Optional[str] = None
    """IP address (v4) of this Load Balancer"""


class PublicNetIpv6(BaseModel):
    dns_ptr: Optional[str] = None
    """Reverse DNS PTR entry for the IPv6 address of this Load Balancer"""

    ip: Optional[str] = None
    """IP address (v6) of this Load Balancer"""


class PublicNet(BaseModel):
    enabled: bool
    """Public Interface enabled or not"""

    ipv4: PublicNetIpv4
    """IP address (v4)"""

    ipv6: PublicNetIpv6
    """IP address (v6)"""


class TargetLabelSelector(BaseModel):
    selector: str
    """Label selector"""


class TargetServer(BaseModel):
    id: int
    """ID of the Resource | ID of the Server"""


class TargetTargetServer(BaseModel):
    id: int
    """ID of the Resource | ID of the Server"""


class TargetTarget(BaseModel):
    health_status: Optional[List[HealthStatus]] = None
    """List of health statuses of the services on this target.

    Only present for target types "server" and "ip".
    """

    server: Optional[TargetTargetServer] = None
    """ID of the Resource"""

    type: Optional[str] = None
    """Type of the resource. Here always "server"."""

    use_private_ip: Optional[bool] = None
    """Use the private network IP instead of the public IP.

    Default value is false. Only present for target types "server" and
    "label_selector".
    """


class Target(BaseModel):
    type: Literal["ip", "label_selector", "server"]
    """Type of the resource"""

    health_status: Optional[List[HealthStatus]] = None
    """List of health statuses of the services on this target.

    Only present for target types "server" and "ip".
    """

    ip: Optional[LoadBalancerTargetIp] = None
    """IP targets where the traffic should be routed to.

    It is only possible to use the (Public or vSwitch) IPs of Hetzner Online Root
    Servers belonging to the project owner. IPs belonging to other users are
    blocked. Additionally IPs belonging to services provided by Hetzner Cloud
    (Servers, Load Balancers, ...) are blocked as well. Only present for target type
    "ip".
    """

    label_selector: Optional[TargetLabelSelector] = None
    """Configuration for type LabelSelector, required if type is `label_selector`"""

    server: Optional[TargetServer] = None
    """ID of the Resource"""

    targets: Optional[List[TargetTarget]] = None
    """List of resolved label selector target Servers.

    Only present for type "label_selector".
    """

    use_private_ip: Optional[bool] = None
    """Use the private network IP instead of the public IP.

    Default value is false. Only present for target types "server" and
    "label_selector".
    """


class LoadBalancer(BaseModel):
    id: int
    """ID of the Resource"""

    algorithm: Algorithm
    """
    Algorithm of the Load Balancer | Request for POST
    https://api.hetzner.cloud/v1/load_balancers/{id}/actions/change_algorithm
    """

    created: str
    """Point in time when the Resource was created (in ISO-8601 format)"""

    included_traffic: int
    """Free Traffic for the current billing period in bytes"""

    ingoing_traffic: Optional[int]
    """Inbound Traffic for the current billing period in bytes"""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    load_balancer_type: LoadBalancerType

    location: Location
    """Location the Floating IP was created in.

    Routing is optimized for this Location. | Location of the Volume. Volume can
    only be attached to Servers in the same Location.
    """

    name: str
    """Name of the Resource. Must be unique per Project."""

    outgoing_traffic: Optional[int]
    """Outbound Traffic for the current billing period in bytes"""

    private_net: List[PrivateNet]
    """Private networks information"""

    protection: Protection
    """Protection configuration for the Resource"""

    public_net: PublicNet
    """Public network information"""

    services: List[LoadBalancerServiceModel]
    """List of services that belong to this Load Balancer"""

    targets: List[Target]
    """List of targets that belong to this Load Balancer"""
