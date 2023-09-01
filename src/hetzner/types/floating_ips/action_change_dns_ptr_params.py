# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ActionChangeDNSPtrParams"]


class ActionChangeDNSPtrParams(TypedDict, total=False):
    dns_ptr: Required[Optional[str]]
    """
    Hostname to set as a reverse DNS PTR entry, will reset to original default value
    if `null`
    """

    ip: Required[str]
    """IP address for which to set the reverse DNS entry"""
