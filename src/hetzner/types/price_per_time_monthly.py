# File generated from our OpenAPI spec by Stainless.

from .price import Price
from .._models import BaseModel

__all__ = ["PricePerTimeMonthly"]


class PricePerTimeMonthly(BaseModel):
    location: str
    """Name of the Location the price is for"""

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
