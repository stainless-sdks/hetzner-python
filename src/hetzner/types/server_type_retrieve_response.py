# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel
from .server_type import ServerType

__all__ = ["ServerTypeRetrieveResponse"]


class ServerTypeRetrieveResponse(BaseModel):
    server_type: ServerType
