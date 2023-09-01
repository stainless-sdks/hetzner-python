# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from ...types import shared_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.networks import (
    ActionListResponse,
    ActionAddRouteResponse,
    ActionRetrieveResponse,
    ActionAddSubnetResponse,
    ActionDeleteRouteResponse,
    ActionDeleteSubnetResponse,
    ActionChangeIPRangeResponse,
    ActionChangeProtectionResponse,
    action_list_params,
    action_add_route_params,
    action_add_subnet_params,
    action_delete_route_params,
    action_delete_subnet_params,
    action_change_ip_range_params,
    action_change_protection_params,
)

__all__ = ["Actions", "AsyncActions"]


class Actions(SyncAPIResource):
    def retrieve(
        self,
        action_id: int,
        *,
        id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionRetrieveResponse:
        """
        Returns a specific Action for a Network.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/networks/{id}/actions/{action_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRetrieveResponse,
        )

    def list(
        self,
        id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: shared_params.SortParam | NotGiven = NOT_GIVEN,
        status: shared_params.StatusParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionListResponse:
        """Returns all Action objects for a Network.

        You can sort the results by using the
        `sort` URI parameter, and filter them with the `status` parameter.

        Args:
          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          sort: Can be used multiple times.

          status: Can be used multiple times, the response will contain only Actions with
              specified statuses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/networks/{id}/actions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "status": status,
                    },
                    action_list_params.ActionListParams,
                ),
            ),
            cast_to=ActionListResponse,
        )

    def add_route(
        self,
        id: int,
        *,
        destination: str,
        gateway: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionAddRouteResponse:
        """
        Adds a route entry to a Network.

        Note: if the Network object changes during the request, the response will be a
        “conflict” error.

        Args:
          destination: Destination network or host of this route. Must not overlap with an existing
              ip_range in any subnets or with any destinations in other routes or with the
              first IP of the networks ip_range or with 172.31.1.1. Must be one of the private
              IPv4 ranges of RFC1918.

          gateway: Gateway for the route. Cannot be the first IP of the networks ip_range and also
              cannot be 172.31.1.1 as this IP is being used as a gateway for the public
              network interface of Servers. | Gateway for the route. Cannot be the first IP of
              the networks ip_range, an IP behind a vSwitch or 172.31.1.1, as this IP is being
              used as a gateway for the public network interface of Servers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/networks/{id}/actions/add_route",
            body=maybe_transform(
                {
                    "destination": destination,
                    "gateway": gateway,
                },
                action_add_route_params.ActionAddRouteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAddRouteResponse,
        )

    def add_subnet(
        self,
        id: int,
        *,
        network_zone: str,
        type: Literal["cloud", "server", "vswitch"],
        ip_range: str | NotGiven = NOT_GIVEN,
        vswitch_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionAddSubnetResponse:
        """Adds a new subnet object to the Network.

        If you do not specify an `ip_range` for
        the subnet we will automatically pick the first available /24 range for you if
        possible.

        Note: if the parent Network object changes during the request, the response will
        be a “conflict” error.

        Args:
          network_zone: Name of Network zone. The Location object contains the `network_zone` property
              each Location belongs to.

          type: Type of Subnetwork

          ip_range: Range to allocate IPs from. Must be a Subnet of the ip_range of the parent
              network object and must not overlap with any other subnets or with any
              destinations in routes. Minimum Network size is /30. We suggest that you pick a
              bigger Network with a /24 netmask. | Range to allocate IPs from. Must be a
              Subnet of the ip_range of the parent network object and must not overlap with
              any other subnets or with any destinations in routes. If the Subnet is of type
              vSwitch, it also can not overlap with any gateway in routes. Minimum Network
              size is /30. We suggest that you pick a bigger Network with a /24 netmask.

          vswitch_id: ID of the robot vSwitch. Must be supplied if the subnet is of type vswitch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/networks/{id}/actions/add_subnet",
            body=maybe_transform(
                {
                    "network_zone": network_zone,
                    "type": type,
                    "ip_range": ip_range,
                    "vswitch_id": vswitch_id,
                },
                action_add_subnet_params.ActionAddSubnetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAddSubnetResponse,
        )

    def change_ip_range(
        self,
        id: int,
        *,
        ip_range: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionChangeIPRangeResponse:
        """Changes the IP range of a Network.

        IP ranges can only be extended and never
        shrunk. You can only add IPs at the end of an existing IP range. This means that
        the IP part of your existing range must stay the same and you can only change
        its netmask.

        For example if you have a range `10.0.0.0/16` you want to extend then your new
        range must also start with the IP `10.0.0.0`. Your CIDR netmask `/16` may change
        to a number that is smaller than `16` thereby increasing the IP range. So valid
        entries would be `10.0.0.0/15`, `10.0.0.0/14`, `10.0.0.0/13` and so on.

        After changing the IP range you will have to adjust the routes on your connected
        Servers by either rebooting them or manually changing the routes to your private
        Network interface.

        Note: if the Network object changes during the request, the response will be a
        “conflict” error.

        Args:
          ip_range: The new prefix for the whole Network

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/networks/{id}/actions/change_ip_range",
            body=maybe_transform({"ip_range": ip_range}, action_change_ip_range_params.ActionChangeIPRangeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeIPRangeResponse,
        )

    def change_protection(
        self,
        id: int,
        *,
        delete: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionChangeProtectionResponse:
        """
        Changes the protection configuration of a Network.

        Note: if the Network object changes during the request, the response will be a
        “conflict” error.

        Args:
          delete: If true, prevents the Network from being deleted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/networks/{id}/actions/change_protection",
            body=maybe_transform({"delete": delete}, action_change_protection_params.ActionChangeProtectionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeProtectionResponse,
        )

    def delete_route(
        self,
        id: int,
        *,
        destination: str,
        gateway: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionDeleteRouteResponse:
        """
        Delete a route entry from a Network.

        Note: if the Network object changes during the request, the response will be a
        “conflict” error.

        Args:
          destination: Destination network or host of this route. Must not overlap with an existing
              ip_range in any subnets or with any destinations in other routes or with the
              first IP of the networks ip_range or with 172.31.1.1. Must be one of the private
              IPv4 ranges of RFC1918.

          gateway: Gateway for the route. Cannot be the first IP of the networks ip_range and also
              cannot be 172.31.1.1 as this IP is being used as a gateway for the public
              network interface of Servers. | Gateway for the route. Cannot be the first IP of
              the networks ip_range, an IP behind a vSwitch or 172.31.1.1, as this IP is being
              used as a gateway for the public network interface of Servers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/networks/{id}/actions/delete_route",
            body=maybe_transform(
                {
                    "destination": destination,
                    "gateway": gateway,
                },
                action_delete_route_params.ActionDeleteRouteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDeleteRouteResponse,
        )

    def delete_subnet(
        self,
        id: int,
        *,
        ip_range: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionDeleteSubnetResponse:
        """Deletes a single subnet entry from a Network.

        You cannot delete subnets which
        still have Servers attached. If you have Servers attached you first need to
        detach all Servers that use IPs from this subnet before you can delete the
        subnet.

        Note: if the Network object changes during the request, the response will be a
        “conflict” error.

        Args:
          ip_range: IP range of subnet to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/networks/{id}/actions/delete_subnet",
            body=maybe_transform({"ip_range": ip_range}, action_delete_subnet_params.ActionDeleteSubnetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDeleteSubnetResponse,
        )


class AsyncActions(AsyncAPIResource):
    async def retrieve(
        self,
        action_id: int,
        *,
        id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionRetrieveResponse:
        """
        Returns a specific Action for a Network.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/networks/{id}/actions/{action_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRetrieveResponse,
        )

    async def list(
        self,
        id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: shared_params.SortParam | NotGiven = NOT_GIVEN,
        status: shared_params.StatusParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionListResponse:
        """Returns all Action objects for a Network.

        You can sort the results by using the
        `sort` URI parameter, and filter them with the `status` parameter.

        Args:
          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          sort: Can be used multiple times.

          status: Can be used multiple times, the response will contain only Actions with
              specified statuses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/networks/{id}/actions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "status": status,
                    },
                    action_list_params.ActionListParams,
                ),
            ),
            cast_to=ActionListResponse,
        )

    async def add_route(
        self,
        id: int,
        *,
        destination: str,
        gateway: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionAddRouteResponse:
        """
        Adds a route entry to a Network.

        Note: if the Network object changes during the request, the response will be a
        “conflict” error.

        Args:
          destination: Destination network or host of this route. Must not overlap with an existing
              ip_range in any subnets or with any destinations in other routes or with the
              first IP of the networks ip_range or with 172.31.1.1. Must be one of the private
              IPv4 ranges of RFC1918.

          gateway: Gateway for the route. Cannot be the first IP of the networks ip_range and also
              cannot be 172.31.1.1 as this IP is being used as a gateway for the public
              network interface of Servers. | Gateway for the route. Cannot be the first IP of
              the networks ip_range, an IP behind a vSwitch or 172.31.1.1, as this IP is being
              used as a gateway for the public network interface of Servers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/networks/{id}/actions/add_route",
            body=maybe_transform(
                {
                    "destination": destination,
                    "gateway": gateway,
                },
                action_add_route_params.ActionAddRouteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAddRouteResponse,
        )

    async def add_subnet(
        self,
        id: int,
        *,
        network_zone: str,
        type: Literal["cloud", "server", "vswitch"],
        ip_range: str | NotGiven = NOT_GIVEN,
        vswitch_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionAddSubnetResponse:
        """Adds a new subnet object to the Network.

        If you do not specify an `ip_range` for
        the subnet we will automatically pick the first available /24 range for you if
        possible.

        Note: if the parent Network object changes during the request, the response will
        be a “conflict” error.

        Args:
          network_zone: Name of Network zone. The Location object contains the `network_zone` property
              each Location belongs to.

          type: Type of Subnetwork

          ip_range: Range to allocate IPs from. Must be a Subnet of the ip_range of the parent
              network object and must not overlap with any other subnets or with any
              destinations in routes. Minimum Network size is /30. We suggest that you pick a
              bigger Network with a /24 netmask. | Range to allocate IPs from. Must be a
              Subnet of the ip_range of the parent network object and must not overlap with
              any other subnets or with any destinations in routes. If the Subnet is of type
              vSwitch, it also can not overlap with any gateway in routes. Minimum Network
              size is /30. We suggest that you pick a bigger Network with a /24 netmask.

          vswitch_id: ID of the robot vSwitch. Must be supplied if the subnet is of type vswitch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/networks/{id}/actions/add_subnet",
            body=maybe_transform(
                {
                    "network_zone": network_zone,
                    "type": type,
                    "ip_range": ip_range,
                    "vswitch_id": vswitch_id,
                },
                action_add_subnet_params.ActionAddSubnetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAddSubnetResponse,
        )

    async def change_ip_range(
        self,
        id: int,
        *,
        ip_range: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionChangeIPRangeResponse:
        """Changes the IP range of a Network.

        IP ranges can only be extended and never
        shrunk. You can only add IPs at the end of an existing IP range. This means that
        the IP part of your existing range must stay the same and you can only change
        its netmask.

        For example if you have a range `10.0.0.0/16` you want to extend then your new
        range must also start with the IP `10.0.0.0`. Your CIDR netmask `/16` may change
        to a number that is smaller than `16` thereby increasing the IP range. So valid
        entries would be `10.0.0.0/15`, `10.0.0.0/14`, `10.0.0.0/13` and so on.

        After changing the IP range you will have to adjust the routes on your connected
        Servers by either rebooting them or manually changing the routes to your private
        Network interface.

        Note: if the Network object changes during the request, the response will be a
        “conflict” error.

        Args:
          ip_range: The new prefix for the whole Network

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/networks/{id}/actions/change_ip_range",
            body=maybe_transform({"ip_range": ip_range}, action_change_ip_range_params.ActionChangeIPRangeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeIPRangeResponse,
        )

    async def change_protection(
        self,
        id: int,
        *,
        delete: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionChangeProtectionResponse:
        """
        Changes the protection configuration of a Network.

        Note: if the Network object changes during the request, the response will be a
        “conflict” error.

        Args:
          delete: If true, prevents the Network from being deleted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/networks/{id}/actions/change_protection",
            body=maybe_transform({"delete": delete}, action_change_protection_params.ActionChangeProtectionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeProtectionResponse,
        )

    async def delete_route(
        self,
        id: int,
        *,
        destination: str,
        gateway: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionDeleteRouteResponse:
        """
        Delete a route entry from a Network.

        Note: if the Network object changes during the request, the response will be a
        “conflict” error.

        Args:
          destination: Destination network or host of this route. Must not overlap with an existing
              ip_range in any subnets or with any destinations in other routes or with the
              first IP of the networks ip_range or with 172.31.1.1. Must be one of the private
              IPv4 ranges of RFC1918.

          gateway: Gateway for the route. Cannot be the first IP of the networks ip_range and also
              cannot be 172.31.1.1 as this IP is being used as a gateway for the public
              network interface of Servers. | Gateway for the route. Cannot be the first IP of
              the networks ip_range, an IP behind a vSwitch or 172.31.1.1, as this IP is being
              used as a gateway for the public network interface of Servers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/networks/{id}/actions/delete_route",
            body=maybe_transform(
                {
                    "destination": destination,
                    "gateway": gateway,
                },
                action_delete_route_params.ActionDeleteRouteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDeleteRouteResponse,
        )

    async def delete_subnet(
        self,
        id: int,
        *,
        ip_range: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionDeleteSubnetResponse:
        """Deletes a single subnet entry from a Network.

        You cannot delete subnets which
        still have Servers attached. If you have Servers attached you first need to
        detach all Servers that use IPs from this subnet before you can delete the
        subnet.

        Note: if the Network object changes during the request, the response will be a
        “conflict” error.

        Args:
          ip_range: IP range of subnet to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/networks/{id}/actions/delete_subnet",
            body=maybe_transform({"ip_range": ip_range}, action_delete_subnet_params.ActionDeleteSubnetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDeleteSubnetResponse,
        )
