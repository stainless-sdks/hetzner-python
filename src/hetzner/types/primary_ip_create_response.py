# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .shared import Action
from .._models import BaseModel
from .primary_ip import PrimaryIp

__all__ = ["PrimaryIpCreateResponse"]


class PrimaryIpCreateResponse(BaseModel):
    primary_ip: PrimaryIp

    action: Optional[Action] = None
    """Actions show the results and progress of asynchronous requests to the API."""
