# File generated from our OpenAPI spec by Stainless.

from typing import List
from typing_extensions import Literal

from .price import Price
from .._models import BaseModel
from .floating_ip_price_details import FloatingIPPriceDetails

__all__ = [
    "PricingRetrieveResponse",
    "Pricing",
    "PricingFloatingIP",
    "PricingImage",
    "PricingLoadBalancerType",
    "PricingLoadBalancerTypePrice",
    "PricingPrimaryIP",
    "PricingPrimaryIPPrice",
    "PricingServerBackup",
    "PricingServerType",
    "PricingServerTypePrice",
    "PricingTraffic",
    "PricingVolume",
]


class PricingFloatingIP(BaseModel):
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


class PricingImage(BaseModel):
    price_per_gb_month: Price
    """
    Hourly costs for a Resource in this Location | Monthly costs for a Resource in
    this Location | Monthly costs for a Floating IP type in this Location | Hourly
    costs for a Load Balancer type in this network zone | Monthly costs for a Load
    Balancer type in this network zone | Hourly costs for a Primary IP type in this
    Location | Monthly costs for a Primary IP type in this Location | Hourly costs
    for a Server type in this Location | Monthly costs for a Server type in this
    Location
    """


class PricingLoadBalancerTypePrice(BaseModel):
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


class PricingLoadBalancerType(BaseModel):
    id: int
    """ID of the Load Balancer type the price is for"""

    name: str
    """Name of the Load Balancer type the price is for"""

    prices: List[PricingLoadBalancerTypePrice]
    """Load Balancer type costs per Location"""


class PricingPrimaryIPPrice(BaseModel):
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


class PricingPrimaryIP(BaseModel):
    prices: List[PricingPrimaryIPPrice]
    """Primary IP type costs per Location"""

    type: Literal["ipv4", "ipv6"]
    """The type of the IP"""


class PricingServerBackup(BaseModel):
    percentage: str
    """Percentage by how much the base price will increase"""


class PricingServerTypePrice(BaseModel):
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


class PricingServerType(BaseModel):
    id: int
    """ID of the Server type the price is for"""

    name: str
    """Name of the Server type the price is for"""

    prices: List[PricingServerTypePrice]
    """Server type costs per Location"""


class PricingTraffic(BaseModel):
    price_per_tb: Price
    """
    Hourly costs for a Resource in this Location | Monthly costs for a Resource in
    this Location | Monthly costs for a Floating IP type in this Location | Hourly
    costs for a Load Balancer type in this network zone | Monthly costs for a Load
    Balancer type in this network zone | Hourly costs for a Primary IP type in this
    Location | Monthly costs for a Primary IP type in this Location | Hourly costs
    for a Server type in this Location | Monthly costs for a Server type in this
    Location
    """


class PricingVolume(BaseModel):
    price_per_gb_month: Price
    """
    Hourly costs for a Resource in this Location | Monthly costs for a Resource in
    this Location | Monthly costs for a Floating IP type in this Location | Hourly
    costs for a Load Balancer type in this network zone | Monthly costs for a Load
    Balancer type in this network zone | Hourly costs for a Primary IP type in this
    Location | Monthly costs for a Primary IP type in this Location | Hourly costs
    for a Server type in this Location | Monthly costs for a Server type in this
    Location
    """


class Pricing(BaseModel):
    currency: str
    """Currency the returned prices are expressed in, coded according to ISO 4217"""

    floating_ip: PricingFloatingIP
    """The cost of one Floating IP per month"""

    floating_ips: List[FloatingIPPriceDetails]
    """Costs of Floating IPs types per Location and type"""

    image: PricingImage
    """The cost of Image per GB/month"""

    load_balancer_types: List[PricingLoadBalancerType]
    """Costs of Load Balancer types per Location and type"""

    primary_ips: List[PricingPrimaryIP]
    """Costs of Primary IPs types per Location"""

    server_backup: PricingServerBackup
    """Will increase base Server costs by specific percentage"""

    server_types: List[PricingServerType]
    """Costs of Server types per Location and type"""

    traffic: PricingTraffic
    """The cost of additional traffic per TB"""

    vat_rate: str
    """The VAT rate used for calculating prices with VAT"""

    volume: PricingVolume
    """The cost of Volume per GB/month"""


class PricingRetrieveResponse(BaseModel):
    pricing: Pricing
