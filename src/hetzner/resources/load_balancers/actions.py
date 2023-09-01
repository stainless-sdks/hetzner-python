# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ...types import LoadBalancerTargetIPParam, shared_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.load_balancers import (
    ActionListResponse,
    ActionRetrieveResponse,
    ActionAssTargetResponse,
    ActionAddServiceResponse,
    ActionChangeTypeResponse,
    ActionChangeDNSPtrResponse,
    ActionRemoveTargetResponse,
    ActionDeleteServiceResponse,
    ActionUpdateServiceResponse,
    ActionAttachToNetworkResponse,
    ActionChangeAlgorithmResponse,
    ActionChangeProtectionResponse,
    ActionDetachFromNetworkResponse,
    ActionEnablePublicInterfaceResponse,
    ActionDisablePublicInterfaceResponse,
    action_list_params,
    action_ass_target_params,
    action_add_service_params,
    action_change_type_params,
    action_remove_target_params,
    action_change_dns_ptr_params,
    action_delete_service_params,
    action_update_service_params,
    action_change_algorithm_params,
    action_attach_to_network_params,
    action_change_protection_params,
    action_detach_from_network_params,
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
        Returns a specific Action for a Load Balancer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/load_balancers/{id}/actions/{action_id}",
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
        """Returns all Action objects for a Load Balancer.

        You can sort the results by
        using the `sort` URI parameter, and filter them with the `status` parameter.

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
            f"/load_balancers/{id}/actions",
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

    def add_service(
        self,
        id: int,
        *,
        destination_port: int,
        health_check: action_add_service_params.HealthCheck,
        listen_port: int,
        protocol: Literal["http", "https", "tcp"],
        proxyprotocol: bool,
        http: action_add_service_params.HTTP | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionAddServiceResponse:
        """
        Adds a service to a Load Balancer.

        #### Call specific error codes

        | Code                       | Description                                             |
        | -------------------------- | ------------------------------------------------------- |
        | `source_port_already_used` | The source port you are trying to add is already in use |

        Args:
          destination_port: Port the Load Balancer will balance to

          health_check: Service health check

          listen_port: Port the Load Balancer listens on

          protocol: Protocol of the Load Balancer

          proxyprotocol: Is Proxyprotocol enabled or not

          http: Configuration option for protocols http and https

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/load_balancers/{id}/actions/add_service",
            body=maybe_transform(
                {
                    "destination_port": destination_port,
                    "health_check": health_check,
                    "listen_port": listen_port,
                    "protocol": protocol,
                    "proxyprotocol": proxyprotocol,
                    "http": http,
                },
                action_add_service_params.ActionAddServiceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAddServiceResponse,
        )

    def ass_target(
        self,
        id: int,
        *,
        type: Literal["ip", "label_selector", "server"],
        ip: LoadBalancerTargetIPParam | NotGiven = NOT_GIVEN,
        label_selector: action_ass_target_params.LabelSelector | NotGiven = NOT_GIVEN,
        server: action_ass_target_params.Server | NotGiven = NOT_GIVEN,
        use_private_ip: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionAssTargetResponse:
        """
        Adds a target to a Load Balancer.

        #### Call specific error codes

        | Code                                    | Description                                                                                           |
        | --------------------------------------- | ----------------------------------------------------------------------------------------------------- |
        | `cloud_resource_ip_not_allowed`         | The IP you are trying to add as a target belongs to a Hetzner Cloud resource                          |
        | `ip_not_owned`                          | The IP you are trying to add as a target is not owned by the Project owner                            |
        | `load_balancer_not_attached_to_network` | The Load Balancer is not attached to a network                                                        |
        | `robot_unavailable`                     | Robot was not available. The caller may retry the operation after a short delay.                      |
        | `server_not_attached_to_network`        | The server you are trying to add as a target is not attached to the same network as the Load Balancer |
        | `target_already_defined`                | The Load Balancer target you are trying to define is already defined                                  |

        Args:
          type: Type of the resource

          ip: IP targets where the traffic should be routed to. It is only possible to use the
              (Public or vSwitch) IPs of Hetzner Online Root Servers belonging to the project
              owner. IPs belonging to other users are blocked. Additionally IPs belonging to
              services provided by Hetzner Cloud (Servers, Load Balancers, ...) are blocked as
              well. Only present for target type "ip".

          label_selector: Configuration for type LabelSelector, required if type is `label_selector`

          server: Configuration for type Server, required if type is `server`

          use_private_ip: Use the private network IP instead of the public IP of the Server, requires the
              Server and Load Balancer to be in the same network. Default value is false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/load_balancers/{id}/actions/add_target",
            body=maybe_transform(
                {
                    "type": type,
                    "ip": ip,
                    "label_selector": label_selector,
                    "server": server,
                    "use_private_ip": use_private_ip,
                },
                action_ass_target_params.ActionAssTargetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAssTargetResponse,
        )

    def attach_to_network(
        self,
        id: int,
        *,
        network: int,
        ip: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionAttachToNetworkResponse:
        """
        Attach a Load Balancer to a Network.

        **Call specific error codes**

        | Code                             | Description                                                           |
        | -------------------------------- | --------------------------------------------------------------------- |
        | `load_balancer_already_attached` | The Load Balancer is already attached to a network                    |
        | `ip_not_available`               | The provided Network IP is not available                              |
        | `no_subnet_available`            | No Subnet or IP is available for the Load Balancer within the network |

        Args:
          network: ID of an existing network to attach the Load Balancer to

          ip: IP to request to be assigned to this Load Balancer; if you do not provide this
              then you will be auto assigned an IP address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/load_balancers/{id}/actions/attach_to_network",
            body=maybe_transform(
                {
                    "network": network,
                    "ip": ip,
                },
                action_attach_to_network_params.ActionAttachToNetworkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAttachToNetworkResponse,
        )

    def change_algorithm(
        self,
        id: int,
        *,
        type: Literal["least_connections", "round_robin"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionChangeAlgorithmResponse:
        """
        Change the algorithm that determines to which target new requests are sent.

        Args:
          type: Type of the algorithm | Algorithm of the Load Balancer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/load_balancers/{id}/actions/change_algorithm",
            body=maybe_transform({"type": type}, action_change_algorithm_params.ActionChangeAlgorithmParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeAlgorithmResponse,
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
    ) -> ActionChangeDNSPtrResponse:
        """
        Changes the hostname that will appear when getting the hostname belonging to the
        public IPs (IPv4 and IPv6) of this Load Balancer.

        Floating IPs assigned to the Server are not affected by this.

        Args:
          dns_ptr: Hostname to set as a reverse DNS PTR entry

          ip: Public IP address for which the reverse DNS entry should be set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/load_balancers/{id}/actions/change_dns_ptr",
            body=maybe_transform(
                {
                    "dns_ptr": dns_ptr,
                    "ip": ip,
                },
                action_change_dns_ptr_params.ActionChangeDNSPtrParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeDNSPtrResponse,
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
        Changes the protection configuration of a Load Balancer.

        Args:
          delete: If true, prevents the Load Balancer from being deleted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/load_balancers/{id}/actions/change_protection",
            body=maybe_transform({"delete": delete}, action_change_protection_params.ActionChangeProtectionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeProtectionResponse,
        )

    def change_type(
        self,
        id: int,
        *,
        load_balancer_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionChangeTypeResponse:
        """
        Changes the type (Max Services, Max Targets and Max Connections) of a Load
        Balancer.

        **Call specific error codes**

        | Code                         | Description                                                     |
        | ---------------------------- | --------------------------------------------------------------- |
        | `invalid_load_balancer_type` | The Load Balancer type does not fit for the given Load Balancer |

        Args:
          load_balancer_type: ID or name of Load Balancer type the Load Balancer should migrate to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/load_balancers/{id}/actions/change_type",
            body=maybe_transform(
                {"load_balancer_type": load_balancer_type}, action_change_type_params.ActionChangeTypeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeTypeResponse,
        )

    def delete_service(
        self,
        id: int,
        *,
        listen_port: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionDeleteServiceResponse:
        """
        Delete a service of a Load Balancer.

        Args:
          listen_port: The listen port of the service you want to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/load_balancers/{id}/actions/delete_service",
            body=maybe_transform({"listen_port": listen_port}, action_delete_service_params.ActionDeleteServiceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDeleteServiceResponse,
        )

    def detach_from_network(
        self,
        id: int,
        *,
        network: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionDetachFromNetworkResponse:
        """
        Detaches a Load Balancer from a network.

        Args:
          network: ID of an existing network to detach the Load Balancer from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/load_balancers/{id}/actions/detach_from_network",
            body=maybe_transform({"network": network}, action_detach_from_network_params.ActionDetachFromNetworkParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDetachFromNetworkResponse,
        )

    def disable_public_interface(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionDisablePublicInterfaceResponse:
        """Disable the public interface of a Load Balancer.

        The Load Balancer will be not
        accessible from the internet via its public IPs.

        #### Call specific error codes

        | Code                                    | Description                                                                    |
        | --------------------------------------- | ------------------------------------------------------------------------------ |
        | `load_balancer_not_attached_to_network` | The Load Balancer is not attached to a network                                 |
        | `targets_without_use_private_ip`        | The Load Balancer has targets that use the public IP instead of the private IP |

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/load_balancers/{id}/actions/disable_public_interface",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDisablePublicInterfaceResponse,
        )

    def enable_public_interface(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionEnablePublicInterfaceResponse:
        """Enable the public interface of a Load Balancer.

        The Load Balancer will be
        accessible from the internet via its public IPs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/load_balancers/{id}/actions/enable_public_interface",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionEnablePublicInterfaceResponse,
        )

    def remove_target(
        self,
        id: int,
        *,
        type: Literal["ip", "label_selector", "server"],
        ip: LoadBalancerTargetIPParam | NotGiven = NOT_GIVEN,
        label_selector: action_remove_target_params.LabelSelector | NotGiven = NOT_GIVEN,
        server: action_remove_target_params.Server | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionRemoveTargetResponse:
        """
        Removes a target from a Load Balancer.

        Args:
          type: Type of the resource

          ip: IP targets where the traffic should be routed to. It is only possible to use the
              (Public or vSwitch) IPs of Hetzner Online Root Servers belonging to the project
              owner. IPs belonging to other users are blocked. Additionally IPs belonging to
              services provided by Hetzner Cloud (Servers, Load Balancers, ...) are blocked as
              well. Only present for target type "ip".

          label_selector: Configuration for type LabelSelector, required if type is `label_selector`

          server: Configuration for type Server, required if type is `server`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/load_balancers/{id}/actions/remove_target",
            body=maybe_transform(
                {
                    "type": type,
                    "ip": ip,
                    "label_selector": label_selector,
                    "server": server,
                },
                action_remove_target_params.ActionRemoveTargetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRemoveTargetResponse,
        )

    def update_service(
        self,
        id: int,
        *,
        destination_port: int,
        health_check: action_update_service_params.HealthCheck,
        listen_port: int,
        protocol: Literal["http", "https", "tcp"],
        proxyprotocol: bool,
        http: action_update_service_params.HTTP | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionUpdateServiceResponse:
        """
        Updates a Load Balancer Service.

        #### Call specific error codes

        | Code                       | Description                                             |
        | -------------------------- | ------------------------------------------------------- |
        | `source_port_already_used` | The source port you are trying to add is already in use |

        Args:
          destination_port: Port the Load Balancer will balance to

          health_check: Service health check

          listen_port: Port the Load Balancer listens on

          protocol: Protocol of the Load Balancer

          proxyprotocol: Is Proxyprotocol enabled or not

          http: Configuration option for protocols http and https

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/load_balancers/{id}/actions/update_service",
            body=maybe_transform(
                {
                    "destination_port": destination_port,
                    "health_check": health_check,
                    "listen_port": listen_port,
                    "protocol": protocol,
                    "proxyprotocol": proxyprotocol,
                    "http": http,
                },
                action_update_service_params.ActionUpdateServiceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionUpdateServiceResponse,
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
        Returns a specific Action for a Load Balancer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/load_balancers/{id}/actions/{action_id}",
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
        """Returns all Action objects for a Load Balancer.

        You can sort the results by
        using the `sort` URI parameter, and filter them with the `status` parameter.

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
            f"/load_balancers/{id}/actions",
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

    async def add_service(
        self,
        id: int,
        *,
        destination_port: int,
        health_check: action_add_service_params.HealthCheck,
        listen_port: int,
        protocol: Literal["http", "https", "tcp"],
        proxyprotocol: bool,
        http: action_add_service_params.HTTP | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionAddServiceResponse:
        """
        Adds a service to a Load Balancer.

        #### Call specific error codes

        | Code                       | Description                                             |
        | -------------------------- | ------------------------------------------------------- |
        | `source_port_already_used` | The source port you are trying to add is already in use |

        Args:
          destination_port: Port the Load Balancer will balance to

          health_check: Service health check

          listen_port: Port the Load Balancer listens on

          protocol: Protocol of the Load Balancer

          proxyprotocol: Is Proxyprotocol enabled or not

          http: Configuration option for protocols http and https

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/load_balancers/{id}/actions/add_service",
            body=maybe_transform(
                {
                    "destination_port": destination_port,
                    "health_check": health_check,
                    "listen_port": listen_port,
                    "protocol": protocol,
                    "proxyprotocol": proxyprotocol,
                    "http": http,
                },
                action_add_service_params.ActionAddServiceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAddServiceResponse,
        )

    async def ass_target(
        self,
        id: int,
        *,
        type: Literal["ip", "label_selector", "server"],
        ip: LoadBalancerTargetIPParam | NotGiven = NOT_GIVEN,
        label_selector: action_ass_target_params.LabelSelector | NotGiven = NOT_GIVEN,
        server: action_ass_target_params.Server | NotGiven = NOT_GIVEN,
        use_private_ip: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionAssTargetResponse:
        """
        Adds a target to a Load Balancer.

        #### Call specific error codes

        | Code                                    | Description                                                                                           |
        | --------------------------------------- | ----------------------------------------------------------------------------------------------------- |
        | `cloud_resource_ip_not_allowed`         | The IP you are trying to add as a target belongs to a Hetzner Cloud resource                          |
        | `ip_not_owned`                          | The IP you are trying to add as a target is not owned by the Project owner                            |
        | `load_balancer_not_attached_to_network` | The Load Balancer is not attached to a network                                                        |
        | `robot_unavailable`                     | Robot was not available. The caller may retry the operation after a short delay.                      |
        | `server_not_attached_to_network`        | The server you are trying to add as a target is not attached to the same network as the Load Balancer |
        | `target_already_defined`                | The Load Balancer target you are trying to define is already defined                                  |

        Args:
          type: Type of the resource

          ip: IP targets where the traffic should be routed to. It is only possible to use the
              (Public or vSwitch) IPs of Hetzner Online Root Servers belonging to the project
              owner. IPs belonging to other users are blocked. Additionally IPs belonging to
              services provided by Hetzner Cloud (Servers, Load Balancers, ...) are blocked as
              well. Only present for target type "ip".

          label_selector: Configuration for type LabelSelector, required if type is `label_selector`

          server: Configuration for type Server, required if type is `server`

          use_private_ip: Use the private network IP instead of the public IP of the Server, requires the
              Server and Load Balancer to be in the same network. Default value is false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/load_balancers/{id}/actions/add_target",
            body=maybe_transform(
                {
                    "type": type,
                    "ip": ip,
                    "label_selector": label_selector,
                    "server": server,
                    "use_private_ip": use_private_ip,
                },
                action_ass_target_params.ActionAssTargetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAssTargetResponse,
        )

    async def attach_to_network(
        self,
        id: int,
        *,
        network: int,
        ip: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionAttachToNetworkResponse:
        """
        Attach a Load Balancer to a Network.

        **Call specific error codes**

        | Code                             | Description                                                           |
        | -------------------------------- | --------------------------------------------------------------------- |
        | `load_balancer_already_attached` | The Load Balancer is already attached to a network                    |
        | `ip_not_available`               | The provided Network IP is not available                              |
        | `no_subnet_available`            | No Subnet or IP is available for the Load Balancer within the network |

        Args:
          network: ID of an existing network to attach the Load Balancer to

          ip: IP to request to be assigned to this Load Balancer; if you do not provide this
              then you will be auto assigned an IP address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/load_balancers/{id}/actions/attach_to_network",
            body=maybe_transform(
                {
                    "network": network,
                    "ip": ip,
                },
                action_attach_to_network_params.ActionAttachToNetworkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAttachToNetworkResponse,
        )

    async def change_algorithm(
        self,
        id: int,
        *,
        type: Literal["least_connections", "round_robin"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionChangeAlgorithmResponse:
        """
        Change the algorithm that determines to which target new requests are sent.

        Args:
          type: Type of the algorithm | Algorithm of the Load Balancer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/load_balancers/{id}/actions/change_algorithm",
            body=maybe_transform({"type": type}, action_change_algorithm_params.ActionChangeAlgorithmParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeAlgorithmResponse,
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
    ) -> ActionChangeDNSPtrResponse:
        """
        Changes the hostname that will appear when getting the hostname belonging to the
        public IPs (IPv4 and IPv6) of this Load Balancer.

        Floating IPs assigned to the Server are not affected by this.

        Args:
          dns_ptr: Hostname to set as a reverse DNS PTR entry

          ip: Public IP address for which the reverse DNS entry should be set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/load_balancers/{id}/actions/change_dns_ptr",
            body=maybe_transform(
                {
                    "dns_ptr": dns_ptr,
                    "ip": ip,
                },
                action_change_dns_ptr_params.ActionChangeDNSPtrParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeDNSPtrResponse,
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
        Changes the protection configuration of a Load Balancer.

        Args:
          delete: If true, prevents the Load Balancer from being deleted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/load_balancers/{id}/actions/change_protection",
            body=maybe_transform({"delete": delete}, action_change_protection_params.ActionChangeProtectionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeProtectionResponse,
        )

    async def change_type(
        self,
        id: int,
        *,
        load_balancer_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionChangeTypeResponse:
        """
        Changes the type (Max Services, Max Targets and Max Connections) of a Load
        Balancer.

        **Call specific error codes**

        | Code                         | Description                                                     |
        | ---------------------------- | --------------------------------------------------------------- |
        | `invalid_load_balancer_type` | The Load Balancer type does not fit for the given Load Balancer |

        Args:
          load_balancer_type: ID or name of Load Balancer type the Load Balancer should migrate to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/load_balancers/{id}/actions/change_type",
            body=maybe_transform(
                {"load_balancer_type": load_balancer_type}, action_change_type_params.ActionChangeTypeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeTypeResponse,
        )

    async def delete_service(
        self,
        id: int,
        *,
        listen_port: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionDeleteServiceResponse:
        """
        Delete a service of a Load Balancer.

        Args:
          listen_port: The listen port of the service you want to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/load_balancers/{id}/actions/delete_service",
            body=maybe_transform({"listen_port": listen_port}, action_delete_service_params.ActionDeleteServiceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDeleteServiceResponse,
        )

    async def detach_from_network(
        self,
        id: int,
        *,
        network: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionDetachFromNetworkResponse:
        """
        Detaches a Load Balancer from a network.

        Args:
          network: ID of an existing network to detach the Load Balancer from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/load_balancers/{id}/actions/detach_from_network",
            body=maybe_transform({"network": network}, action_detach_from_network_params.ActionDetachFromNetworkParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDetachFromNetworkResponse,
        )

    async def disable_public_interface(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionDisablePublicInterfaceResponse:
        """Disable the public interface of a Load Balancer.

        The Load Balancer will be not
        accessible from the internet via its public IPs.

        #### Call specific error codes

        | Code                                    | Description                                                                    |
        | --------------------------------------- | ------------------------------------------------------------------------------ |
        | `load_balancer_not_attached_to_network` | The Load Balancer is not attached to a network                                 |
        | `targets_without_use_private_ip`        | The Load Balancer has targets that use the public IP instead of the private IP |

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/load_balancers/{id}/actions/disable_public_interface",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDisablePublicInterfaceResponse,
        )

    async def enable_public_interface(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionEnablePublicInterfaceResponse:
        """Enable the public interface of a Load Balancer.

        The Load Balancer will be
        accessible from the internet via its public IPs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/load_balancers/{id}/actions/enable_public_interface",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionEnablePublicInterfaceResponse,
        )

    async def remove_target(
        self,
        id: int,
        *,
        type: Literal["ip", "label_selector", "server"],
        ip: LoadBalancerTargetIPParam | NotGiven = NOT_GIVEN,
        label_selector: action_remove_target_params.LabelSelector | NotGiven = NOT_GIVEN,
        server: action_remove_target_params.Server | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionRemoveTargetResponse:
        """
        Removes a target from a Load Balancer.

        Args:
          type: Type of the resource

          ip: IP targets where the traffic should be routed to. It is only possible to use the
              (Public or vSwitch) IPs of Hetzner Online Root Servers belonging to the project
              owner. IPs belonging to other users are blocked. Additionally IPs belonging to
              services provided by Hetzner Cloud (Servers, Load Balancers, ...) are blocked as
              well. Only present for target type "ip".

          label_selector: Configuration for type LabelSelector, required if type is `label_selector`

          server: Configuration for type Server, required if type is `server`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/load_balancers/{id}/actions/remove_target",
            body=maybe_transform(
                {
                    "type": type,
                    "ip": ip,
                    "label_selector": label_selector,
                    "server": server,
                },
                action_remove_target_params.ActionRemoveTargetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRemoveTargetResponse,
        )

    async def update_service(
        self,
        id: int,
        *,
        destination_port: int,
        health_check: action_update_service_params.HealthCheck,
        listen_port: int,
        protocol: Literal["http", "https", "tcp"],
        proxyprotocol: bool,
        http: action_update_service_params.HTTP | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionUpdateServiceResponse:
        """
        Updates a Load Balancer Service.

        #### Call specific error codes

        | Code                       | Description                                             |
        | -------------------------- | ------------------------------------------------------- |
        | `source_port_already_used` | The source port you are trying to add is already in use |

        Args:
          destination_port: Port the Load Balancer will balance to

          health_check: Service health check

          listen_port: Port the Load Balancer listens on

          protocol: Protocol of the Load Balancer

          proxyprotocol: Is Proxyprotocol enabled or not

          http: Configuration option for protocols http and https

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/load_balancers/{id}/actions/update_service",
            body=maybe_transform(
                {
                    "destination_port": destination_port,
                    "health_check": health_check,
                    "listen_port": listen_port,
                    "protocol": protocol,
                    "proxyprotocol": proxyprotocol,
                    "http": http,
                },
                action_update_service_params.ActionUpdateServiceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionUpdateServiceResponse,
        )
