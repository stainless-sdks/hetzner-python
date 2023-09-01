# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MetricListParams"]


class MetricListParams(TypedDict, total=False):
    end: Required[str]
    """End of period to get Metrics for (in ISO-8601 format)"""

    start: Required[str]
    """Start of period to get Metrics for (in ISO-8601 format)"""

    type: Required[Literal["cpu", "disk", "network"]]
    """Type of metrics to get"""

    step: str
    """Resolution of results in seconds"""
