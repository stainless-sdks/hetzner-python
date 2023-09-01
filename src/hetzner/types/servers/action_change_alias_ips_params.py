# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ActionChangeAliasIpsParams"]


class ActionChangeAliasIpsParams(TypedDict, total=False):
    alias_ips: Required[List[str]]
    """New alias IPs to set for this Server"""

    network: Required[int]
    """ID of an existing Network already attached to the Server"""
