# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from . import price
from .._models import BaseModel
from .cpu_type import CpuType

__all__ = ["ServerType", "Price", "Deprecation"]


class Price(BaseModel):
    location: str
    """Name of the Location the price is for"""

    price_hourly: price.Price
    """
    Hourly costs for a Resource in this Location | Monthly costs for a Resource in
    this Location | Monthly costs for a Floating IP type in this Location | Hourly
    costs for a Load Balancer type in this network zone | Monthly costs for a Load
    Balancer type in this network zone | Hourly costs for a Primary IP type in this
    Location | Monthly costs for a Primary IP type in this Location | Hourly costs
    for a Server type in this Location | Monthly costs for a Server type in this
    Location
    """

    price_monthly: price.Price
    """
    Hourly costs for a Resource in this Location | Monthly costs for a Resource in
    this Location | Monthly costs for a Floating IP type in this Location | Hourly
    costs for a Load Balancer type in this network zone | Monthly costs for a Load
    Balancer type in this network zone | Hourly costs for a Primary IP type in this
    Location | Monthly costs for a Primary IP type in this Location | Hourly costs
    for a Server type in this Location | Monthly costs for a Server type in this
    Location
    """


class Deprecation(BaseModel):
    announced: str
    """Date of when the deprecation was announced."""

    unavailable_after: str
    """
    After the time in this field, the resource will not be available from the
    general listing endpoint of the resource type, and it can not be used in new
    resources. For example, if this is an image, you can not create new servers with
    this image after the mentioned date.
    """


class ServerType(BaseModel):
    id: int
    """ID of the Server type"""

    architecture: Literal["arm", "x86"]
    """Type of cpu architecture this image is compatible with.

    | Type of cpu architecture
    """

    cores: int
    """Number of cpu cores a Server of this type will have"""

    cpu_type: CpuType
    """Type of cpu"""

    deprecated: Optional[bool]
    """This field is deprecated. Use the deprecation object instead"""

    description: str
    """Description of the Server type"""

    disk: float
    """Disk size a Server of this type will have in GB"""

    included_traffic: int
    """Free traffic per month in bytes"""

    memory: float
    """Memory a Server of this type will have in GB"""

    name: str
    """Unique identifier of the Server type"""

    prices: List[Price]
    """Prices in different Locations"""

    storage_type: Literal["local", "network"]
    """Type of Server boot drive.

    Local has higher speed. Network has better availability.
    """

    deprecation: Optional[Deprecation] = None
    """Describes if, when & how the resources was deprecated.

    If this field is set to `null` the resource is not deprecated. If it has a
    value, it is considered deprecated.
    """
