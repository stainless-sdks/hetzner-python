# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .shared import ResponseMeta
from .._models import BaseModel
from .server_type import ServerType

__all__ = ["ServerTypeListResponse"]


class ServerTypeListResponse(BaseModel):
    server_types: List[ServerType]

    meta: Optional[ResponseMeta] = None
    """Metadata contained in the response"""
