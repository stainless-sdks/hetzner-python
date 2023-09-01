# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ActionChangeProtectionParams"]


class ActionChangeProtectionParams(TypedDict, total=False):
    delete: bool
    """
    If true, prevents the Server from being deleted (currently delete and rebuild
    attribute needs to have the same value)
    """

    rebuild: bool
    """
    If true, prevents the Server from being rebuilt (currently delete and rebuild
    attribute needs to have the same value)
    """
