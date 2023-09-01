# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .price import Price
from .._models import BaseModel

__all__ = ["LoadBalancerTypeRetrieveResponse", "LoadBalancerType", "LoadBalancerTypePrice"]


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


class LoadBalancerTypeRetrieveResponse(BaseModel):
    load_balancer_type: Optional[LoadBalancerType] = None
