# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionDetachFromNetworkParams"]


class ActionDetachFromNetworkParams(TypedDict, total=False):
    network: Required[int]
    """ID of an existing network to detach the Load Balancer from"""
