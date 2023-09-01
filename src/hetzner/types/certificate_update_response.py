# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel
from .certificate import Certificate

__all__ = ["CertificateUpdateResponse"]


class CertificateUpdateResponse(BaseModel):
    certificate: Certificate
    """
    TLS/SSL Certificates prove the identity of a Server and are used to encrypt
    client traffic.
    """
