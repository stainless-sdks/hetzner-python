# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List

from ...types import (
    NetworkListResponse,
    NetworkCreateResponse,
    NetworkUpdateResponse,
    NetworkRetrieveResponse,
    network_list_params,
    network_create_params,
    network_update_params,
)
from .actions import Actions, AsyncActions
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Hetzner, AsyncHetzner

__all__ = ["Networks", "AsyncNetworks"]


class Networks(SyncAPIResource):
    actions: Actions

    def __init__(self, client: Hetzner) -> None:
        super().__init__(client)
        self.actions = Actions(client)

    def create(
        self,
        *,
        ip_range: str,
        name: str,
        expose_routes_to_vswitch: bool | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        routes: List[network_create_params.Route] | NotGiven = NOT_GIVEN,
        subnets: List[network_create_params.Subnet] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> NetworkCreateResponse:
        """
        Creates a network with the specified `ip_range`.

        You may specify one or more `subnets`. You can also add more Subnets later by
        using the
        [add subnet action](https://docs.hetzner.cloud/#network-actions-add-a-subnet-to-a-network).
        If you do not specify an `ip_range` in the subnet we will automatically pick the
        first available /24 range for you.

        You may specify one or more routes in `routes`. You can also add more routes
        later by using the
        [add route action](https://docs.hetzner.cloud/#network-actions-add-a-route-to-a-network).

        Args:
          ip_range: IP range of the whole network which must span all included subnets. Must be one
              of the private IPv4 ranges of RFC1918. Minimum network size is /24. We highly
              recommend that you pick a larger network with a /16 netmask.

          name: Name of the network

          expose_routes_to_vswitch: Indicates if the routes from this network should be exposed to the vSwitch
              connection. The exposing only takes effect if a vSwitch connection is active.

              Currently the default route 0.0.0.0/0 is not exposed to the vSwitch connection.
              We are aware of the issue and are working on a solution.

          labels: User-defined labels (key-value pairs)

          routes: Array of routes set in this network. The destination of the route must be one of
              the private IPv4 ranges of RFC1918. The gateway must be a subnet/IP of the
              ip_range of the network object. The destination must not overlap with an
              existing ip_range in any subnets or with any destinations in other routes or
              with the first IP of the networks ip_range or with 172.31.1.1. The gateway
              cannot be the first IP of the networks ip_range and also cannot be 172.31.1.1.

          subnets: Array of subnets allocated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/networks",
            body=maybe_transform(
                {
                    "ip_range": ip_range,
                    "name": name,
                    "expose_routes_to_vswitch": expose_routes_to_vswitch,
                    "labels": labels,
                    "routes": routes,
                    "subnets": subnets,
                },
                network_create_params.NetworkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkCreateResponse,
        )

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
    ) -> NetworkRetrieveResponse:
        """
        Gets a specific network object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/networks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkRetrieveResponse,
        )

    def update(
        self,
        id: int,
        *,
        expose_routes_to_vswitch: bool | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> NetworkUpdateResponse:
        """
        Updates the network properties.

        Note that when updating labels, the network’s current set of labels will be
        replaced with the labels provided in the request body. So, for example, if you
        want to add a new label, you have to provide all existing labels plus the new
        label in the request body.

        Note: if the network object changes during the request, the response will be a
        “conflict” error.

        Args:
          expose_routes_to_vswitch: Indicates if the routes from this network should be exposed to the vSwitch
              connection. The exposing only takes effect if a vSwitch connection is active.

              Currently the default route 0.0.0.0/0 is not exposed to the vSwitch connection.
              We are aware of the issue and are working on a solution.

          labels: User-defined labels (key-value pairs)

          name: New network name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/networks/{id}",
            body=maybe_transform(
                {
                    "expose_routes_to_vswitch": expose_routes_to_vswitch,
                    "labels": labels,
                    "name": name,
                },
                network_update_params.NetworkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkUpdateResponse,
        )

    def list(
        self,
        *,
        label_selector: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> NetworkListResponse:
        """
        Gets all existing networks that you have available.

        Args:
          label_selector: Can be used to filter networks by labels. The response will only contain
              networks with a matching label selector pattern.

          name: Can be used to filter networks by their name. The response will only contain the
              networks matching the specified name.

          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/networks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "label_selector": label_selector,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    network_list_params.NetworkListParams,
                ),
            ),
            cast_to=NetworkListResponse,
        )

    def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes a network.

        If there are Servers attached they will be detached in the
        background.

        Note: if the network object changes during the request, the response will be a
        “conflict” error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/networks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncNetworks(AsyncAPIResource):
    actions: AsyncActions

    def __init__(self, client: AsyncHetzner) -> None:
        super().__init__(client)
        self.actions = AsyncActions(client)

    async def create(
        self,
        *,
        ip_range: str,
        name: str,
        expose_routes_to_vswitch: bool | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        routes: List[network_create_params.Route] | NotGiven = NOT_GIVEN,
        subnets: List[network_create_params.Subnet] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> NetworkCreateResponse:
        """
        Creates a network with the specified `ip_range`.

        You may specify one or more `subnets`. You can also add more Subnets later by
        using the
        [add subnet action](https://docs.hetzner.cloud/#network-actions-add-a-subnet-to-a-network).
        If you do not specify an `ip_range` in the subnet we will automatically pick the
        first available /24 range for you.

        You may specify one or more routes in `routes`. You can also add more routes
        later by using the
        [add route action](https://docs.hetzner.cloud/#network-actions-add-a-route-to-a-network).

        Args:
          ip_range: IP range of the whole network which must span all included subnets. Must be one
              of the private IPv4 ranges of RFC1918. Minimum network size is /24. We highly
              recommend that you pick a larger network with a /16 netmask.

          name: Name of the network

          expose_routes_to_vswitch: Indicates if the routes from this network should be exposed to the vSwitch
              connection. The exposing only takes effect if a vSwitch connection is active.

              Currently the default route 0.0.0.0/0 is not exposed to the vSwitch connection.
              We are aware of the issue and are working on a solution.

          labels: User-defined labels (key-value pairs)

          routes: Array of routes set in this network. The destination of the route must be one of
              the private IPv4 ranges of RFC1918. The gateway must be a subnet/IP of the
              ip_range of the network object. The destination must not overlap with an
              existing ip_range in any subnets or with any destinations in other routes or
              with the first IP of the networks ip_range or with 172.31.1.1. The gateway
              cannot be the first IP of the networks ip_range and also cannot be 172.31.1.1.

          subnets: Array of subnets allocated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/networks",
            body=maybe_transform(
                {
                    "ip_range": ip_range,
                    "name": name,
                    "expose_routes_to_vswitch": expose_routes_to_vswitch,
                    "labels": labels,
                    "routes": routes,
                    "subnets": subnets,
                },
                network_create_params.NetworkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkCreateResponse,
        )

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
    ) -> NetworkRetrieveResponse:
        """
        Gets a specific network object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/networks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkRetrieveResponse,
        )

    async def update(
        self,
        id: int,
        *,
        expose_routes_to_vswitch: bool | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> NetworkUpdateResponse:
        """
        Updates the network properties.

        Note that when updating labels, the network’s current set of labels will be
        replaced with the labels provided in the request body. So, for example, if you
        want to add a new label, you have to provide all existing labels plus the new
        label in the request body.

        Note: if the network object changes during the request, the response will be a
        “conflict” error.

        Args:
          expose_routes_to_vswitch: Indicates if the routes from this network should be exposed to the vSwitch
              connection. The exposing only takes effect if a vSwitch connection is active.

              Currently the default route 0.0.0.0/0 is not exposed to the vSwitch connection.
              We are aware of the issue and are working on a solution.

          labels: User-defined labels (key-value pairs)

          name: New network name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/networks/{id}",
            body=maybe_transform(
                {
                    "expose_routes_to_vswitch": expose_routes_to_vswitch,
                    "labels": labels,
                    "name": name,
                },
                network_update_params.NetworkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkUpdateResponse,
        )

    async def list(
        self,
        *,
        label_selector: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> NetworkListResponse:
        """
        Gets all existing networks that you have available.

        Args:
          label_selector: Can be used to filter networks by labels. The response will only contain
              networks with a matching label selector pattern.

          name: Can be used to filter networks by their name. The response will only contain the
              networks matching the specified name.

          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/networks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "label_selector": label_selector,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    network_list_params.NetworkListParams,
                ),
            ),
            cast_to=NetworkListResponse,
        )

    async def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes a network.

        If there are Servers attached they will be detached in the
        background.

        Note: if the network object changes during the request, the response will be a
        “conflict” error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/networks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )
