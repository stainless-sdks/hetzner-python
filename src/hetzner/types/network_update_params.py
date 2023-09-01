# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["NetworkUpdateParams"]


class NetworkUpdateParams(TypedDict, total=False):
    expose_routes_to_vswitch: bool
    """
    Indicates if the routes from this network should be exposed to the vSwitch
    connection. The exposing only takes effect if a vSwitch connection is active.

    Currently the default route 0.0.0.0/0 is not exposed to the vSwitch connection.
    We are aware of the issue and are working on a solution.
    """

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    name: str
    """New network name"""
