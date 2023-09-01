# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .rule import Rule
from .._models import BaseModel

__all__ = [
    "Firewall",
    "AppliedTo",
    "AppliedToAppliedToResource",
    "AppliedToAppliedToResourceServer",
    "AppliedToLabelSelector",
    "AppliedToServer",
]


class AppliedToAppliedToResourceServer(BaseModel):
    id: int
    """ID of the Resource | ID of the Server"""


class AppliedToAppliedToResource(BaseModel):
    server: Optional[AppliedToAppliedToResourceServer] = None
    """ID of the Resource"""

    type: Optional[Literal["server"]] = None
    """Type of resource referenced"""


class AppliedToLabelSelector(BaseModel):
    selector: str
    """Label selector"""


class AppliedToServer(BaseModel):
    id: int
    """ID of the Resource | ID of the Server"""


class AppliedTo(BaseModel):
    type: Literal["label_selector", "server"]
    """Type of resource referenced"""

    applied_to_resources: Optional[List[AppliedToAppliedToResource]] = None

    label_selector: Optional[AppliedToLabelSelector] = None
    """Configuration for type LabelSelector, required if type is `label_selector`"""

    server: Optional[AppliedToServer] = None
    """ID of the Resource"""


class Firewall(BaseModel):
    id: int
    """ID of the Resource"""

    applied_to: List[AppliedTo]

    created: str
    """Point in time when the Resource was created (in ISO-8601 format)"""

    name: str
    """Name of the Resource. Must be unique per Project."""

    rules: List[Rule]

    labels: Optional[Dict[str, str]] = None
    """User-defined labels (key-value pairs)"""
