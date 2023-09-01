# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..shared import Action
from ..._models import BaseModel

__all__ = ["ActionEnableRescueResponse"]


class ActionEnableRescueResponse(BaseModel):
    action: Optional[Action] = None
    """Actions show the results and progress of asynchronous requests to the API."""

    root_password: Optional[str] = None
    """Password that will be set for this Server once the Action succeeds"""
