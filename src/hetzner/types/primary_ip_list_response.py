# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .shared import ResponseMeta
from .._models import BaseModel
from .primary_ip import PrimaryIp

__all__ = ["PrimaryIpListResponse"]


class PrimaryIpListResponse(BaseModel):
    primary_ips: List[PrimaryIp]

    meta: Optional[ResponseMeta] = None
    """Metadata contained in the response"""
