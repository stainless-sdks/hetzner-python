# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ...types import shared_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.primary_ips import (
    ActionListResponse,
    ActionAssignResponse,
    ActionRetrieveResponse,
    ActionUnassignResponse,
    ActionChangeDnsPtrResponse,
    ActionChangeProtectionResponse,
    action_list_params,
    action_assign_params,
    action_change_dns_ptr_params,
    action_change_protection_params,
)

__all__ = ["Actions", "AsyncActions"]


class Actions(SyncAPIResource):
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
    ) -> ActionRetrieveResponse:
        """
        Returns a specific Action object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/primary_ips/actions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRetrieveResponse,
        )

    def list(
        self,
        *,
        id: int | NotGiven = NOT_GIVEN,
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
        """Returns all Action objects.

        You can `sort` the results by using the sort URI
        parameter, and filter them with the `status` and `id` parameter.

        Args:
          id: Can be used multiple times, the response will contain only Actions with
              specified IDs

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
            "/primary_ips/actions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
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

    def assign(
        self,
        id: int,
        *,
        assignee_id: int,
        assignee_type: Literal["server"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionAssignResponse:
        """
        Assigns a Primary IP to a Server.

        A Server can only have one Primary IP of type `ipv4` and one of type `ipv6`
        assigned. If you need more IPs use Floating IPs.

        The Server must be powered off (status `off`) in order for this operation to
        succeed.

        #### Call specific error codes

        | Code                          | Description                                          |
        | ----------------------------- | ---------------------------------------------------- |
        | `server_not_stopped`          | The server is running, but needs to be powered off   |
        | `primary_ip_already_assigned` | Primary ip is already assigned to a different server |
        | `server_has_ipv4`             | The server already has an ipv4 address               |
        | `server_has_ipv6`             | The server already has an ipv6 address               |

        Args:
          assignee_id: ID of a resource of type `assignee_type`

          assignee_type: Type of resource assigning the Primary IP to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/primary_ips/{id}/actions/assign",
            body=maybe_transform(
                {
                    "assignee_id": assignee_id,
                    "assignee_type": assignee_type,
                },
                action_assign_params.ActionAssignParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAssignResponse,
        )

    def change_dns_ptr(
        self,
        id: int,
        *,
        dns_ptr: Optional[str],
        ip: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionChangeDnsPtrResponse:
        """
        Changes the hostname that will appear when getting the hostname belonging to
        this Primary IP.

        Args:
          dns_ptr: Hostname to set as a reverse DNS PTR entry, will reset to original default value
              if `null`

          ip: IP address for which to set the reverse DNS entry

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/primary_ips/{id}/actions/change_dns_ptr",
            body=maybe_transform(
                {
                    "dns_ptr": dns_ptr,
                    "ip": ip,
                },
                action_change_dns_ptr_params.ActionChangeDnsPtrParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeDnsPtrResponse,
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
        Changes the protection configuration of a Primary IP.

        A Primary IP can only be delete protected if its `auto_delete` property is set
        to `false`.

        Args:
          delete: If true, prevents the Primary IP from being deleted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/primary_ips/{id}/actions/change_protection",
            body=maybe_transform({"delete": delete}, action_change_protection_params.ActionChangeProtectionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeProtectionResponse,
        )

    def unassign(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionUnassignResponse:
        """
        Unassigns a Primary IP from a Server.

        The Server must be powered off (status `off`) in order for this operation to
        succeed.

        Note that only Servers that have at least one network interface (public or
        private) attached can be powered on.

        #### Call specific error codes

        | Code                             | Description                                        |
        | -------------------------------- | -------------------------------------------------- |
        | `server_not_stopped`             | The server is running, but needs to be powered off |
        | `server_is_load_balancer_target` | The server ipv4 address is a loadbalancer target   |

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/primary_ips/{id}/actions/unassign",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionUnassignResponse,
        )


class AsyncActions(AsyncAPIResource):
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
    ) -> ActionRetrieveResponse:
        """
        Returns a specific Action object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/primary_ips/actions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRetrieveResponse,
        )

    async def list(
        self,
        *,
        id: int | NotGiven = NOT_GIVEN,
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
        """Returns all Action objects.

        You can `sort` the results by using the sort URI
        parameter, and filter them with the `status` and `id` parameter.

        Args:
          id: Can be used multiple times, the response will contain only Actions with
              specified IDs

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
            "/primary_ips/actions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
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

    async def assign(
        self,
        id: int,
        *,
        assignee_id: int,
        assignee_type: Literal["server"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionAssignResponse:
        """
        Assigns a Primary IP to a Server.

        A Server can only have one Primary IP of type `ipv4` and one of type `ipv6`
        assigned. If you need more IPs use Floating IPs.

        The Server must be powered off (status `off`) in order for this operation to
        succeed.

        #### Call specific error codes

        | Code                          | Description                                          |
        | ----------------------------- | ---------------------------------------------------- |
        | `server_not_stopped`          | The server is running, but needs to be powered off   |
        | `primary_ip_already_assigned` | Primary ip is already assigned to a different server |
        | `server_has_ipv4`             | The server already has an ipv4 address               |
        | `server_has_ipv6`             | The server already has an ipv6 address               |

        Args:
          assignee_id: ID of a resource of type `assignee_type`

          assignee_type: Type of resource assigning the Primary IP to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/primary_ips/{id}/actions/assign",
            body=maybe_transform(
                {
                    "assignee_id": assignee_id,
                    "assignee_type": assignee_type,
                },
                action_assign_params.ActionAssignParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAssignResponse,
        )

    async def change_dns_ptr(
        self,
        id: int,
        *,
        dns_ptr: Optional[str],
        ip: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionChangeDnsPtrResponse:
        """
        Changes the hostname that will appear when getting the hostname belonging to
        this Primary IP.

        Args:
          dns_ptr: Hostname to set as a reverse DNS PTR entry, will reset to original default value
              if `null`

          ip: IP address for which to set the reverse DNS entry

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/primary_ips/{id}/actions/change_dns_ptr",
            body=maybe_transform(
                {
                    "dns_ptr": dns_ptr,
                    "ip": ip,
                },
                action_change_dns_ptr_params.ActionChangeDnsPtrParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeDnsPtrResponse,
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
        Changes the protection configuration of a Primary IP.

        A Primary IP can only be delete protected if its `auto_delete` property is set
        to `false`.

        Args:
          delete: If true, prevents the Primary IP from being deleted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/primary_ips/{id}/actions/change_protection",
            body=maybe_transform({"delete": delete}, action_change_protection_params.ActionChangeProtectionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeProtectionResponse,
        )

    async def unassign(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionUnassignResponse:
        """
        Unassigns a Primary IP from a Server.

        The Server must be powered off (status `off`) in order for this operation to
        succeed.

        Note that only Servers that have at least one network interface (public or
        private) attached can be powered on.

        #### Call specific error codes

        | Code                             | Description                                        |
        | -------------------------------- | -------------------------------------------------- |
        | `server_not_stopped`             | The server is running, but needs to be powered off |
        | `server_is_load_balancer_target` | The server ipv4 address is a loadbalancer target   |

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/primary_ips/{id}/actions/unassign",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionUnassignResponse,
        )
