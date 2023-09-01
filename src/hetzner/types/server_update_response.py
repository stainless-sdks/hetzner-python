# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .server import Server
from .._models import BaseModel

__all__ = ["ServerUpdateResponse"]


class ServerUpdateResponse(BaseModel):
    server: Optional[Server] = None
    """Servers are virtual machines that can be provisioned."""
