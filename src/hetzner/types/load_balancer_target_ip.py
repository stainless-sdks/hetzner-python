# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel

__all__ = ["LoadBalancerTargetIp"]


class LoadBalancerTargetIp(BaseModel):
    ip: str
    """
    IP of a server that belongs to the same customer (public IPv4/IPv6) or private
    IP in a Subnetwork type vswitch.
    """
