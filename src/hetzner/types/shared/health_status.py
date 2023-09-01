# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["HealthStatus"]


class HealthStatus(BaseModel):
    listen_port: Optional[int] = None

    status: Optional[Literal["healthy", "unhealthy", "unknown"]] = None
