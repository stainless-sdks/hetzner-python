# File generated from our OpenAPI spec by Stainless.

from .shared import Action
from .._models import BaseModel
from .load_balancer import LoadBalancer

__all__ = ["LoadBalancerCreateResponse"]


class LoadBalancerCreateResponse(BaseModel):
    action: Action
    """Actions show the results and progress of asynchronous requests to the API."""

    load_balancer: LoadBalancer
