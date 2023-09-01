# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Action", "Error", "Resource"]


class Error(BaseModel):
    code: str
    """Fixed machine readable code"""

    message: str
    """Humanized error message"""


class Resource(BaseModel):
    id: int
    """ID of the Resource | ID of resource referenced"""

    type: str
    """Type of resource referenced"""


class Action(BaseModel):
    id: int
    """ID of the Action"""

    command: str
    """Command executed in the Action"""

    error: Optional[Error]
    """Error message for the Action if error occurred, otherwise null"""

    finished: Optional[str]
    """Point in time when the Action was finished (in ISO-8601 format).

    Only set if the Action is finished otherwise null.
    """

    progress: float
    """Progress of Action in percent"""

    resources: List[Resource]
    """Resources the Action relates to"""

    started: str
    """Point in time when the Action was started (in ISO-8601 format)"""

    status: Literal["error", "running", "success"]
    """Status of the Action"""
