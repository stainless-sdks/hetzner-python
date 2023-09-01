# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel
from .primary_ip import PrimaryIp

__all__ = ["PrimaryIpUpdateResponse"]


class PrimaryIpUpdateResponse(BaseModel):
    primary_ip: PrimaryIp
