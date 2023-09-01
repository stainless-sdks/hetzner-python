# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import IsoListResponse, IsoRetrieveResponse, iso_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["Isos", "AsyncIsos"]


class Isos(SyncAPIResource):
    def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> IsoRetrieveResponse:
        """
        Returns a specific ISO object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/isos/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IsoRetrieveResponse,
        )

    def list(
        self,
        *,
        architecture: str | NotGiven = NOT_GIVEN,
        include_architecture_wildcard: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> IsoListResponse:
        """
        Returns all available ISO objects.

        Args:
          architecture: Return only ISOs with the given architecture.

          include_architecture_wildcard: Include Images with wildcard architecture (architecture is null). Works only if
              architecture filter is specified.

          name: Can be used to filter ISOs by their name. The response will only contain the ISO
              matching the specified name.

          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/isos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "architecture": architecture,
                        "include_architecture_wildcard": include_architecture_wildcard,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    iso_list_params.IsoListParams,
                ),
            ),
            cast_to=IsoListResponse,
        )


class AsyncIsos(AsyncAPIResource):
    async def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> IsoRetrieveResponse:
        """
        Returns a specific ISO object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/isos/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IsoRetrieveResponse,
        )

    async def list(
        self,
        *,
        architecture: str | NotGiven = NOT_GIVEN,
        include_architecture_wildcard: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> IsoListResponse:
        """
        Returns all available ISO objects.

        Args:
          architecture: Return only ISOs with the given architecture.

          include_architecture_wildcard: Include Images with wildcard architecture (architecture is null). Works only if
              architecture filter is specified.

          name: Can be used to filter ISOs by their name. The response will only contain the ISO
              matching the specified name.

          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/isos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "architecture": architecture,
                        "include_architecture_wildcard": include_architecture_wildcard,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    iso_list_params.IsoListParams,
                ),
            ),
            cast_to=IsoListResponse,
        )
