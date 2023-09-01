# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict
from typing_extensions import Literal

from ...types import (
    PrimaryIpListResponse,
    PrimaryIpCreateResponse,
    PrimaryIpUpdateResponse,
    PrimaryIpRetrieveResponse,
    primary_ip_list_params,
    primary_ip_create_params,
    primary_ip_update_params,
)
from .actions import Actions, AsyncActions
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Hetzner, AsyncHetzner

__all__ = ["PrimaryIps", "AsyncPrimaryIps"]


class PrimaryIps(SyncAPIResource):
    actions: Actions

    def __init__(self, client: Hetzner) -> None:
        super().__init__(client)
        self.actions = Actions(client)

    def create(
        self,
        *,
        assignee_type: Literal["server"],
        name: str,
        type: Literal["ipv4", "ipv6"],
        assignee_id: int | NotGiven = NOT_GIVEN,
        auto_delete: bool | NotGiven = NOT_GIVEN,
        datacenter: str | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> PrimaryIpCreateResponse:
        """
        Creates a new Primary IP, optionally assigned to a Server.

        If you want to create a Primary IP that is not assigned to a Server, you need to
        provide the `datacenter` key instead of `assignee_id`. This can be either the ID
        or the name of the Datacenter this Primary IP shall be created in.

        Note that a Primary IP can only be assigned to a Server in the same Datacenter
        later on.

        #### Call specific error codes

        | Code                 | Description                                                  |
        | -------------------- | ------------------------------------------------------------ |
        | `server_not_stopped` | The specified server is running, but needs to be powered off |
        | `server_has_ipv4`    | The server already has an ipv4 address                       |
        | `server_has_ipv6`    | The server already has an ipv6 address                       |

        Args:
          assignee_type: Resource type the Primary IP can be assigned to

          type: The type of the IP

          assignee_id: ID of the resource the Primary IP should be assigned to. Omitted if it should
              not be assigned.

          auto_delete: Delete the Primary IP when the Server it is assigned to is deleted. If omitted
              defaults to `false`.

          datacenter: ID or name of Datacenter the Primary IP will be bound to. Needs to be omitted if
              `assignee_id` is passed.

          labels: User-defined labels (key-value pairs)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/primary_ips",
            body=maybe_transform(
                {
                    "assignee_type": assignee_type,
                    "name": name,
                    "type": type,
                    "assignee_id": assignee_id,
                    "auto_delete": auto_delete,
                    "datacenter": datacenter,
                    "labels": labels,
                },
                primary_ip_create_params.PrimaryIpCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrimaryIpCreateResponse,
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
    ) -> PrimaryIpRetrieveResponse:
        """
        Returns a specific Primary IP object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/primary_ips/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrimaryIpRetrieveResponse,
        )

    def update(
        self,
        id: int,
        *,
        auto_delete: bool | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> PrimaryIpUpdateResponse:
        """
        Updates the Primary IP.

        Note that when updating labels, the Primary IP's current set of labels will be
        replaced with the labels provided in the request body. So, for example, if you
        want to add a new label, you have to provide all existing labels plus the new
        label in the request body.

        If the Primary IP object changes during the request, the response will be a
        “conflict” error.

        Args:
          auto_delete: Delete this Primary IP when the resource it is assigned to is deleted

          labels: User-defined labels (key-value pairs)

          name: New unique name to set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/primary_ips/{id}",
            body=maybe_transform(
                {
                    "auto_delete": auto_delete,
                    "labels": labels,
                    "name": name,
                },
                primary_ip_update_params.PrimaryIpUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrimaryIpUpdateResponse,
        )

    def list(
        self,
        *,
        ip: str | NotGiven = NOT_GIVEN,
        label_selector: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["id", "id:asc", "id:desc", "created", "created:asc", "created:desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> PrimaryIpListResponse:
        """
        Returns all Primary IP objects.

        Args:
          ip: Can be used to filter resources by their ip. The response will only contain the
              resources matching the specified ip.

          label_selector: Can be used to filter resources by labels. The response will only contain
              resources matching the label selector.

          name: Can be used to filter resources by their name. The response will only contain
              the resources matching the specified name

          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          sort: Can be used multiple times. Choices id id:asc id:desc created created:asc
              created:desc

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/primary_ips",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ip": ip,
                        "label_selector": label_selector,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    primary_ip_list_params.PrimaryIpListParams,
                ),
            ),
            cast_to=PrimaryIpListResponse,
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
        """Deletes a Primary IP.

        The Primary IP may be assigned to a Server.

        In this case it is unassigned
        automatically. The Server must be powered off (status `off`) in order for this
        operation to succeed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/primary_ips/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPrimaryIps(AsyncAPIResource):
    actions: AsyncActions

    def __init__(self, client: AsyncHetzner) -> None:
        super().__init__(client)
        self.actions = AsyncActions(client)

    async def create(
        self,
        *,
        assignee_type: Literal["server"],
        name: str,
        type: Literal["ipv4", "ipv6"],
        assignee_id: int | NotGiven = NOT_GIVEN,
        auto_delete: bool | NotGiven = NOT_GIVEN,
        datacenter: str | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> PrimaryIpCreateResponse:
        """
        Creates a new Primary IP, optionally assigned to a Server.

        If you want to create a Primary IP that is not assigned to a Server, you need to
        provide the `datacenter` key instead of `assignee_id`. This can be either the ID
        or the name of the Datacenter this Primary IP shall be created in.

        Note that a Primary IP can only be assigned to a Server in the same Datacenter
        later on.

        #### Call specific error codes

        | Code                 | Description                                                  |
        | -------------------- | ------------------------------------------------------------ |
        | `server_not_stopped` | The specified server is running, but needs to be powered off |
        | `server_has_ipv4`    | The server already has an ipv4 address                       |
        | `server_has_ipv6`    | The server already has an ipv6 address                       |

        Args:
          assignee_type: Resource type the Primary IP can be assigned to

          type: The type of the IP

          assignee_id: ID of the resource the Primary IP should be assigned to. Omitted if it should
              not be assigned.

          auto_delete: Delete the Primary IP when the Server it is assigned to is deleted. If omitted
              defaults to `false`.

          datacenter: ID or name of Datacenter the Primary IP will be bound to. Needs to be omitted if
              `assignee_id` is passed.

          labels: User-defined labels (key-value pairs)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/primary_ips",
            body=maybe_transform(
                {
                    "assignee_type": assignee_type,
                    "name": name,
                    "type": type,
                    "assignee_id": assignee_id,
                    "auto_delete": auto_delete,
                    "datacenter": datacenter,
                    "labels": labels,
                },
                primary_ip_create_params.PrimaryIpCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrimaryIpCreateResponse,
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
    ) -> PrimaryIpRetrieveResponse:
        """
        Returns a specific Primary IP object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/primary_ips/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrimaryIpRetrieveResponse,
        )

    async def update(
        self,
        id: int,
        *,
        auto_delete: bool | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> PrimaryIpUpdateResponse:
        """
        Updates the Primary IP.

        Note that when updating labels, the Primary IP's current set of labels will be
        replaced with the labels provided in the request body. So, for example, if you
        want to add a new label, you have to provide all existing labels plus the new
        label in the request body.

        If the Primary IP object changes during the request, the response will be a
        “conflict” error.

        Args:
          auto_delete: Delete this Primary IP when the resource it is assigned to is deleted

          labels: User-defined labels (key-value pairs)

          name: New unique name to set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/primary_ips/{id}",
            body=maybe_transform(
                {
                    "auto_delete": auto_delete,
                    "labels": labels,
                    "name": name,
                },
                primary_ip_update_params.PrimaryIpUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrimaryIpUpdateResponse,
        )

    async def list(
        self,
        *,
        ip: str | NotGiven = NOT_GIVEN,
        label_selector: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["id", "id:asc", "id:desc", "created", "created:asc", "created:desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> PrimaryIpListResponse:
        """
        Returns all Primary IP objects.

        Args:
          ip: Can be used to filter resources by their ip. The response will only contain the
              resources matching the specified ip.

          label_selector: Can be used to filter resources by labels. The response will only contain
              resources matching the label selector.

          name: Can be used to filter resources by their name. The response will only contain
              the resources matching the specified name

          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          sort: Can be used multiple times. Choices id id:asc id:desc created created:asc
              created:desc

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/primary_ips",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ip": ip,
                        "label_selector": label_selector,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    primary_ip_list_params.PrimaryIpListParams,
                ),
            ),
            cast_to=PrimaryIpListResponse,
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
        """Deletes a Primary IP.

        The Primary IP may be assigned to a Server.

        In this case it is unassigned
        automatically. The Server must be powered off (status `off`) in order for this
        operation to succeed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/primary_ips/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )
