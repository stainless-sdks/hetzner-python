# File generated from our OpenAPI spec by Stainless.

from typing import List

from .shared import ResponseMeta
from .._models import BaseModel

__all__ = ["DatacenterListResponse", "Datacenter", "DatacenterLocation", "DatacenterServerTypes"]


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


class DatacenterListResponse(BaseModel):
    datacenters: List[Datacenter]

    meta: ResponseMeta
    """Metadata contained in the response"""

    recommendation: int
    """The Datacenter which is recommended to be used to create new Servers."""
