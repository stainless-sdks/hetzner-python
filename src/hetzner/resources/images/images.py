# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict
from typing_extensions import Literal

from ...types import (
    ImageListResponse,
    ImageUpdateResponse,
    ImageRetrieveResponse,
    image_list_params,
    image_update_params,
)
from .actions import Actions, AsyncActions
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Hetzner, AsyncHetzner

__all__ = ["Images", "AsyncImages"]


class Images(SyncAPIResource):
    actions: Actions

    def __init__(self, client: Hetzner) -> None:
        super().__init__(client)
        self.actions = Actions(client)

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
    ) -> ImageRetrieveResponse:
        """
        Returns a specific Image object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/images/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageRetrieveResponse,
        )

    def update(
        self,
        id: int,
        *,
        description: str | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        type: Literal["snapshot"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ImageUpdateResponse:
        """Updates the Image.

        You may change the description, convert a Backup Image to a
        Snapshot Image or change the Image labels. Only Images of type `snapshot` and
        `backup` can be updated.

        Note that when updating labels, the current set of labels will be replaced with
        the labels provided in the request body. So, for example, if you want to add a
        new label, you have to provide all existing labels plus the new label in the
        request body.

        Args:
          description: New description of Image

          labels: User-defined labels (key-value pairs)

          type: Destination Image type to convert to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/images/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "labels": labels,
                    "type": type,
                },
                image_update_params.ImageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageUpdateResponse,
        )

    def list(
        self,
        *,
        architecture: str | NotGiven = NOT_GIVEN,
        bound_to: str | NotGiven = NOT_GIVEN,
        include_deprecated: bool | NotGiven = NOT_GIVEN,
        label_selector: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal[
            "id", "id:asc", "id:desc", "name", "name:asc", "name:desc", "created", "created:asc", "created:desc"
        ]
        | NotGiven = NOT_GIVEN,
        status: Literal["available", "creating"] | NotGiven = NOT_GIVEN,
        type: Literal["system", "snapshot", "backup", "app"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ImageListResponse:
        """Returns all Image objects.

        You can select specific Image types only and sort the
        results by using URI parameters.

        Args:
          architecture: Return only Images with the given architecture.

          bound_to: Can be used multiple times. Server ID linked to the Image. Only available for
              Images of type `backup`

          include_deprecated: Can be used multiple times.

          label_selector: Can be used to filter resources by labels. The response will only contain
              resources matching the label selector.

          name: Can be used to filter resources by their name. The response will only contain
              the resources matching the specified name

          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          sort: Can be used multiple times.

          status: Can be used multiple times. The response will only contain Images matching the
              status.

          type: Can be used multiple times.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "architecture": architecture,
                        "bound_to": bound_to,
                        "include_deprecated": include_deprecated,
                        "label_selector": label_selector,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "status": status,
                        "type": type,
                    },
                    image_list_params.ImageListParams,
                ),
            ),
            cast_to=ImageListResponse,
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
        """Deletes an Image.

        Only Images of type `snapshot` and `backup` can be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/images/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncImages(AsyncAPIResource):
    actions: AsyncActions

    def __init__(self, client: AsyncHetzner) -> None:
        super().__init__(client)
        self.actions = AsyncActions(client)

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
    ) -> ImageRetrieveResponse:
        """
        Returns a specific Image object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/images/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageRetrieveResponse,
        )

    async def update(
        self,
        id: int,
        *,
        description: str | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        type: Literal["snapshot"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ImageUpdateResponse:
        """Updates the Image.

        You may change the description, convert a Backup Image to a
        Snapshot Image or change the Image labels. Only Images of type `snapshot` and
        `backup` can be updated.

        Note that when updating labels, the current set of labels will be replaced with
        the labels provided in the request body. So, for example, if you want to add a
        new label, you have to provide all existing labels plus the new label in the
        request body.

        Args:
          description: New description of Image

          labels: User-defined labels (key-value pairs)

          type: Destination Image type to convert to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/images/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "labels": labels,
                    "type": type,
                },
                image_update_params.ImageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageUpdateResponse,
        )

    async def list(
        self,
        *,
        architecture: str | NotGiven = NOT_GIVEN,
        bound_to: str | NotGiven = NOT_GIVEN,
        include_deprecated: bool | NotGiven = NOT_GIVEN,
        label_selector: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal[
            "id", "id:asc", "id:desc", "name", "name:asc", "name:desc", "created", "created:asc", "created:desc"
        ]
        | NotGiven = NOT_GIVEN,
        status: Literal["available", "creating"] | NotGiven = NOT_GIVEN,
        type: Literal["system", "snapshot", "backup", "app"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ImageListResponse:
        """Returns all Image objects.

        You can select specific Image types only and sort the
        results by using URI parameters.

        Args:
          architecture: Return only Images with the given architecture.

          bound_to: Can be used multiple times. Server ID linked to the Image. Only available for
              Images of type `backup`

          include_deprecated: Can be used multiple times.

          label_selector: Can be used to filter resources by labels. The response will only contain
              resources matching the label selector.

          name: Can be used to filter resources by their name. The response will only contain
              the resources matching the specified name

          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          sort: Can be used multiple times.

          status: Can be used multiple times. The response will only contain Images matching the
              status.

          type: Can be used multiple times.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "architecture": architecture,
                        "bound_to": bound_to,
                        "include_deprecated": include_deprecated,
                        "label_selector": label_selector,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "status": status,
                        "type": type,
                    },
                    image_list_params.ImageListParams,
                ),
            ),
            cast_to=ImageListResponse,
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
        """Deletes an Image.

        Only Images of type `snapshot` and `backup` can be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/images/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )
