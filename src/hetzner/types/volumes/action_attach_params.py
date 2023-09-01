# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionAttachParams"]


class ActionAttachParams(TypedDict, total=False):
    server: Required[int]
    """ID of the Server the Volume will be attached to"""

    automount: bool
    """Auto-mount the Volume after attaching it"""
