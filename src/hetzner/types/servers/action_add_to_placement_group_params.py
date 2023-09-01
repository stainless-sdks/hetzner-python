# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionAddToPlacementGroupParams"]


class ActionAddToPlacementGroupParams(TypedDict, total=False):
    placement_group: Required[int]
    """ID of Placement Group the Server should be added to"""
