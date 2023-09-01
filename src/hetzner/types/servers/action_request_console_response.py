# File generated from our OpenAPI spec by Stainless.

from ..shared import Action
from ..._models import BaseModel

__all__ = ["ActionRequestConsoleResponse"]


class ActionRequestConsoleResponse(BaseModel):
    action: Action
    """Actions show the results and progress of asynchronous requests to the API."""

    password: str
    """
    VNC password to use for this connection (this password only works in combination
    with a wss_url with valid token)
    """

    wss_url: str
    """
    URL of websocket proxy to use; this includes a token which is valid for a
    limited time only
    """
