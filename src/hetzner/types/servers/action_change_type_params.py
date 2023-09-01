# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionChangeTypeParams"]


class ActionChangeTypeParams(TypedDict, total=False):
    server_type: Required[str]
    """ID or name of Server type the Server should migrate to"""

    upgrade_disk: Required[bool]
    """
    If false, do not upgrade the disk (this allows downgrading the Server type
    later)
    """
