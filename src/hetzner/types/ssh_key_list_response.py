# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional

from .shared import ResponseMeta
from .._models import BaseModel

__all__ = ["SshKeyListResponse", "SshKey"]


class SshKey(BaseModel):
    id: int
    """ID of the Resource"""

    created: str
    """Point in time when the Resource was created (in ISO-8601 format)"""

    fingerprint: str
    """Fingerprint of public key"""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    name: str
    """Name of the Resource. Must be unique per Project."""

    public_key: str
    """Public key"""


class SshKeyListResponse(BaseModel):
    ssh_keys: List[SshKey]

    meta: Optional[ResponseMeta] = None
    """Metadata contained in the response"""
