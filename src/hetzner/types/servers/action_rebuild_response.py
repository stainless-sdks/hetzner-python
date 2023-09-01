# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..shared import Action
from ..._models import BaseModel

__all__ = ["ActionRebuildResponse"]


class ActionRebuildResponse(BaseModel):
    action: Optional[Action] = None
    """Actions show the results and progress of asynchronous requests to the API."""

    root_password: Optional[str] = None
    """New root password when not using SSH keys"""
