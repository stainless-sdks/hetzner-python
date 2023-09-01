# File generated from our OpenAPI spec by Stainless.

from typing import List

from .shared import ResponseMeta
from .._models import BaseModel

__all__ = ["LocationListResponse", "Location"]


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


class LocationListResponse(BaseModel):
    locations: List[Location]

    meta: ResponseMeta
    """Metadata contained in the response"""
