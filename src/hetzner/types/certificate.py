# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Certificate", "UsedBy", "Status", "StatusError"]


class UsedBy(BaseModel):
    id: int
    """ID of the Resource | ID of resource referenced"""

    type: str
    """Type of resource referenced"""


class StatusError(BaseModel):
    code: Optional[str] = None

    message: Optional[str] = None


class Status(BaseModel):
    error: Optional[StatusError] = None
    """
    If issuance or renewal reports `failed`, this property contains information
    about what happened
    """

    issuance: Optional[Literal["completed", "failed", "pending"]] = None
    """Status of the issuance process of the Certificate"""

    renewal: Optional[Literal["failed", "pending", "scheduled", "unavailable"]] = None
    """Status of the renewal process of the Certificate."""


class Certificate(BaseModel):
    id: int
    """ID of the Resource"""

    certificate: Optional[str]
    """
    Certificate and chain in PEM format, in order so that each record directly
    certifies the one preceding
    """

    created: str
    """Point in time when the Resource was created (in ISO-8601 format)"""

    domain_names: List[str]
    """Domains and subdomains covered by the Certificate"""

    fingerprint: Optional[str]
    """SHA256 fingerprint of the Certificate"""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    name: str
    """Name of the Resource. Must be unique per Project."""

    not_valid_after: Optional[str]
    """Point in time when the Certificate stops being valid (in ISO-8601 format)"""

    not_valid_before: Optional[str]
    """Point in time when the Certificate becomes valid (in ISO-8601 format)"""

    used_by: List[UsedBy]
    """Resources currently using the Certificate"""

    status: Optional[Status] = None
    """
    Current status of a type `managed` Certificate, always _null_ for type
    `uploaded` Certificates
    """

    type: Optional[Literal["managed", "uploaded"]] = None
    """Type of the Certificate"""
