# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ActionChangeProtectionParams"]


class ActionChangeProtectionParams(TypedDict, total=False):
    delete: bool
    """If true, prevents the Volume from being deleted"""
