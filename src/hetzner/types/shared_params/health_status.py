# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["HealthStatus"]


class HealthStatus(TypedDict, total=False):
    listen_port: int

    status: Literal["healthy", "unhealthy", "unknown"]
