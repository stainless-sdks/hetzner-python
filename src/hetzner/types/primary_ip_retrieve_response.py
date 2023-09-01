# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel
from .primary_ip import PrimaryIp

__all__ = ["PrimaryIpRetrieveResponse"]


class PrimaryIpRetrieveResponse(BaseModel):
    primary_ip: PrimaryIp
