# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["Action", "Error", "Resource"]


class Error(TypedDict, total=False):
    code: Required[str]
    """Fixed machine readable code"""

    message: Required[str]
    """Humanized error message"""


class Resource(TypedDict, total=False):
    id: Required[int]
    """ID of the Resource | ID of resource referenced"""

    type: Required[str]
    """Type of resource referenced"""


class Action(TypedDict, total=False):
    id: Required[int]
    """ID of the Action"""

    command: Required[str]
    """Command executed in the Action"""

    error: Required[Optional[Error]]
    """Error message for the Action if error occurred, otherwise null"""

    finished: Required[Optional[str]]
    """Point in time when the Action was finished (in ISO-8601 format).

    Only set if the Action is finished otherwise null.
    """

    progress: Required[float]
    """Progress of Action in percent"""

    resources: Required[List[Resource]]
    """Resources the Action relates to"""

    started: Required[str]
    """Point in time when the Action was started (in ISO-8601 format)"""

    status: Required[Literal["error", "running", "success"]]
    """Status of the Action"""
