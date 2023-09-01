# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .shared import Action
from .._models import BaseModel
from .floating_ip import FloatingIP

__all__ = ["FloatingIPCreateResponse"]


class FloatingIPCreateResponse(BaseModel):
    floating_ip: FloatingIP

    action: Optional[Action] = None
    """Actions show the results and progress of asynchronous requests to the API."""
