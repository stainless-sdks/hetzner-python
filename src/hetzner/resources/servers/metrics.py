# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.servers import MetricListResponse, metric_list_params

__all__ = ["Metrics", "AsyncMetrics"]


class Metrics(SyncAPIResource):
    def list(
        self,
        id: int,
        *,
        end: str,
        start: str,
        type: Literal["cpu", "disk", "network"],
        step: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> MetricListResponse:
        """
        Get Metrics for specified Server.

        You must specify the type of metric to get: cpu, disk or network. You can also
        specify more than one type by comma separation, e.g. cpu,disk.

        Depending on the type you will get different time series data

        | Type    | Timeseries              | Unit      | Description                                          |
        | ------- | ----------------------- | --------- | ---------------------------------------------------- |
        | cpu     | cpu                     | percent   | Percent CPU usage                                    |
        | disk    | disk.0.iops.read        | iop/s     | Number of read IO operations per second              |
        |         | disk.0.iops.write       | iop/s     | Number of write IO operations per second             |
        |         | disk.0.bandwidth.read   | bytes/s   | Bytes read per second                                |
        |         | disk.0.bandwidth.write  | bytes/s   | Bytes written per second                             |
        | network | network.0.pps.in        | packets/s | Public Network interface packets per second received |
        |         | network.0.pps.out       | packets/s | Public Network interface packets per second sent     |
        |         | network.0.bandwidth.in  | bytes/s   | Public Network interface bytes/s received            |
        |         | network.0.bandwidth.out | bytes/s   | Public Network interface bytes/s sent                |

        Metrics are available for the last 30 days only.

        If you do not provide the step argument we will automatically adjust it so that
        a maximum of 200 samples are returned.

        We limit the number of samples returned to a maximum of 500 and will adjust the
        step parameter accordingly.

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
            f"/servers/{id}/metrics",
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
        type: Literal["cpu", "disk", "network"],
        step: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> MetricListResponse:
        """
        Get Metrics for specified Server.

        You must specify the type of metric to get: cpu, disk or network. You can also
        specify more than one type by comma separation, e.g. cpu,disk.

        Depending on the type you will get different time series data

        | Type    | Timeseries              | Unit      | Description                                          |
        | ------- | ----------------------- | --------- | ---------------------------------------------------- |
        | cpu     | cpu                     | percent   | Percent CPU usage                                    |
        | disk    | disk.0.iops.read        | iop/s     | Number of read IO operations per second              |
        |         | disk.0.iops.write       | iop/s     | Number of write IO operations per second             |
        |         | disk.0.bandwidth.read   | bytes/s   | Bytes read per second                                |
        |         | disk.0.bandwidth.write  | bytes/s   | Bytes written per second                             |
        | network | network.0.pps.in        | packets/s | Public Network interface packets per second received |
        |         | network.0.pps.out       | packets/s | Public Network interface packets per second sent     |
        |         | network.0.bandwidth.in  | bytes/s   | Public Network interface bytes/s received            |
        |         | network.0.bandwidth.out | bytes/s   | Public Network interface bytes/s sent                |

        Metrics are available for the last 30 days only.

        If you do not provide the step argument we will automatically adjust it so that
        a maximum of 200 samples are returned.

        We limit the number of samples returned to a maximum of 500 and will adjust the
        step parameter accordingly.

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
            f"/servers/{id}/metrics",
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
