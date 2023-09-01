# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionAssignParams"]


class ActionAssignParams(TypedDict, total=False):
    assignee_id: Required[int]
    """ID of a resource of type `assignee_type`"""

    assignee_type: Required[Literal["server"]]
    """Type of resource assigning the Primary IP to"""
