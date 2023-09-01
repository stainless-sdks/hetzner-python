# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionResizeParams"]


class ActionResizeParams(TypedDict, total=False):
    size: Required[float]
    """New Volume size in GB (must be greater than current size)"""
