# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .shared import ResponseMeta
from .._models import BaseModel
from .primary_ip import PrimaryIP

__all__ = ["PrimaryIPListResponse"]


class PrimaryIPListResponse(BaseModel):
    primary_ips: List[PrimaryIP]

    meta: Optional[ResponseMeta] = None
    """Metadata contained in the response"""
