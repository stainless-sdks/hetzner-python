# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionChangeAlgorithmParams"]


class ActionChangeAlgorithmParams(TypedDict, total=False):
    type: Required[Literal["least_connections", "round_robin"]]
    """Type of the algorithm | Algorithm of the Load Balancer"""
