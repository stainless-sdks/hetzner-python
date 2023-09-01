# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionChangeTypeParams"]


class ActionChangeTypeParams(TypedDict, total=False):
    load_balancer_type: Required[str]
    """ID or name of Load Balancer type the Load Balancer should migrate to"""
