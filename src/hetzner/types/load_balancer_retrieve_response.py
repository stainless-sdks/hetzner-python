# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel
from .load_balancer import LoadBalancer

__all__ = ["LoadBalancerRetrieveResponse"]


class LoadBalancerRetrieveResponse(BaseModel):
    load_balancer: LoadBalancer
