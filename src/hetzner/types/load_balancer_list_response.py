# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .shared import ResponseMeta
from .._models import BaseModel
from .load_balancer import LoadBalancer

__all__ = ["LoadBalancerListResponse"]


class LoadBalancerListResponse(BaseModel):
    load_balancers: List[LoadBalancer]

    meta: Optional[ResponseMeta] = None
    """Metadata contained in the response"""
