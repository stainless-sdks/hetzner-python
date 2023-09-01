# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel
from .floating_ip import FloatingIp

__all__ = ["FloatingIpRetrieveResponse"]


class FloatingIpRetrieveResponse(BaseModel):
    floating_ip: FloatingIp
