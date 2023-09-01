# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel
from .placement_group import PlacementGroup

__all__ = ["PlacementGroupRetrieveResponse"]


class PlacementGroupRetrieveResponse(BaseModel):
    placement_group: PlacementGroup
