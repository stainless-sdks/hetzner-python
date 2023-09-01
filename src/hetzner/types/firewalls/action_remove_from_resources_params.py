# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionRemoveFromResourcesParams", "RemoveFrom", "RemoveFromLabelSelector", "RemoveFromServer"]


class ActionRemoveFromResourcesParams(TypedDict, total=False):
    remove_from: Required[List[RemoveFrom]]
    """Resources the Firewall should be removed from"""


class RemoveFromLabelSelector(TypedDict, total=False):
    selector: Required[str]
    """Label selector"""


class RemoveFromServer(TypedDict, total=False):
    id: Required[int]
    """ID of the Resource | ID of the Server"""


class RemoveFrom(TypedDict, total=False):
    label_selector: RemoveFromLabelSelector
    """Configuration for type LabelSelector, required if type is `label_selector`"""

    server: RemoveFromServer
    """ID of the Resource"""

    type: Literal["label_selector", "server"]
    """Type of the resource"""
