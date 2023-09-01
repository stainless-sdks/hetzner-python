# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionDeleteServiceParams"]


class ActionDeleteServiceParams(TypedDict, total=False):
    listen_port: Required[int]
    """The listen port of the service you want to delete"""
