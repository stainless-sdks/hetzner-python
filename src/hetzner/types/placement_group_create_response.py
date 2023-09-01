# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .placement_group import PlacementGroup

__all__ = ["PlacementGroupCreateResponse", "Action", "ActionError", "ActionResource"]


class ActionError(BaseModel):
    code: str
    """Fixed machine readable code"""

    message: str
    """Humanized error message"""


class ActionResource(BaseModel):
    id: int
    """ID of the Resource | ID of resource referenced"""

    type: str
    """Type of resource referenced"""


class Action(BaseModel):
    id: int
    """ID of the Action"""

    command: str
    """Command executed in the Action"""

    error: Optional[ActionError]
    """Error message for the Action if error occurred, otherwise null"""

    finished: Optional[str]
    """Point in time when the Action was finished (in ISO-8601 format).

    Only set if the Action is finished otherwise null.
    """

    progress: float
    """Progress of Action in percent"""

    resources: List[ActionResource]
    """Resources the Action relates to"""

    started: str
    """Point in time when the Action was started (in ISO-8601 format)"""

    status: Literal["error", "running", "success"]
    """Status of the Action"""


class PlacementGroupCreateResponse(BaseModel):
    placement_group: PlacementGroup

    action: Optional[Action] = None
    """Actions show the results and progress of asynchronous requests to the API."""
