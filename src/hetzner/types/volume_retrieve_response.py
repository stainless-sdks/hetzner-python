# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VolumeRetrieveResponse", "Volume", "VolumeLocation", "VolumeProtection"]


class VolumeLocation(BaseModel):
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


class VolumeProtection(BaseModel):
    delete: bool
    """
    If true, prevents the Resource from being deleted | If true, prevents the
    Network from being deleted
    """


class Volume(BaseModel):
    id: int
    """ID of the Resource"""

    created: str
    """Point in time when the Resource was created (in ISO-8601 format)"""

    format: Optional[str]
    """
    Filesystem of the Volume if formatted on creation, null if not formatted on
    creation
    """

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    linux_device: str
    """Device path on the file system for the Volume"""

    location: VolumeLocation
    """Location the Floating IP was created in.

    Routing is optimized for this Location. | Location of the Volume. Volume can
    only be attached to Servers in the same Location.
    """

    name: str
    """Name of the Resource. Must be unique per Project."""

    protection: VolumeProtection
    """Protection configuration for the Resource"""

    server: Optional[int]
    """ID of the Server the Volume is attached to, null if it is not attached at all"""

    size: float
    """Size in GB of the Volume"""

    status: Literal["available", "creating"]
    """Current status of the Volume"""


class VolumeRetrieveResponse(BaseModel):
    volume: Volume
    """
    A Volume is a highly-available, scalable, and SSD-based block storage for
    Servers. Pricing for Volumes depends on the Volume size and Location, not the
    actual used storage. Please see
    [Hetzner Wiki](https://wiki.hetzner.de/index.php/CloudServer/en#Volumes) for
    more details about Volumes.
    """
