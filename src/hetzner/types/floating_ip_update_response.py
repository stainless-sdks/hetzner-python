# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel
from .floating_ip import FloatingIp

__all__ = ["FloatingIpUpdateResponse"]


class FloatingIpUpdateResponse(BaseModel):
    floating_ip: FloatingIp
