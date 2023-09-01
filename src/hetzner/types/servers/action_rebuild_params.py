# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionRebuildParams"]


class ActionRebuildParams(TypedDict, total=False):
    image: Required[str]
    """ID or name of Image to rebuilt from."""
