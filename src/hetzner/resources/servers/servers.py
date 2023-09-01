# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List
from typing_extensions import Literal

from ...types import (
    Server,
    ServerCreateResponse,
    ServerDeleteResponse,
    ServerUpdateResponse,
    ServerRetrieveResponse,
    server_list_params,
    server_create_params,
    server_update_params,
)
from .actions import Actions, AsyncActions
from .metrics import Metrics, AsyncMetrics
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncServersPage, AsyncServersPage
from ..._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from ..._client import Hetzner, AsyncHetzner

__all__ = ["Servers", "AsyncServers"]


class Servers(SyncAPIResource):
    actions: Actions
    metrics: Metrics

    def __init__(self, client: Hetzner) -> None:
        super().__init__(client)
        self.actions = Actions(client)
        self.metrics = Metrics(client)

    def create(
        self,
        *,
        image: str,
        name: str,
        server_type: str,
        automount: bool | NotGiven = NOT_GIVEN,
        datacenter: str | NotGiven = NOT_GIVEN,
        firewalls: List[server_create_params.Firewall] | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        networks: List[int] | NotGiven = NOT_GIVEN,
        placement_group: int | NotGiven = NOT_GIVEN,
        public_net: server_create_params.PublicNet | NotGiven = NOT_GIVEN,
        ssh_keys: List[str] | NotGiven = NOT_GIVEN,
        start_after_create: bool | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        volumes: List[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ServerCreateResponse:
        """Creates a new Server.

        Returns preliminary information about the Server as well
        as an Action that covers progress of creation.

        Args:
          image: ID or name of the Image the Server is created from

          name: Name of the Server to create (must be unique per Project and a valid hostname as
              per RFC 1123)

          server_type: ID or name of the Server type this Server should be created with

          automount: Auto-mount Volumes after attach

          datacenter: ID or name of Datacenter to create Server in (must not be used together with
              location)

          firewalls: Firewalls which should be applied on the Server's public network interface at
              creation time

          labels: User-defined labels (key-value pairs)

          location: ID or name of Location to create Server in (must not be used together with
              datacenter)

          networks: Network IDs which should be attached to the Server private network interface at
              the creation time

          placement_group: ID of the Placement Group the server should be in

          public_net: Public Network options

          ssh_keys: SSH key IDs (`integer`) or names (`string`) which should be injected into the
              Server at creation time

          start_after_create: Start Server right after creation. Defaults to true.

          user_data: Cloud-Init user data to use during Server creation. This field is limited to
              32KiB.

          volumes: Volume IDs which should be attached to the Server at the creation time. Volumes
              must be in the same Location.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/servers",
            body=maybe_transform(
                {
                    "image": image,
                    "name": name,
                    "server_type": server_type,
                    "automount": automount,
                    "datacenter": datacenter,
                    "firewalls": firewalls,
                    "labels": labels,
                    "location": location,
                    "networks": networks,
                    "placement_group": placement_group,
                    "public_net": public_net,
                    "ssh_keys": ssh_keys,
                    "start_after_create": start_after_create,
                    "user_data": user_data,
                    "volumes": volumes,
                },
                server_create_params.ServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerCreateResponse,
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
    ) -> ServerRetrieveResponse:
        """Returns a specific Server object.

        The Server must exist inside the Project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/servers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerRetrieveResponse,
        )

    def update(
        self,
        id: int,
        *,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ServerUpdateResponse:
        """Updates a Server.

        You can update a Server’s name and a Server’s labels. Please
        note that Server names must be unique per Project and valid hostnames as per RFC
        1123 (i.e. may only contain letters, digits, periods, and dashes). Also note
        that when updating labels, the Server’s current set of labels will be replaced
        with the labels provided in the request body. So, for example, if you want to
        add a new label, you have to provide all existing labels plus the new label in
        the request body.

        Args:
          labels: User-defined labels (key-value pairs)

          name: New name to set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/servers/{id}",
            body=maybe_transform(
                {
                    "labels": labels,
                    "name": name,
                },
                server_update_params.ServerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerUpdateResponse,
        )

    def list(
        self,
        *,
        label_selector: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal[
            "id", "id:asc", "id:desc", "name", "name:asc", "name:desc", "created", "created:asc", "created:desc"
        ]
        | NotGiven = NOT_GIVEN,
        status: Literal[
            "initializing", "starting", "running", "stopping", "off", "deleting", "rebuilding", "migrating", "unknown"
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncServersPage[Server]:
        """
        Returns all existing Server objects

        Args:
          label_selector: Can be used to filter resources by labels. The response will only contain
              resources matching the label selector.

          name: Can be used to filter resources by their name. The response will only contain
              the resources matching the specified name

          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          sort: Can be used multiple times.

          status: Can be used multiple times. The response will only contain Server matching the
              status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/servers",
            page=SyncServersPage[Server],
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
                        "status": status,
                    },
                    server_list_params.ServerListParams,
                ),
            ),
            model=Server,
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
    ) -> ServerDeleteResponse:
        """Deletes a Server.

        This immediately removes the Server from your account, and it
        is no longer accessible.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/servers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerDeleteResponse,
        )


class AsyncServers(AsyncAPIResource):
    actions: AsyncActions
    metrics: AsyncMetrics

    def __init__(self, client: AsyncHetzner) -> None:
        super().__init__(client)
        self.actions = AsyncActions(client)
        self.metrics = AsyncMetrics(client)

    async def create(
        self,
        *,
        image: str,
        name: str,
        server_type: str,
        automount: bool | NotGiven = NOT_GIVEN,
        datacenter: str | NotGiven = NOT_GIVEN,
        firewalls: List[server_create_params.Firewall] | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        networks: List[int] | NotGiven = NOT_GIVEN,
        placement_group: int | NotGiven = NOT_GIVEN,
        public_net: server_create_params.PublicNet | NotGiven = NOT_GIVEN,
        ssh_keys: List[str] | NotGiven = NOT_GIVEN,
        start_after_create: bool | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        volumes: List[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ServerCreateResponse:
        """Creates a new Server.

        Returns preliminary information about the Server as well
        as an Action that covers progress of creation.

        Args:
          image: ID or name of the Image the Server is created from

          name: Name of the Server to create (must be unique per Project and a valid hostname as
              per RFC 1123)

          server_type: ID or name of the Server type this Server should be created with

          automount: Auto-mount Volumes after attach

          datacenter: ID or name of Datacenter to create Server in (must not be used together with
              location)

          firewalls: Firewalls which should be applied on the Server's public network interface at
              creation time

          labels: User-defined labels (key-value pairs)

          location: ID or name of Location to create Server in (must not be used together with
              datacenter)

          networks: Network IDs which should be attached to the Server private network interface at
              the creation time

          placement_group: ID of the Placement Group the server should be in

          public_net: Public Network options

          ssh_keys: SSH key IDs (`integer`) or names (`string`) which should be injected into the
              Server at creation time

          start_after_create: Start Server right after creation. Defaults to true.

          user_data: Cloud-Init user data to use during Server creation. This field is limited to
              32KiB.

          volumes: Volume IDs which should be attached to the Server at the creation time. Volumes
              must be in the same Location.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/servers",
            body=maybe_transform(
                {
                    "image": image,
                    "name": name,
                    "server_type": server_type,
                    "automount": automount,
                    "datacenter": datacenter,
                    "firewalls": firewalls,
                    "labels": labels,
                    "location": location,
                    "networks": networks,
                    "placement_group": placement_group,
                    "public_net": public_net,
                    "ssh_keys": ssh_keys,
                    "start_after_create": start_after_create,
                    "user_data": user_data,
                    "volumes": volumes,
                },
                server_create_params.ServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerCreateResponse,
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
    ) -> ServerRetrieveResponse:
        """Returns a specific Server object.

        The Server must exist inside the Project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/servers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerRetrieveResponse,
        )

    async def update(
        self,
        id: int,
        *,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ServerUpdateResponse:
        """Updates a Server.

        You can update a Server’s name and a Server’s labels. Please
        note that Server names must be unique per Project and valid hostnames as per RFC
        1123 (i.e. may only contain letters, digits, periods, and dashes). Also note
        that when updating labels, the Server’s current set of labels will be replaced
        with the labels provided in the request body. So, for example, if you want to
        add a new label, you have to provide all existing labels plus the new label in
        the request body.

        Args:
          labels: User-defined labels (key-value pairs)

          name: New name to set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/servers/{id}",
            body=maybe_transform(
                {
                    "labels": labels,
                    "name": name,
                },
                server_update_params.ServerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerUpdateResponse,
        )

    def list(
        self,
        *,
        label_selector: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal[
            "id", "id:asc", "id:desc", "name", "name:asc", "name:desc", "created", "created:asc", "created:desc"
        ]
        | NotGiven = NOT_GIVEN,
        status: Literal[
            "initializing", "starting", "running", "stopping", "off", "deleting", "rebuilding", "migrating", "unknown"
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Server, AsyncServersPage[Server]]:
        """
        Returns all existing Server objects

        Args:
          label_selector: Can be used to filter resources by labels. The response will only contain
              resources matching the label selector.

          name: Can be used to filter resources by their name. The response will only contain
              the resources matching the specified name

          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          sort: Can be used multiple times.

          status: Can be used multiple times. The response will only contain Server matching the
              status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/servers",
            page=AsyncServersPage[Server],
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
                        "status": status,
                    },
                    server_list_params.ServerListParams,
                ),
            ),
            model=Server,
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
    ) -> ServerDeleteResponse:
        """Deletes a Server.

        This immediately removes the Server from your account, and it
        is no longer accessible.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/servers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerDeleteResponse,
        )
