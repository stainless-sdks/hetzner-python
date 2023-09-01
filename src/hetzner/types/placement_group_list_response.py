# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .shared import ResponseMeta
from .._models import BaseModel
from .placement_group import PlacementGroup

__all__ = ["PlacementGroupListResponse"]


class PlacementGroupListResponse(BaseModel):
    placement_groups: List[PlacementGroup]

    meta: Optional[ResponseMeta] = None
    """Metadata contained in the response"""
