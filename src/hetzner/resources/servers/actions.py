# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

from ...types import shared_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.servers import (
    ActionListResponse,
    ActionResetResponse,
    ActionRebootResponse,
    ActionPoweronResponse,
    ActionRebuildResponse,
    ActionPoweroffResponse,
    ActionRetrieveResponse,
    ActionShutdownResponse,
    ActionAttachIsoResponse,
    ActionDetachIsoResponse,
    ActionChangeTypeResponse,
    ActionCreateImageResponse,
    ActionChangeDnsPtrResponse,
    ActionEnableBackupResponse,
    ActionEnableRescueResponse,
    ActionDisableBackupResponse,
    ActionDisableRescueResponse,
    ActionResetPasswordResponse,
    ActionChangeAliasIpsResponse,
    ActionRequestConsoleResponse,
    ActionAttachToNetworkResponse,
    ActionChangeProtectionResponse,
    ActionDetachFromNetworkResponse,
    ActionAddToPlacementGroupResponse,
    ActionRemoveFromPlacementGroupResponse,
    action_list_params,
    action_rebuild_params,
    action_attach_iso_params,
    action_change_type_params,
    action_create_image_params,
    action_enable_rescue_params,
    action_change_dns_ptr_params,
    action_change_alias_ips_params,
    action_attach_to_network_params,
    action_change_protection_params,
    action_detach_from_network_params,
    action_add_to_placement_group_params,
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
        Returns a specific Action object for a Server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/servers/{id}/actions/{action_id}",
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
        """Returns all Action objects for a Server.

        You can `sort` the results by using the
        sort URI parameter, and filter them with the `status` parameter.

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
            f"/servers/{id}/actions",
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

    def add_to_placement_group(
        self,
        id: int,
        *,
        placement_group: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionAddToPlacementGroupResponse:
        """
        Adds a Server to a Placement Group.

        Server must be powered off for this command to succeed.

        #### Call specific error codes

        | Code                 | Description                          |
        | -------------------- | ------------------------------------ |
        | `server_not_stopped` | The action requires a stopped server |

        Args:
          placement_group: ID of Placement Group the Server should be added to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/add_to_placement_group",
            body=maybe_transform(
                {"placement_group": placement_group},
                action_add_to_placement_group_params.ActionAddToPlacementGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAddToPlacementGroupResponse,
        )

    def attach_iso(
        self,
        id: int,
        *,
        iso: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionAttachIsoResponse:
        """Attaches an ISO to a Server.

        The Server will immediately see it as a new disk.
        An already attached ISO will automatically be detached before the new ISO is
        attached.

        Servers with attached ISOs have a modified boot order: They will try to boot
        from the ISO first before falling back to hard disk.

        Args:
          iso: ID or name of ISO to attach to the Server as listed in GET `/isos`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/attach_iso",
            body=maybe_transform({"iso": iso}, action_attach_iso_params.ActionAttachIsoParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAttachIsoResponse,
        )

    def attach_to_network(
        self,
        id: int,
        *,
        network: int,
        alias_ips: List[str] | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionAttachToNetworkResponse:
        """Attaches a Server to a network.

        This will complement the fixed public Server
        interface by adding an additional ethernet interface to the Server which is
        connected to the specified network.

        The Server will get an IP auto assigned from a subnet of type `server` in the
        same `network_zone`.

        Using the `alias_ips` attribute you can also define one or more additional IPs
        to the Servers. Please note that you will have to configure these IPs by hand on
        your Server since only the primary IP will be given out by DHCP.

        **Call specific error codes**

        | Code                      | Description                                                    |
        | ------------------------- | -------------------------------------------------------------- |
        | `server_already_attached` | The server is already attached to the network                  |
        | `ip_not_available`        | The provided Network IP is not available                       |
        | `no_subnet_available`     | No Subnet or IP is available for the Server within the network |
        | `networks_overlap`        | The network IP range overlaps with one of the server networks  |

        Args:
          network: ID of an existing network to attach the Server to

          alias_ips: Additional IPs to be assigned to this Server

          ip: IP to request to be assigned to this Server; if you do not provide this then you
              will be auto assigned an IP address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/attach_to_network",
            body=maybe_transform(
                {
                    "network": network,
                    "alias_ips": alias_ips,
                    "ip": ip,
                },
                action_attach_to_network_params.ActionAttachToNetworkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAttachToNetworkResponse,
        )

    def change_alias_ips(
        self,
        id: int,
        *,
        alias_ips: List[str],
        network: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionChangeAliasIpsResponse:
        """Changes the alias IPs of an already attached Network.

        Note that the existing
        aliases for the specified Network will be replaced with these provided in the
        request body. So if you want to add an alias IP, you have to provide the
        existing ones from the Network plus the new alias IP in the request body.

        Args:
          alias_ips: New alias IPs to set for this Server

          network: ID of an existing Network already attached to the Server

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/change_alias_ips",
            body=maybe_transform(
                {
                    "alias_ips": alias_ips,
                    "network": network,
                },
                action_change_alias_ips_params.ActionChangeAliasIpsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeAliasIpsResponse,
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
        Changes the hostname that will appear when getting the hostname belonging to the
        primary IPs (IPv4 and IPv6) of this Server.

        Floating IPs assigned to the Server are not affected by this.

        Args:
          dns_ptr: Hostname to set as a reverse DNS PTR entry, reset to original value if `null`

          ip: Primary IP address for which the reverse DNS entry should be set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/change_dns_ptr",
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
        rebuild: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionChangeProtectionResponse:
        """
        Changes the protection configuration of the Server.

        Args:
          delete: If true, prevents the Server from being deleted (currently delete and rebuild
              attribute needs to have the same value)

          rebuild: If true, prevents the Server from being rebuilt (currently delete and rebuild
              attribute needs to have the same value)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/change_protection",
            body=maybe_transform(
                {
                    "delete": delete,
                    "rebuild": rebuild,
                },
                action_change_protection_params.ActionChangeProtectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeProtectionResponse,
        )

    def change_type(
        self,
        id: int,
        *,
        server_type: str,
        upgrade_disk: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionChangeTypeResponse:
        """
        Changes the type (Cores, RAM and disk sizes) of a Server.

        Server must be powered off for this command to succeed.

        This copies the content of its disk, and starts it again.

        You can only migrate to Server types with the same `storage_type` and equal or
        bigger disks. Shrinking disks is not possible as it might destroy data.

        If the disk gets upgraded, the Server type can not be downgraded any more. If
        you plan to downgrade the Server type, set `upgrade_disk` to `false`.

        #### Call specific error codes

        | Code                  | Description                                                        |
        | --------------------- | ------------------------------------------------------------------ |
        | `invalid_server_type` | The server type does not fit for the given server or is deprecated |
        | `server_not_stopped`  | The action requires a stopped server                               |

        Args:
          server_type: ID or name of Server type the Server should migrate to

          upgrade_disk: If false, do not upgrade the disk (this allows downgrading the Server type
              later)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/change_type",
            body=maybe_transform(
                {
                    "server_type": server_type,
                    "upgrade_disk": upgrade_disk,
                },
                action_change_type_params.ActionChangeTypeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeTypeResponse,
        )

    def create_image(
        self,
        id: int,
        *,
        description: str | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        type: Literal["backup", "snapshot"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionCreateImageResponse:
        """
        Creates an Image (snapshot) from a Server by copying the contents of its disks.
        This creates a snapshot of the current state of the disk and copies it into an
        Image. If the Server is currently running you must make sure that its disk
        content is consistent. Otherwise, the created Image may not be readable.

        To make sure disk content is consistent, we recommend to shut down the Server
        prior to creating an Image.

        You can either create a `backup` Image that is bound to the Server and therefore
        will be deleted when the Server is deleted, or you can create an `snapshot`
        Image which is completely independent of the Server it was created from and will
        survive Server deletion. Backup Images are only available when the backup option
        is enabled for the Server. Snapshot Images are billed on a per GB basis.

        Args:
          description: Description of the Image, will be auto-generated if not set

          labels: User-defined labels (key-value pairs)

          type: Type of Image to create (default: `snapshot`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/create_image",
            body=maybe_transform(
                {
                    "description": description,
                    "labels": labels,
                    "type": type,
                },
                action_create_image_params.ActionCreateImageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionCreateImageResponse,
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
        """Detaches a Server from a network.

        The interface for this network will vanish.

        Args:
          network: ID of an existing network to detach the Server from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/detach_from_network",
            body=maybe_transform({"network": network}, action_detach_from_network_params.ActionDetachFromNetworkParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDetachFromNetworkResponse,
        )

    def detach_iso(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionDetachIsoResponse:
        """Detaches an ISO from a Server.

        In case no ISO Image is attached to the Server,
        the status of the returned Action is immediately set to `success`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/detach_iso",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDetachIsoResponse,
        )

    def disable_backup(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionDisableBackupResponse:
        """
        Disables the automatic backup option and deletes all existing Backups for a
        Server. No more additional charges for backups will be made.

        Caution: This immediately removes all existing backups for the Server!

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/disable_backup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDisableBackupResponse,
        )

    def disable_rescue(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionDisableRescueResponse:
        """Disables the Hetzner Rescue System for a Server.

        This makes a Server start from
        its disks on next reboot.

        Rescue Mode is automatically disabled when you first boot into it or if you do
        not use it for 60 minutes.

        Disabling rescue mode will not reboot your Server — you will have to do this
        yourself.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/disable_rescue",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDisableRescueResponse,
        )

    def enable_backup(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionEnableBackupResponse:
        """
        Enables and configures the automatic daily backup option for the Server.
        Enabling automatic backups will increase the price of the Server by 20%. In
        return, you will get seven slots where Images of type backup can be stored.

        Backups are automatically created daily.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/enable_backup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionEnableBackupResponse,
        )

    def enable_rescue(
        self,
        id: int,
        *,
        ssh_keys: List[int] | NotGiven = NOT_GIVEN,
        type: Literal["linux32", "linux64"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionEnableRescueResponse:
        """Enable the Hetzner Rescue System for this Server.

        The next time a Server with
        enabled rescue mode boots it will start a special minimal Linux distribution
        designed for repair and reinstall.

        In case a Server cannot boot on its own you can use this to access a Server’s
        disks.

        Rescue Mode is automatically disabled when you first boot into it or if you do
        not use it for 60 minutes.

        Enabling rescue mode will not
        [reboot](https://docs.hetzner.cloud/#server-actions-soft-reboot-a-server) your
        Server — you will have to do this yourself.

        Args:
          ssh_keys: Array of SSH key IDs which should be injected into the rescue system.

          type: Type of rescue system to boot (default: `linux64`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/enable_rescue",
            body=maybe_transform(
                {
                    "ssh_keys": ssh_keys,
                    "type": type,
                },
                action_enable_rescue_params.ActionEnableRescueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionEnableRescueResponse,
        )

    def poweroff(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionPoweroffResponse:
        """Cuts power to the Server.

        This forcefully stops it without giving the Server
        operating system time to gracefully stop. May lead to data loss, equivalent to
        pulling the power cord. Power off should only be used when shutdown does not
        work.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/poweroff",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionPoweroffResponse,
        )

    def poweron(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionPoweronResponse:
        """
        Starts a Server by turning its power on.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/poweron",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionPoweronResponse,
        )

    def reboot(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionRebootResponse:
        """Reboots a Server gracefully by sending an ACPI request.

        The Server operating
        system must support ACPI and react to the request, otherwise the Server will not
        reboot.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/reboot",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRebootResponse,
        )

    def rebuild(
        self,
        id: int,
        *,
        image: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionRebuildResponse:
        """
        Rebuilds a Server overwriting its disk with the content of an Image, thereby
        **destroying all data** on the target Server

        The Image can either be one you have created earlier (`backup` or `snapshot`
        Image) or it can be a completely fresh `system` Image provided by us. You can
        get a list of all available Images with `GET /images`.

        Your Server will automatically be powered off before the rebuild command
        executes.

        Args:
          image: ID or name of Image to rebuilt from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/rebuild",
            body=maybe_transform({"image": image}, action_rebuild_params.ActionRebuildParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRebuildResponse,
        )

    def remove_from_placement_group(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionRemoveFromPlacementGroupResponse:
        """
        Removes a Server from a Placement Group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/remove_from_placement_group",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRemoveFromPlacementGroupResponse,
        )

    def request_console(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionRequestConsoleResponse:
        """
        Requests credentials for remote access via VNC over websocket to keyboard,
        monitor, and mouse for a Server. The provided URL is valid for 1 minute, after
        this period a new url needs to be created to connect to the Server. How long the
        connection is open after the initial connect is not subject to this timeout.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/request_console",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRequestConsoleResponse,
        )

    def reset(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionResetResponse:
        """Cuts power to a Server and starts it again.

        This forcefully stops it without
        giving the Server operating system time to gracefully stop. This may lead to
        data loss, it’s equivalent to pulling the power cord and plugging it in again.
        Reset should only be used when reboot does not work.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/reset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResetResponse,
        )

    def reset_password(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionResetPasswordResponse:
        """Resets the root password.

        Only works for Linux systems that are running the qemu
        guest agent. Server must be powered on (status `running`) in order for this
        operation to succeed.

        This will generate a new password for this Server and return it.

        If this does not succeed you can use the rescue system to netboot the Server and
        manually change your Server password by hand.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/reset_password",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResetPasswordResponse,
        )

    def shutdown(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionShutdownResponse:
        """Shuts down a Server gracefully by sending an ACPI shutdown request.

        The Server
        operating system must support ACPI and react to the request, otherwise the
        Server will not shut down. Please note that the `action` status in this case
        only reflects whether the action was sent to the server. It does not mean that
        the server actually shut down successfully. If you need to ensure that the
        server is off, use the `poweroff` action

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/servers/{id}/actions/shutdown",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionShutdownResponse,
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
        Returns a specific Action object for a Server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/servers/{id}/actions/{action_id}",
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
        """Returns all Action objects for a Server.

        You can `sort` the results by using the
        sort URI parameter, and filter them with the `status` parameter.

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
            f"/servers/{id}/actions",
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

    async def add_to_placement_group(
        self,
        id: int,
        *,
        placement_group: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionAddToPlacementGroupResponse:
        """
        Adds a Server to a Placement Group.

        Server must be powered off for this command to succeed.

        #### Call specific error codes

        | Code                 | Description                          |
        | -------------------- | ------------------------------------ |
        | `server_not_stopped` | The action requires a stopped server |

        Args:
          placement_group: ID of Placement Group the Server should be added to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/add_to_placement_group",
            body=maybe_transform(
                {"placement_group": placement_group},
                action_add_to_placement_group_params.ActionAddToPlacementGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAddToPlacementGroupResponse,
        )

    async def attach_iso(
        self,
        id: int,
        *,
        iso: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionAttachIsoResponse:
        """Attaches an ISO to a Server.

        The Server will immediately see it as a new disk.
        An already attached ISO will automatically be detached before the new ISO is
        attached.

        Servers with attached ISOs have a modified boot order: They will try to boot
        from the ISO first before falling back to hard disk.

        Args:
          iso: ID or name of ISO to attach to the Server as listed in GET `/isos`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/attach_iso",
            body=maybe_transform({"iso": iso}, action_attach_iso_params.ActionAttachIsoParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAttachIsoResponse,
        )

    async def attach_to_network(
        self,
        id: int,
        *,
        network: int,
        alias_ips: List[str] | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionAttachToNetworkResponse:
        """Attaches a Server to a network.

        This will complement the fixed public Server
        interface by adding an additional ethernet interface to the Server which is
        connected to the specified network.

        The Server will get an IP auto assigned from a subnet of type `server` in the
        same `network_zone`.

        Using the `alias_ips` attribute you can also define one or more additional IPs
        to the Servers. Please note that you will have to configure these IPs by hand on
        your Server since only the primary IP will be given out by DHCP.

        **Call specific error codes**

        | Code                      | Description                                                    |
        | ------------------------- | -------------------------------------------------------------- |
        | `server_already_attached` | The server is already attached to the network                  |
        | `ip_not_available`        | The provided Network IP is not available                       |
        | `no_subnet_available`     | No Subnet or IP is available for the Server within the network |
        | `networks_overlap`        | The network IP range overlaps with one of the server networks  |

        Args:
          network: ID of an existing network to attach the Server to

          alias_ips: Additional IPs to be assigned to this Server

          ip: IP to request to be assigned to this Server; if you do not provide this then you
              will be auto assigned an IP address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/attach_to_network",
            body=maybe_transform(
                {
                    "network": network,
                    "alias_ips": alias_ips,
                    "ip": ip,
                },
                action_attach_to_network_params.ActionAttachToNetworkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAttachToNetworkResponse,
        )

    async def change_alias_ips(
        self,
        id: int,
        *,
        alias_ips: List[str],
        network: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionChangeAliasIpsResponse:
        """Changes the alias IPs of an already attached Network.

        Note that the existing
        aliases for the specified Network will be replaced with these provided in the
        request body. So if you want to add an alias IP, you have to provide the
        existing ones from the Network plus the new alias IP in the request body.

        Args:
          alias_ips: New alias IPs to set for this Server

          network: ID of an existing Network already attached to the Server

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/change_alias_ips",
            body=maybe_transform(
                {
                    "alias_ips": alias_ips,
                    "network": network,
                },
                action_change_alias_ips_params.ActionChangeAliasIpsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeAliasIpsResponse,
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
        Changes the hostname that will appear when getting the hostname belonging to the
        primary IPs (IPv4 and IPv6) of this Server.

        Floating IPs assigned to the Server are not affected by this.

        Args:
          dns_ptr: Hostname to set as a reverse DNS PTR entry, reset to original value if `null`

          ip: Primary IP address for which the reverse DNS entry should be set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/change_dns_ptr",
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
        rebuild: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionChangeProtectionResponse:
        """
        Changes the protection configuration of the Server.

        Args:
          delete: If true, prevents the Server from being deleted (currently delete and rebuild
              attribute needs to have the same value)

          rebuild: If true, prevents the Server from being rebuilt (currently delete and rebuild
              attribute needs to have the same value)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/change_protection",
            body=maybe_transform(
                {
                    "delete": delete,
                    "rebuild": rebuild,
                },
                action_change_protection_params.ActionChangeProtectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeProtectionResponse,
        )

    async def change_type(
        self,
        id: int,
        *,
        server_type: str,
        upgrade_disk: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionChangeTypeResponse:
        """
        Changes the type (Cores, RAM and disk sizes) of a Server.

        Server must be powered off for this command to succeed.

        This copies the content of its disk, and starts it again.

        You can only migrate to Server types with the same `storage_type` and equal or
        bigger disks. Shrinking disks is not possible as it might destroy data.

        If the disk gets upgraded, the Server type can not be downgraded any more. If
        you plan to downgrade the Server type, set `upgrade_disk` to `false`.

        #### Call specific error codes

        | Code                  | Description                                                        |
        | --------------------- | ------------------------------------------------------------------ |
        | `invalid_server_type` | The server type does not fit for the given server or is deprecated |
        | `server_not_stopped`  | The action requires a stopped server                               |

        Args:
          server_type: ID or name of Server type the Server should migrate to

          upgrade_disk: If false, do not upgrade the disk (this allows downgrading the Server type
              later)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/change_type",
            body=maybe_transform(
                {
                    "server_type": server_type,
                    "upgrade_disk": upgrade_disk,
                },
                action_change_type_params.ActionChangeTypeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeTypeResponse,
        )

    async def create_image(
        self,
        id: int,
        *,
        description: str | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        type: Literal["backup", "snapshot"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionCreateImageResponse:
        """
        Creates an Image (snapshot) from a Server by copying the contents of its disks.
        This creates a snapshot of the current state of the disk and copies it into an
        Image. If the Server is currently running you must make sure that its disk
        content is consistent. Otherwise, the created Image may not be readable.

        To make sure disk content is consistent, we recommend to shut down the Server
        prior to creating an Image.

        You can either create a `backup` Image that is bound to the Server and therefore
        will be deleted when the Server is deleted, or you can create an `snapshot`
        Image which is completely independent of the Server it was created from and will
        survive Server deletion. Backup Images are only available when the backup option
        is enabled for the Server. Snapshot Images are billed on a per GB basis.

        Args:
          description: Description of the Image, will be auto-generated if not set

          labels: User-defined labels (key-value pairs)

          type: Type of Image to create (default: `snapshot`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/create_image",
            body=maybe_transform(
                {
                    "description": description,
                    "labels": labels,
                    "type": type,
                },
                action_create_image_params.ActionCreateImageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionCreateImageResponse,
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
        """Detaches a Server from a network.

        The interface for this network will vanish.

        Args:
          network: ID of an existing network to detach the Server from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/detach_from_network",
            body=maybe_transform({"network": network}, action_detach_from_network_params.ActionDetachFromNetworkParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDetachFromNetworkResponse,
        )

    async def detach_iso(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionDetachIsoResponse:
        """Detaches an ISO from a Server.

        In case no ISO Image is attached to the Server,
        the status of the returned Action is immediately set to `success`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/detach_iso",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDetachIsoResponse,
        )

    async def disable_backup(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionDisableBackupResponse:
        """
        Disables the automatic backup option and deletes all existing Backups for a
        Server. No more additional charges for backups will be made.

        Caution: This immediately removes all existing backups for the Server!

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/disable_backup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDisableBackupResponse,
        )

    async def disable_rescue(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionDisableRescueResponse:
        """Disables the Hetzner Rescue System for a Server.

        This makes a Server start from
        its disks on next reboot.

        Rescue Mode is automatically disabled when you first boot into it or if you do
        not use it for 60 minutes.

        Disabling rescue mode will not reboot your Server — you will have to do this
        yourself.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/disable_rescue",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionDisableRescueResponse,
        )

    async def enable_backup(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionEnableBackupResponse:
        """
        Enables and configures the automatic daily backup option for the Server.
        Enabling automatic backups will increase the price of the Server by 20%. In
        return, you will get seven slots where Images of type backup can be stored.

        Backups are automatically created daily.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/enable_backup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionEnableBackupResponse,
        )

    async def enable_rescue(
        self,
        id: int,
        *,
        ssh_keys: List[int] | NotGiven = NOT_GIVEN,
        type: Literal["linux32", "linux64"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionEnableRescueResponse:
        """Enable the Hetzner Rescue System for this Server.

        The next time a Server with
        enabled rescue mode boots it will start a special minimal Linux distribution
        designed for repair and reinstall.

        In case a Server cannot boot on its own you can use this to access a Server’s
        disks.

        Rescue Mode is automatically disabled when you first boot into it or if you do
        not use it for 60 minutes.

        Enabling rescue mode will not
        [reboot](https://docs.hetzner.cloud/#server-actions-soft-reboot-a-server) your
        Server — you will have to do this yourself.

        Args:
          ssh_keys: Array of SSH key IDs which should be injected into the rescue system.

          type: Type of rescue system to boot (default: `linux64`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/enable_rescue",
            body=maybe_transform(
                {
                    "ssh_keys": ssh_keys,
                    "type": type,
                },
                action_enable_rescue_params.ActionEnableRescueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionEnableRescueResponse,
        )

    async def poweroff(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionPoweroffResponse:
        """Cuts power to the Server.

        This forcefully stops it without giving the Server
        operating system time to gracefully stop. May lead to data loss, equivalent to
        pulling the power cord. Power off should only be used when shutdown does not
        work.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/poweroff",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionPoweroffResponse,
        )

    async def poweron(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionPoweronResponse:
        """
        Starts a Server by turning its power on.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/poweron",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionPoweronResponse,
        )

    async def reboot(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionRebootResponse:
        """Reboots a Server gracefully by sending an ACPI request.

        The Server operating
        system must support ACPI and react to the request, otherwise the Server will not
        reboot.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/reboot",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRebootResponse,
        )

    async def rebuild(
        self,
        id: int,
        *,
        image: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionRebuildResponse:
        """
        Rebuilds a Server overwriting its disk with the content of an Image, thereby
        **destroying all data** on the target Server

        The Image can either be one you have created earlier (`backup` or `snapshot`
        Image) or it can be a completely fresh `system` Image provided by us. You can
        get a list of all available Images with `GET /images`.

        Your Server will automatically be powered off before the rebuild command
        executes.

        Args:
          image: ID or name of Image to rebuilt from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/rebuild",
            body=maybe_transform({"image": image}, action_rebuild_params.ActionRebuildParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRebuildResponse,
        )

    async def remove_from_placement_group(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionRemoveFromPlacementGroupResponse:
        """
        Removes a Server from a Placement Group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/remove_from_placement_group",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRemoveFromPlacementGroupResponse,
        )

    async def request_console(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionRequestConsoleResponse:
        """
        Requests credentials for remote access via VNC over websocket to keyboard,
        monitor, and mouse for a Server. The provided URL is valid for 1 minute, after
        this period a new url needs to be created to connect to the Server. How long the
        connection is open after the initial connect is not subject to this timeout.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/request_console",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRequestConsoleResponse,
        )

    async def reset(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionResetResponse:
        """Cuts power to a Server and starts it again.

        This forcefully stops it without
        giving the Server operating system time to gracefully stop. This may lead to
        data loss, it’s equivalent to pulling the power cord and plugging it in again.
        Reset should only be used when reboot does not work.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/reset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResetResponse,
        )

    async def reset_password(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionResetPasswordResponse:
        """Resets the root password.

        Only works for Linux systems that are running the qemu
        guest agent. Server must be powered on (status `running`) in order for this
        operation to succeed.

        This will generate a new password for this Server and return it.

        If this does not succeed you can use the rescue system to netboot the Server and
        manually change your Server password by hand.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/reset_password",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResetPasswordResponse,
        )

    async def shutdown(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionShutdownResponse:
        """Shuts down a Server gracefully by sending an ACPI shutdown request.

        The Server
        operating system must support ACPI and react to the request, otherwise the
        Server will not shut down. Please note that the `action` status in this case
        only reflects whether the action was sent to the server. It does not mean that
        the server actually shut down successfully. If you need to ensure that the
        server is off, use the `poweroff` action

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/servers/{id}/actions/shutdown",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionShutdownResponse,
        )
