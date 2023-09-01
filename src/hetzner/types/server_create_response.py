# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .server import Server
from .shared import Action
from .._models import BaseModel

__all__ = ["ServerCreateResponse"]


class ServerCreateResponse(BaseModel):
    action: Action
    """Actions show the results and progress of asynchronous requests to the API."""

    next_actions: List[Action]

    root_password: Optional[str]
    """Root password when no SSH keys have been specified"""

    server: Server
    """Servers are virtual machines that can be provisioned."""
