# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CertificateCreateParams"]


class CertificateCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the Certificate"""

    certificate: str
    """
    Certificate and chain in PEM format, in order so that each record directly
    certifies the one preceding. Required for type `uploaded` Certificates.
    """

    domain_names: List[str]
    """
    Domains and subdomains that should be contained in the Certificate issued by
    _Let's Encrypt_. Required for type `managed` Certificates.
    """

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    private_key: str
    """Certificate key in PEM format. Required for type `uploaded` Certificates."""

    type: Literal["managed", "uploaded"]
    """
    Choose between uploading a Certificate in PEM format or requesting a managed
    _Let's Encrypt_ Certificate. If omitted defaults to `uploaded`.
    """
