# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel
from .floating_ip import FloatingIP

__all__ = ["FloatingIPRetrieveResponse"]


class FloatingIPRetrieveResponse(BaseModel):
    floating_ip: FloatingIP
