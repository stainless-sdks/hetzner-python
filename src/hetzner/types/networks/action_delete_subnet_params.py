# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionDeleteSubnetParams"]


class ActionDeleteSubnetParams(TypedDict, total=False):
    ip_range: Required[str]
    """IP range of subnet to delete"""
