# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ActionChangeDNSPtrParams"]


class ActionChangeDNSPtrParams(TypedDict, total=False):
    dns_ptr: Required[Optional[str]]
    """Hostname to set as a reverse DNS PTR entry"""

    ip: Required[str]
    """Public IP address for which the reverse DNS entry should be set"""
