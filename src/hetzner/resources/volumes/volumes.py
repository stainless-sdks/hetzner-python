# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict
from typing_extensions import Literal

from ...types import (
    VolumeListResponse,
    VolumeCreateResponse,
    VolumeUpdateResponse,
    VolumeRetrieveResponse,
    volume_list_params,
    volume_create_params,
    volume_update_params,
)
from .actions import Actions, AsyncActions
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Hetzner, AsyncHetzner

__all__ = ["Volumes", "AsyncVolumes"]


class Volumes(SyncAPIResource):
    actions: Actions

    def __init__(self, client: Hetzner) -> None:
        super().__init__(client)
        self.actions = Actions(client)

    def create(
        self,
        *,
        name: str,
        size: int,
        automount: bool | NotGiven = NOT_GIVEN,
        format: str | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        server: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> VolumeCreateResponse:
        """Creates a new Volume attached to a Server.

        If you want to create a Volume that
        is not attached to a Server, you need to provide the `location` key instead of
        `server`. This can be either the ID or the name of the Location this Volume will
        be created in. Note that a Volume can be attached to a Server only in the same
        Location as the Volume itself.

        Specifying the Server during Volume creation will automatically attach the
        Volume to that Server after it has been initialized. In that case, the
        `next_actions` key in the response is an array which contains a single
        `attach_volume` action.

        The minimum Volume size is 10GB and the maximum size is 10TB (10240GB).

        A volume’s name can consist of alphanumeric characters, dashes, underscores, and
        dots, but has to start and end with an alphanumeric character. The total length
        is limited to 64 characters. Volume names must be unique per Project.

        #### Call specific error codes

        | Code                        | Description                                         |
        | --------------------------- | --------------------------------------------------- |
        | `no_space_left_in_location` | There is no volume space left in the given location |

        Args:
          name: Name of the volume

          size: Size of the Volume in GB

          automount: Auto-mount Volume after attach. `server` must be provided.

          format: Format Volume after creation. One of: `xfs`, `ext4`

          labels: User-defined labels (key-value pairs)

          location: Location to create the Volume in (can be omitted if Server is specified)

          server: Server to which to attach the Volume once it's created (Volume will be created
              in the same Location as the server)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/volumes",
            body=maybe_transform(
                {
                    "name": name,
                    "size": size,
                    "automount": automount,
                    "format": format,
                    "labels": labels,
                    "location": location,
                    "server": server,
                },
                volume_create_params.VolumeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeCreateResponse,
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
    ) -> VolumeRetrieveResponse:
        """
        Gets a specific Volume object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/volumes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeRetrieveResponse,
        )

    def update(
        self,
        id: int,
        *,
        name: str,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> VolumeUpdateResponse:
        """
        Updates the Volume properties.

        Note that when updating labels, the volume’s current set of labels will be
        replaced with the labels provided in the request body. So, for example, if you
        want to add a new label, you have to provide all existing labels plus the new
        label in the request body.

        Args:
          name: New Volume name

          labels: User-defined labels (key-value pairs)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/volumes/{id}",
            body=maybe_transform(
                {
                    "name": name,
                    "labels": labels,
                },
                volume_update_params.VolumeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeUpdateResponse,
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
        status: Literal["available", "creating"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> VolumeListResponse:
        """
        Gets all existing Volumes that you have available.

        Args:
          label_selector: Can be used to filter resources by labels. The response will only contain
              resources matching the label selector.

          name: Can be used to filter resources by their name. The response will only contain
              the resources matching the specified name

          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          sort: Can be used multiple times.

          status: Can be used multiple times. The response will only contain Volumes matching the
              status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/volumes",
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
                    volume_list_params.VolumeListParams,
                ),
            ),
            cast_to=VolumeListResponse,
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
        """Deletes a volume.

        All Volume data is irreversibly destroyed. The Volume must not
        be attached to a Server and it must not have delete protection enabled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/volumes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncVolumes(AsyncAPIResource):
    actions: AsyncActions

    def __init__(self, client: AsyncHetzner) -> None:
        super().__init__(client)
        self.actions = AsyncActions(client)

    async def create(
        self,
        *,
        name: str,
        size: int,
        automount: bool | NotGiven = NOT_GIVEN,
        format: str | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        server: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> VolumeCreateResponse:
        """Creates a new Volume attached to a Server.

        If you want to create a Volume that
        is not attached to a Server, you need to provide the `location` key instead of
        `server`. This can be either the ID or the name of the Location this Volume will
        be created in. Note that a Volume can be attached to a Server only in the same
        Location as the Volume itself.

        Specifying the Server during Volume creation will automatically attach the
        Volume to that Server after it has been initialized. In that case, the
        `next_actions` key in the response is an array which contains a single
        `attach_volume` action.

        The minimum Volume size is 10GB and the maximum size is 10TB (10240GB).

        A volume’s name can consist of alphanumeric characters, dashes, underscores, and
        dots, but has to start and end with an alphanumeric character. The total length
        is limited to 64 characters. Volume names must be unique per Project.

        #### Call specific error codes

        | Code                        | Description                                         |
        | --------------------------- | --------------------------------------------------- |
        | `no_space_left_in_location` | There is no volume space left in the given location |

        Args:
          name: Name of the volume

          size: Size of the Volume in GB

          automount: Auto-mount Volume after attach. `server` must be provided.

          format: Format Volume after creation. One of: `xfs`, `ext4`

          labels: User-defined labels (key-value pairs)

          location: Location to create the Volume in (can be omitted if Server is specified)

          server: Server to which to attach the Volume once it's created (Volume will be created
              in the same Location as the server)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/volumes",
            body=maybe_transform(
                {
                    "name": name,
                    "size": size,
                    "automount": automount,
                    "format": format,
                    "labels": labels,
                    "location": location,
                    "server": server,
                },
                volume_create_params.VolumeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeCreateResponse,
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
    ) -> VolumeRetrieveResponse:
        """
        Gets a specific Volume object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/volumes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeRetrieveResponse,
        )

    async def update(
        self,
        id: int,
        *,
        name: str,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> VolumeUpdateResponse:
        """
        Updates the Volume properties.

        Note that when updating labels, the volume’s current set of labels will be
        replaced with the labels provided in the request body. So, for example, if you
        want to add a new label, you have to provide all existing labels plus the new
        label in the request body.

        Args:
          name: New Volume name

          labels: User-defined labels (key-value pairs)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/volumes/{id}",
            body=maybe_transform(
                {
                    "name": name,
                    "labels": labels,
                },
                volume_update_params.VolumeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VolumeUpdateResponse,
        )

    async def list(
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
        status: Literal["available", "creating"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> VolumeListResponse:
        """
        Gets all existing Volumes that you have available.

        Args:
          label_selector: Can be used to filter resources by labels. The response will only contain
              resources matching the label selector.

          name: Can be used to filter resources by their name. The response will only contain
              the resources matching the specified name

          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          sort: Can be used multiple times.

          status: Can be used multiple times. The response will only contain Volumes matching the
              status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/volumes",
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
                    volume_list_params.VolumeListParams,
                ),
            ),
            cast_to=VolumeListResponse,
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
        """Deletes a volume.

        All Volume data is irreversibly destroyed. The Volume must not
        be attached to a Server and it must not have delete protection enabled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/volumes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )
