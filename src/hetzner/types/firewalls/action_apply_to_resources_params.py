# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionApplyToResourcesParams", "ApplyTo", "ApplyToLabelSelector", "ApplyToServer"]


class ActionApplyToResourcesParams(TypedDict, total=False):
    apply_to: Required[List[ApplyTo]]
    """Resources the Firewall should be applied to"""


class ApplyToLabelSelector(TypedDict, total=False):
    selector: Required[str]
    """Label selector"""


class ApplyToServer(TypedDict, total=False):
    id: Required[int]
    """ID of the Resource | ID of the Server"""


class ApplyTo(TypedDict, total=False):
    label_selector: ApplyToLabelSelector
    """Configuration for type LabelSelector, required if type is `label_selector`"""

    server: ApplyToServer
    """ID of the Resource"""

    type: Literal["label_selector", "server"]
    """Type of the resource"""
