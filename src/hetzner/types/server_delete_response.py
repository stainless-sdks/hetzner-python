# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .shared import Action
from .._models import BaseModel

__all__ = ["ServerDeleteResponse"]


class ServerDeleteResponse(BaseModel):
    action: Optional[Action] = None
    """Actions show the results and progress of asynchronous requests to the API."""
