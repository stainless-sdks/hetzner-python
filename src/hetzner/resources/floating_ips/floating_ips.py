# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict
from typing_extensions import Literal

from ...types import (
    FloatingIp,
    FloatingIpCreateResponse,
    FloatingIpUpdateResponse,
    FloatingIpRetrieveResponse,
    floating_ip_list_params,
    floating_ip_create_params,
    floating_ip_update_params,
)
from .actions import Actions, AsyncActions
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncFloatingIpsPage, AsyncFloatingIpsPage
from ..._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from ..._client import Hetzner, AsyncHetzner

__all__ = ["FloatingIps", "AsyncFloatingIps"]


class FloatingIps(SyncAPIResource):
    actions: Actions

    def __init__(self, client: Hetzner) -> None:
        super().__init__(client)
        self.actions = Actions(client)

    def create(
        self,
        *,
        type: Literal["ipv4", "ipv6"],
        description: str | NotGiven = NOT_GIVEN,
        home_location: str | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        server: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> FloatingIpCreateResponse:
        """Creates a new Floating IP assigned to a Server.

        If you want to create a Floating
        IP that is not bound to a Server, you need to provide the `home_location` key
        instead of `server`. This can be either the ID or the name of the Location this
        IP shall be created in. Note that a Floating IP can be assigned to a Server in
        any Location later on. For optimal routing it is advised to use the Floating IP
        in the same Location it was created in.

        Args:
          type: The type of the IP

          home_location: Home Location (routing is optimized for that Location). Only optional if Server
              argument is passed.

          labels: User-defined labels (key-value pairs)

          server: ID of the Server to assign the Floating IP to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/floating_ips",
            body=maybe_transform(
                {
                    "type": type,
                    "description": description,
                    "home_location": home_location,
                    "labels": labels,
                    "name": name,
                    "server": server,
                },
                floating_ip_create_params.FloatingIpCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FloatingIpCreateResponse,
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
    ) -> FloatingIpRetrieveResponse:
        """
        Returns a specific Floating IP object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/floating_ips/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FloatingIpRetrieveResponse,
        )

    def update(
        self,
        id: int,
        *,
        description: str | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> FloatingIpUpdateResponse:
        """Updates the description or labels of a Floating IP.

        Also note that when updating
        labels, the Floating IP’s current set of labels will be replaced with the labels
        provided in the request body. So, for example, if you want to add a new label,
        you have to provide all existing labels plus the new label in the request body.

        Args:
          description: New Description to set

          labels: User-defined labels (key-value pairs)

          name: New unique name to set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/floating_ips/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "labels": labels,
                    "name": name,
                },
                floating_ip_update_params.FloatingIpUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FloatingIpUpdateResponse,
        )

    def list(
        self,
        *,
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
    ) -> SyncFloatingIpsPage[FloatingIp]:
        """
        Returns all Floating IP objects.

        Args:
          label_selector: Can be used to filter Floating IPs by labels. The response will only contain
              Floating IPs matching the label selector.

          name: Can be used to filter Floating IPs by their name. The response will only contain
              the Floating IP matching the specified name.

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
        return self._get_api_list(
            "/floating_ips",
            page=SyncFloatingIpsPage[FloatingIp],
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
                        "sort": sort,
                    },
                    floating_ip_list_params.FloatingIpListParams,
                ),
            ),
            model=FloatingIp,
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
        """Deletes a Floating IP.

        If it is currently assigned to a Server it will
        automatically get unassigned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/floating_ips/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncFloatingIps(AsyncAPIResource):
    actions: AsyncActions

    def __init__(self, client: AsyncHetzner) -> None:
        super().__init__(client)
        self.actions = AsyncActions(client)

    async def create(
        self,
        *,
        type: Literal["ipv4", "ipv6"],
        description: str | NotGiven = NOT_GIVEN,
        home_location: str | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        server: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> FloatingIpCreateResponse:
        """Creates a new Floating IP assigned to a Server.

        If you want to create a Floating
        IP that is not bound to a Server, you need to provide the `home_location` key
        instead of `server`. This can be either the ID or the name of the Location this
        IP shall be created in. Note that a Floating IP can be assigned to a Server in
        any Location later on. For optimal routing it is advised to use the Floating IP
        in the same Location it was created in.

        Args:
          type: The type of the IP

          home_location: Home Location (routing is optimized for that Location). Only optional if Server
              argument is passed.

          labels: User-defined labels (key-value pairs)

          server: ID of the Server to assign the Floating IP to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/floating_ips",
            body=maybe_transform(
                {
                    "type": type,
                    "description": description,
                    "home_location": home_location,
                    "labels": labels,
                    "name": name,
                    "server": server,
                },
                floating_ip_create_params.FloatingIpCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FloatingIpCreateResponse,
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
    ) -> FloatingIpRetrieveResponse:
        """
        Returns a specific Floating IP object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/floating_ips/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FloatingIpRetrieveResponse,
        )

    async def update(
        self,
        id: int,
        *,
        description: str | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> FloatingIpUpdateResponse:
        """Updates the description or labels of a Floating IP.

        Also note that when updating
        labels, the Floating IP’s current set of labels will be replaced with the labels
        provided in the request body. So, for example, if you want to add a new label,
        you have to provide all existing labels plus the new label in the request body.

        Args:
          description: New Description to set

          labels: User-defined labels (key-value pairs)

          name: New unique name to set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/floating_ips/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "labels": labels,
                    "name": name,
                },
                floating_ip_update_params.FloatingIpUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FloatingIpUpdateResponse,
        )

    def list(
        self,
        *,
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
    ) -> AsyncPaginator[FloatingIp, AsyncFloatingIpsPage[FloatingIp]]:
        """
        Returns all Floating IP objects.

        Args:
          label_selector: Can be used to filter Floating IPs by labels. The response will only contain
              Floating IPs matching the label selector.

          name: Can be used to filter Floating IPs by their name. The response will only contain
              the Floating IP matching the specified name.

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
        return self._get_api_list(
            "/floating_ips",
            page=AsyncFloatingIpsPage[FloatingIp],
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
                        "sort": sort,
                    },
                    floating_ip_list_params.FloatingIpListParams,
                ),
            ),
            model=FloatingIp,
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
        """Deletes a Floating IP.

        If it is currently assigned to a Server it will
        automatically get unassigned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/floating_ips/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )
