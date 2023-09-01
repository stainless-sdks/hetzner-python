# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .shared import ResponseMeta
from .._models import BaseModel
from .firewall import Firewall

__all__ = ["FirewallListResponse"]


class FirewallListResponse(BaseModel):
    firewalls: List[Firewall]

    meta: Optional[ResponseMeta] = None
    """Metadata contained in the response"""
