# File generated from our OpenAPI spec by Stainless.

from ..shared import Action
from ..._models import BaseModel

__all__ = ["ActionChangeDnsPtrResponse"]


class ActionChangeDnsPtrResponse(BaseModel):
    action: Action
    """Actions show the results and progress of asynchronous requests to the API."""
