# File generated from our OpenAPI spec by Stainless.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .price_per_time_monthly import PricePerTimeMonthly

__all__ = ["FloatingIpPriceDetails"]


class FloatingIpPriceDetails(BaseModel):
    prices: List[PricePerTimeMonthly]
    """Floating IP type costs per Location"""

    type: Literal["ipv4", "ipv6"]
    """The type of the IP"""
