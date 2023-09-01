# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .shared import Action
from .._models import BaseModel
from .floating_ip import FloatingIp

__all__ = ["FloatingIpCreateResponse"]


class FloatingIpCreateResponse(BaseModel):
    floating_ip: FloatingIp

    action: Optional[Action] = None
    """Actions show the results and progress of asynchronous requests to the API."""
