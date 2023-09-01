# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, TypedDict

from .rule_param import RuleParam

__all__ = ["FirewallCreateParams", "ApplyTo", "ApplyToLabelSelector", "ApplyToServer"]


class FirewallCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the Firewall"""

    apply_to: List[ApplyTo]
    """Resources the Firewall should be applied to after creation"""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    rules: List[RuleParam]
    """Array of rules"""


class ApplyToLabelSelector(TypedDict, total=False):
    selector: Required[str]
    """Label selector"""


class ApplyToServer(TypedDict, total=False):
    id: Required[int]
    """ID of the Resource | ID of the Server"""


class ApplyTo(TypedDict, total=False):
    type: Required[Literal["label_selector", "server"]]
    """Type of the resource"""

    label_selector: ApplyToLabelSelector
    """Configuration for type LabelSelector, required if type is `label_selector`"""

    server: ApplyToServer
    """ID of the Resource"""
