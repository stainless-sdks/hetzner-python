# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["LoadBalancerUpdateParams"]


class LoadBalancerUpdateParams(TypedDict, total=False):
    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    name: str
    """New Load Balancer name"""
