# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .shared import ResponseMeta
from .._models import BaseModel
from .certificate import Certificate

__all__ = ["CertificateListResponse"]


class CertificateListResponse(BaseModel):
    certificates: List[Certificate]

    meta: Optional[ResponseMeta] = None
    """Metadata contained in the response"""
