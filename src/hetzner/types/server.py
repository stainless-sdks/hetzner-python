# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .price import Price
from .._models import BaseModel
from .server_public_net import ServerPublicNet

__all__ = [
    "Server",
    "Datacenter",
    "DatacenterLocation",
    "DatacenterServerTypes",
    "Image",
    "ImageCreatedFrom",
    "ImageProtection",
    "Iso",
    "PrivateNet",
    "Protection",
    "ServerType",
    "ServerTypePrice",
    "PlacementGroup",
]


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


class ImageCreatedFrom(BaseModel):
    id: int
    """ID of the Server the Image was created from"""

    name: str
    """Server name at the time the Image was created"""


class ImageProtection(BaseModel):
    delete: bool
    """
    If true, prevents the Resource from being deleted | If true, prevents the
    Network from being deleted
    """


class Image(BaseModel):
    id: int
    """ID of the Resource"""

    architecture: Literal["arm", "x86"]
    """Type of cpu architecture this image is compatible with.

    | Type of cpu architecture
    """

    bound_to: Optional[int]
    """ID of Server the Image is bound to. Only set for Images of type `backup`."""

    created: str
    """Point in time when the Resource was created (in ISO-8601 format)"""

    created_from: Optional[ImageCreatedFrom]
    """Information about the Server the Image was created from"""

    deleted: Optional[str]
    """Point in time where the Image was deleted (in ISO-8601 format)"""

    deprecated: Optional[str]
    """
    Point in time when the Image is considered to be deprecated (in ISO-8601 format)
    """

    description: str
    """Description of the Image"""

    disk_size: float
    """Size of the disk contained in the Image in GB"""

    image_size: Optional[float]
    """Size of the Image file in our storage in GB.

    For snapshot Images this is the value relevant for calculating costs for the
    Image.
    """

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    name: Optional[str]
    """Unique identifier of the Image. This value is only set for system Images."""

    os_flavor: Literal["alma", "centos", "debian", "fedora", "rocky", "ubuntu", "unknown"]
    """Flavor of operating system contained in the Image"""

    os_version: Optional[str]
    """Operating system version"""

    protection: ImageProtection
    """Protection configuration for the Resource"""

    status: Literal["available", "creating", "unavailable"]
    """Whether the Image can be used or if it's still being created or unavailable"""

    type: Literal["app", "backup", "snapshot", "system", "temporary"]
    """Type of the Image"""

    rapid_deploy: Optional[bool] = None
    """Indicates that rapid deploy of the Image is available"""


class Iso(BaseModel):
    id: int
    """ID of the Resource"""

    architecture: Optional[Literal["arm", "x86"]]
    """Type of cpu architecture this iso is compatible with.

    Null indicates no restriction on the architecture (wildcard).
    """

    deprecated: Optional[str]
    """ISO 8601 timestamp of deprecation, null if ISO is still available.

    After the deprecation time it will no longer be possible to attach the ISO to
    Servers.
    """

    description: str
    """Description of the ISO"""

    name: Optional[str]
    """Unique identifier of the ISO. Only set for public ISOs"""

    type: Literal["private", "public"]
    """Type of the ISO"""


class PrivateNet(BaseModel):
    alias_ips: Optional[List[str]] = None

    ip: Optional[str] = None

    mac_address: Optional[str] = None

    network: Optional[int] = None
    """ID of the Network"""


class Protection(BaseModel):
    delete: bool
    """If true, prevents the Server from being deleted"""

    rebuild: bool
    """If true, prevents the Server from being rebuilt"""


class ServerTypePrice(BaseModel):
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


class ServerType(BaseModel):
    id: int
    """ID of the Server type"""

    cores: int
    """Number of cpu cores a Server of this type will have"""

    cpu_type: Literal["dedicated", "shared"]
    """Type of cpu"""

    deprecated: Optional[bool]
    """True if Server type is deprecated"""

    description: str
    """Description of the Server type"""

    disk: float
    """Disk size a Server of this type will have in GB"""

    memory: float
    """Memory a Server of this type will have in GB"""

    name: str
    """Unique identifier of the Server type"""

    prices: List[ServerTypePrice]
    """Prices in different Locations"""

    storage_type: Literal["local", "network"]
    """Type of Server boot drive.

    Local has higher speed. Network has better availability.
    """


class PlacementGroup(BaseModel):
    id: int
    """ID of the Resource"""

    created: str
    """Point in time when the Resource was created (in ISO-8601 format)"""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    name: str
    """Name of the Resource. Must be unique per Project."""

    servers: List[int]
    """Array of IDs of Servers that are part of this Placement Group"""

    type: Literal["spread"]
    """Type of the Placement Group"""


class Server(BaseModel):
    id: int
    """ID of the Resource"""

    backup_window: Optional[str]
    """
    Time window (UTC) in which the backup will run, or null if the backups are not
    enabled
    """

    created: str
    """Point in time when the Resource was created (in ISO-8601 format)"""

    datacenter: Datacenter
    """
    Datacenter this Primary IP is located at | Datacenter this Resource is located
    at
    """

    image: Optional[Image]

    included_traffic: Optional[int]
    """Free Traffic for the current billing period in bytes"""

    ingoing_traffic: Optional[int]
    """Inbound Traffic for the current billing period in bytes"""

    iso: Optional[Iso]
    """ISO Image that is attached to this Server. Null if no ISO is attached."""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    locked: bool
    """True if Server has been locked and is not available to user"""

    name: str
    """
    Name of the Server (must be unique per Project and a valid hostname as per
    RFC 1123)
    """

    outgoing_traffic: Optional[int]
    """Outbound Traffic for the current billing period in bytes"""

    primary_disk_size: int
    """Size of the primary Disk"""

    private_net: List[PrivateNet]
    """Private networks information"""

    protection: Protection
    """Protection configuration for the Server"""

    public_net: ServerPublicNet
    """Public network information.

    The Server's IPv4 address can be found in `public_net->ipv4->ip`
    """

    rescue_enabled: bool
    """True if rescue mode is enabled.

    Server will then boot into rescue system on next reboot
    """

    server_type: ServerType
    """Type of Server - determines how much ram, disk and cpu a Server has"""

    status: Literal[
        "deleting", "initializing", "migrating", "off", "rebuilding", "running", "starting", "stopping", "unknown"
    ]
    """Status of the Server"""

    load_balancers: Optional[List[int]] = None

    placement_group: Optional[PlacementGroup] = None

    volumes: Optional[List[int]] = None
    """IDs of Volumes assigned to this Server"""
