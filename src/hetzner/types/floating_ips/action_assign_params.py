# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionAssignParams"]


class ActionAssignParams(TypedDict, total=False):
    server: Required[int]
    """ID of the Server the Floating IP shall be assigned to"""
