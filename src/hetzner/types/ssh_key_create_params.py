# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["SshKeyCreateParams"]


class SshKeyCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the SSH key"""

    public_key: Required[str]
    """Public key"""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""
