# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionChangeIPRangeParams"]


class ActionChangeIPRangeParams(TypedDict, total=False):
    ip_range: Required[str]
    """The new prefix for the whole Network"""
