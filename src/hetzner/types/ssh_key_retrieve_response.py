# File generated from our OpenAPI spec by Stainless.

from typing import Dict

from .._models import BaseModel

__all__ = ["SshKeyRetrieveResponse", "SshKey"]


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


class SshKeyRetrieveResponse(BaseModel):
    ssh_key: SshKey
    """SSH keys are public keys you provide to the cloud system.

    They can be injected into Servers at creation time. We highly recommend that you
    use keys instead of passwords to manage your Servers.
    """
