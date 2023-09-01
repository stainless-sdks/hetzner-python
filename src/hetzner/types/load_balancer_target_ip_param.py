# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LoadBalancerTargetIPParam"]


class LoadBalancerTargetIPParam(TypedDict, total=False):
    ip: Required[str]
    """
    IP of a server that belongs to the same customer (public IPv4/IPv6) or private
    IP in a Subnetwork type vswitch.
    """
