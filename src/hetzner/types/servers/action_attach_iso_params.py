# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionAttachIsoParams"]


class ActionAttachIsoParams(TypedDict, total=False):
    iso: Required[str]
    """ID or name of ISO to attach to the Server as listed in GET `/isos`"""
