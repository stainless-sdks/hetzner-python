# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List
from typing_extensions import Literal

from ...types import (
    LoadBalancerListResponse,
    LoadBalancerCreateResponse,
    LoadBalancerUpdateResponse,
    LoadBalancerRetrieveResponse,
    LoadBalancerServiceModelParam,
    load_balancer_list_params,
    load_balancer_create_params,
    load_balancer_update_params,
)
from .actions import Actions, AsyncActions
from .metrics import Metrics, AsyncMetrics
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Hetzner, AsyncHetzner

__all__ = ["LoadBalancers", "AsyncLoadBalancers"]


class LoadBalancers(SyncAPIResource):
    actions: Actions
    metrics: Metrics

    def __init__(self, client: Hetzner) -> None:
        super().__init__(client)
        self.actions = Actions(client)
        self.metrics = Metrics(client)

    def create(
        self,
        *,
        algorithm: load_balancer_create_params.Algorithm,
        load_balancer_type: str,
        name: str,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        network: int | NotGiven = NOT_GIVEN,
        network_zone: str | NotGiven = NOT_GIVEN,
        public_interface: bool | NotGiven = NOT_GIVEN,
        services: List[LoadBalancerServiceModelParam] | NotGiven = NOT_GIVEN,
        targets: List[load_balancer_create_params.Target] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancerCreateResponse:
        """
        Creates a Load Balancer.

        #### Call specific error codes

        | Code                                    | Description                                                                                           |
        | --------------------------------------- | ----------------------------------------------------------------------------------------------------- |
        | `cloud_resource_ip_not_allowed`         | The IP you are trying to add as a target belongs to a Hetzner Cloud resource                          |
        | `ip_not_owned`                          | The IP is not owned by the owner of the project of the Load Balancer                                  |
        | `load_balancer_not_attached_to_network` | The Load Balancer is not attached to a network                                                        |
        | `robot_unavailable`                     | Robot was not available. The caller may retry the operation after a short delay.                      |
        | `server_not_attached_to_network`        | The server you are trying to add as a target is not attached to the same network as the Load Balancer |
        | `source_port_already_used`              | The source port you are trying to add is already in use                                               |
        | `target_already_defined`                | The Load Balancer target you are trying to define is already defined                                  |

        Args:
          algorithm: Algorithm of the Load Balancer | Request for POST
              https://api.hetzner.cloud/v1/load_balancers/{id}/actions/change_algorithm

          load_balancer_type: ID or name of the Load Balancer type this Load Balancer should be created with

          name: Name of the Load Balancer

          labels: User-defined labels (key-value pairs)

          location: ID or name of Location to create Load Balancer in

          network: ID of the network the Load Balancer should be attached to on creation

          network_zone: Name of network zone

          public_interface: Enable or disable the public interface of the Load Balancer

          services: Array of services

          targets: Array of targets

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/load_balancers",
            body=maybe_transform(
                {
                    "algorithm": algorithm,
                    "load_balancer_type": load_balancer_type,
                    "name": name,
                    "labels": labels,
                    "location": location,
                    "network": network,
                    "network_zone": network_zone,
                    "public_interface": public_interface,
                    "services": services,
                    "targets": targets,
                },
                load_balancer_create_params.LoadBalancerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoadBalancerCreateResponse,
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
    ) -> LoadBalancerRetrieveResponse:
        """
        Gets a specific Load Balancer object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/load_balancers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoadBalancerRetrieveResponse,
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
    ) -> LoadBalancerUpdateResponse:
        """Updates a Load Balancer.

        You can update a Load Balancer’s name and a Load
        Balancer’s labels.

        Note that when updating labels, the Load Balancer’s current set of labels will
        be replaced with the labels provided in the request body. So, for example, if
        you want to add a new label, you have to provide all existing labels plus the
        new label in the request body.

        Note: if the Load Balancer object changes during the request, the response will
        be a “conflict” error.

        Args:
          labels: User-defined labels (key-value pairs)

          name: New Load Balancer name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/load_balancers/{id}",
            body=maybe_transform(
                {
                    "labels": labels,
                    "name": name,
                },
                load_balancer_update_params.LoadBalancerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoadBalancerUpdateResponse,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancerListResponse:
        """
        Gets all existing Load Balancers that you have available.

        Args:
          label_selector: Can be used to filter resources by labels. The response will only contain
              resources matching the label selector.

          name: Can be used to filter resources by their name. The response will only contain
              the resources matching the specified name

          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          sort: Can be used multiple times.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/load_balancers",
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
                    load_balancer_list_params.LoadBalancerListParams,
                ),
            ),
            cast_to=LoadBalancerListResponse,
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
        """
        Deletes a Load Balancer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/load_balancers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLoadBalancers(AsyncAPIResource):
    actions: AsyncActions
    metrics: AsyncMetrics

    def __init__(self, client: AsyncHetzner) -> None:
        super().__init__(client)
        self.actions = AsyncActions(client)
        self.metrics = AsyncMetrics(client)

    async def create(
        self,
        *,
        algorithm: load_balancer_create_params.Algorithm,
        load_balancer_type: str,
        name: str,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        network: int | NotGiven = NOT_GIVEN,
        network_zone: str | NotGiven = NOT_GIVEN,
        public_interface: bool | NotGiven = NOT_GIVEN,
        services: List[LoadBalancerServiceModelParam] | NotGiven = NOT_GIVEN,
        targets: List[load_balancer_create_params.Target] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancerCreateResponse:
        """
        Creates a Load Balancer.

        #### Call specific error codes

        | Code                                    | Description                                                                                           |
        | --------------------------------------- | ----------------------------------------------------------------------------------------------------- |
        | `cloud_resource_ip_not_allowed`         | The IP you are trying to add as a target belongs to a Hetzner Cloud resource                          |
        | `ip_not_owned`                          | The IP is not owned by the owner of the project of the Load Balancer                                  |
        | `load_balancer_not_attached_to_network` | The Load Balancer is not attached to a network                                                        |
        | `robot_unavailable`                     | Robot was not available. The caller may retry the operation after a short delay.                      |
        | `server_not_attached_to_network`        | The server you are trying to add as a target is not attached to the same network as the Load Balancer |
        | `source_port_already_used`              | The source port you are trying to add is already in use                                               |
        | `target_already_defined`                | The Load Balancer target you are trying to define is already defined                                  |

        Args:
          algorithm: Algorithm of the Load Balancer | Request for POST
              https://api.hetzner.cloud/v1/load_balancers/{id}/actions/change_algorithm

          load_balancer_type: ID or name of the Load Balancer type this Load Balancer should be created with

          name: Name of the Load Balancer

          labels: User-defined labels (key-value pairs)

          location: ID or name of Location to create Load Balancer in

          network: ID of the network the Load Balancer should be attached to on creation

          network_zone: Name of network zone

          public_interface: Enable or disable the public interface of the Load Balancer

          services: Array of services

          targets: Array of targets

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/load_balancers",
            body=maybe_transform(
                {
                    "algorithm": algorithm,
                    "load_balancer_type": load_balancer_type,
                    "name": name,
                    "labels": labels,
                    "location": location,
                    "network": network,
                    "network_zone": network_zone,
                    "public_interface": public_interface,
                    "services": services,
                    "targets": targets,
                },
                load_balancer_create_params.LoadBalancerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoadBalancerCreateResponse,
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
    ) -> LoadBalancerRetrieveResponse:
        """
        Gets a specific Load Balancer object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/load_balancers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoadBalancerRetrieveResponse,
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
    ) -> LoadBalancerUpdateResponse:
        """Updates a Load Balancer.

        You can update a Load Balancer’s name and a Load
        Balancer’s labels.

        Note that when updating labels, the Load Balancer’s current set of labels will
        be replaced with the labels provided in the request body. So, for example, if
        you want to add a new label, you have to provide all existing labels plus the
        new label in the request body.

        Note: if the Load Balancer object changes during the request, the response will
        be a “conflict” error.

        Args:
          labels: User-defined labels (key-value pairs)

          name: New Load Balancer name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/load_balancers/{id}",
            body=maybe_transform(
                {
                    "labels": labels,
                    "name": name,
                },
                load_balancer_update_params.LoadBalancerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoadBalancerUpdateResponse,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancerListResponse:
        """
        Gets all existing Load Balancers that you have available.

        Args:
          label_selector: Can be used to filter resources by labels. The response will only contain
              resources matching the label selector.

          name: Can be used to filter resources by their name. The response will only contain
              the resources matching the specified name

          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          sort: Can be used multiple times.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/load_balancers",
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
                    load_balancer_list_params.LoadBalancerListParams,
                ),
            ),
            cast_to=LoadBalancerListResponse,
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
        """
        Deletes a Load Balancer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/load_balancers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )
