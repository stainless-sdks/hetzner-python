# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Union

from ..._models import BaseModel

__all__ = ["MetricListResponse", "Metrics", "MetricsTimeSeries"]


class MetricsTimeSeries(BaseModel):
    values: List[List[Union[float, str]]]
    """Metrics Timestamps with values"""


class Metrics(BaseModel):
    end: str
    """End of period of metrics reported (in ISO-8601 format)"""

    start: str
    """Start of period of metrics reported (in ISO-8601 format)"""

    step: int
    """Resolution of results in seconds."""

    time_series: Dict[str, MetricsTimeSeries]
    """Hash with timeseries information, containing the name of timeseries as key"""


class MetricListResponse(BaseModel):
    metrics: Metrics
    """
    You must specify the type of metric to get: open_connections,
    requests_per_second or bandwidth. You can also specify more than one type by
    comma separation, e.g. requests_per_second,bandwidth. Depending on the type you
    will get different time series data.
    """
