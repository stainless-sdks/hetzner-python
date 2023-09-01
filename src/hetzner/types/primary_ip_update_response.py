# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel
from .primary_ip import PrimaryIP

__all__ = ["PrimaryIPUpdateResponse"]


class PrimaryIPUpdateResponse(BaseModel):
    primary_ip: PrimaryIP
