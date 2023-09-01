# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.load_balancers import MetricListResponse, metric_list_params

__all__ = ["Metrics", "AsyncMetrics"]


class Metrics(SyncAPIResource):
    def list(
        self,
        id: int,
        *,
        end: str,
        start: str,
        type: Literal["open_connections", "connections_per_second", "requests_per_second", "bandwidth"],
        step: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> MetricListResponse:
        """
        You must specify the type of metric to get: `open_connections`,
        `connections_per_second`, `requests_per_second` or `bandwidth`. You can also
        specify more than one type by comma separation, e.g.
        `requests_per_second,bandwidth`.

        Depending on the type you will get different time series data:

        | Type                   | Timeseries             | Unit          | Description            |
        | ---------------------- | ---------------------- | ------------- | ---------------------- |
        | open_connections       | open_connections       | number        | Open connections       |
        | connections_per_second | connections_per_second | connections/s | Connections per second |
        | requests_per_second    | requests_per_second    | requests/s    | Requests per second    |
        | bandwidth              | bandwidth.in           | bytes/s       | Ingress bandwidth      |
        |                        | bandwidth.out          | bytes/s       | Egress bandwidth       |

        Metrics are available for the last 30 days only.

        If you do not provide the step argument we will automatically adjust it so that
        200 samples are returned.

        We limit the number of samples to a maximum of 500 and will adjust the step
        parameter accordingly.

        Args:
          end: End of period to get Metrics for (in ISO-8601 format)

          start: Start of period to get Metrics for (in ISO-8601 format)

          type: Type of metrics to get

          step: Resolution of results in seconds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/load_balancers/{id}/metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "type": type,
                        "step": step,
                    },
                    metric_list_params.MetricListParams,
                ),
            ),
            cast_to=MetricListResponse,
        )


class AsyncMetrics(AsyncAPIResource):
    async def list(
        self,
        id: int,
        *,
        end: str,
        start: str,
        type: Literal["open_connections", "connections_per_second", "requests_per_second", "bandwidth"],
        step: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> MetricListResponse:
        """
        You must specify the type of metric to get: `open_connections`,
        `connections_per_second`, `requests_per_second` or `bandwidth`. You can also
        specify more than one type by comma separation, e.g.
        `requests_per_second,bandwidth`.

        Depending on the type you will get different time series data:

        | Type                   | Timeseries             | Unit          | Description            |
        | ---------------------- | ---------------------- | ------------- | ---------------------- |
        | open_connections       | open_connections       | number        | Open connections       |
        | connections_per_second | connections_per_second | connections/s | Connections per second |
        | requests_per_second    | requests_per_second    | requests/s    | Requests per second    |
        | bandwidth              | bandwidth.in           | bytes/s       | Ingress bandwidth      |
        |                        | bandwidth.out          | bytes/s       | Egress bandwidth       |

        Metrics are available for the last 30 days only.

        If you do not provide the step argument we will automatically adjust it so that
        200 samples are returned.

        We limit the number of samples to a maximum of 500 and will adjust the step
        parameter accordingly.

        Args:
          end: End of period to get Metrics for (in ISO-8601 format)

          start: Start of period to get Metrics for (in ISO-8601 format)

          type: Type of metrics to get

          step: Resolution of results in seconds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/load_balancers/{id}/metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "type": type,
                        "step": step,
                    },
                    metric_list_params.MetricListParams,
                ),
            ),
            cast_to=MetricListResponse,
        )
