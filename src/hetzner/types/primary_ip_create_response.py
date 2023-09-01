# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .shared import Action
from .._models import BaseModel
from .primary_ip import PrimaryIP

__all__ = ["PrimaryIPCreateResponse"]


class PrimaryIPCreateResponse(BaseModel):
    primary_ip: PrimaryIP

    action: Optional[Action] = None
    """Actions show the results and progress of asynchronous requests to the API."""
