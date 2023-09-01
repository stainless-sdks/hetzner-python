# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..shared import Action, ResponseMeta
from ..._models import BaseModel

__all__ = ["ActionApplyToResourcesResponse"]


class ActionApplyToResourcesResponse(BaseModel):
    actions: List[Action]

    meta: Optional[ResponseMeta] = None
    """Metadata contained in the response"""
