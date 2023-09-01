# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import PricingRetrieveResponse
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["Pricing", "AsyncPricing"]


class Pricing(SyncAPIResource):
    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> PricingRetrieveResponse:
        """Returns prices for all resources available on the platform.

        VAT and currency of
        the Project owner are used for calculations.

        Both net and gross prices are included in the response.
        """
        return self._get(
            "/pricing",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PricingRetrieveResponse,
        )


class AsyncPricing(AsyncAPIResource):
    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> PricingRetrieveResponse:
        """Returns prices for all resources available on the platform.

        VAT and currency of
        the Project owner are used for calculations.

        Both net and gross prices are included in the response.
        """
        return await self._get(
            "/pricing",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PricingRetrieveResponse,
        )
