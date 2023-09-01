# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel
from .placement_group import PlacementGroup

__all__ = ["PlacementGroupUpdateResponse"]


class PlacementGroupUpdateResponse(BaseModel):
    placement_group: PlacementGroup
