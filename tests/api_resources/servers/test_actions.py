# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from hetzner import Hetzner, AsyncHetzner
from tests.utils import assert_matches_type
from hetzner.types.servers import (
    ActionListResponse,
    ActionResetResponse,
    ActionRebootResponse,
    ActionPoweronResponse,
    ActionRebuildResponse,
    ActionPoweroffResponse,
    ActionRetrieveResponse,
    ActionShutdownResponse,
    ActionAttachISOResponse,
    ActionDetachISOResponse,
    ActionChangeTypeResponse,
    ActionCreateImageResponse,
    ActionChangeDNSPtrResponse,
    ActionEnableBackupResponse,
    ActionEnableRescueResponse,
    ActionDisableBackupResponse,
    ActionDisableRescueResponse,
    ActionResetPasswordResponse,
    ActionChangeAliasIPsResponse,
    ActionRequestConsoleResponse,
    ActionAttachToNetworkResponse,
    ActionChangeProtectionResponse,
    ActionDetachFromNetworkResponse,
    ActionAddToPlacementGroupResponse,
    ActionRemoveFromPlacementGroupResponse,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_token = os.environ.get("API_KEY", "something1234")


class TestActions:
    strict_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Hetzner) -> None:
        action = client.servers.actions.retrieve(
            0,
            id=0,
        )
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @parametrize
    def test_method_list(self, client: Hetzner) -> None:
        action = client.servers.actions.list(
            0,
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hetzner) -> None:
        action = client.servers.actions.list(
            0,
            page=1,
            per_page=1,
            sort="id",
            status="running",
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    def test_method_add_to_placement_group(self, client: Hetzner) -> None:
        action = client.servers.actions.add_to_placement_group(
            0,
            placement_group=1,
        )
        assert_matches_type(ActionAddToPlacementGroupResponse, action, path=["response"])

    @parametrize
    def test_method_attach_iso(self, client: Hetzner) -> None:
        action = client.servers.actions.attach_iso(
            0,
            iso="FreeBSD-11.0-RELEASE-amd64-dvd1",
        )
        assert_matches_type(ActionAttachISOResponse, action, path=["response"])

    @parametrize
    def test_method_attach_to_network(self, client: Hetzner) -> None:
        action = client.servers.actions.attach_to_network(
            0,
            network=4711,
        )
        assert_matches_type(ActionAttachToNetworkResponse, action, path=["response"])

    @parametrize
    def test_method_attach_to_network_with_all_params(self, client: Hetzner) -> None:
        action = client.servers.actions.attach_to_network(
            0,
            network=4711,
            alias_ips=["string", "string", "string"],
            ip="10.0.1.1",
        )
        assert_matches_type(ActionAttachToNetworkResponse, action, path=["response"])

    @parametrize
    def test_method_change_alias_ips(self, client: Hetzner) -> None:
        action = client.servers.actions.change_alias_ips(
            0,
            alias_ips=["string", "string", "string"],
            network=4711,
        )
        assert_matches_type(ActionChangeAliasIPsResponse, action, path=["response"])

    @parametrize
    def test_method_change_dns_ptr(self, client: Hetzner) -> None:
        action = client.servers.actions.change_dns_ptr(
            0,
            dns_ptr="server01.example.com",
            ip="1.2.3.4",
        )
        assert_matches_type(ActionChangeDNSPtrResponse, action, path=["response"])

    @parametrize
    def test_method_change_protection(self, client: Hetzner) -> None:
        action = client.servers.actions.change_protection(
            0,
        )
        assert_matches_type(ActionChangeProtectionResponse, action, path=["response"])

    @parametrize
    def test_method_change_protection_with_all_params(self, client: Hetzner) -> None:
        action = client.servers.actions.change_protection(
            0,
            delete=True,
            rebuild=True,
        )
        assert_matches_type(ActionChangeProtectionResponse, action, path=["response"])

    @parametrize
    def test_method_change_type(self, client: Hetzner) -> None:
        action = client.servers.actions.change_type(
            0,
            server_type="cx11",
            upgrade_disk=True,
        )
        assert_matches_type(ActionChangeTypeResponse, action, path=["response"])

    @parametrize
    def test_method_create_image(self, client: Hetzner) -> None:
        action = client.servers.actions.create_image(
            0,
        )
        assert_matches_type(ActionCreateImageResponse, action, path=["response"])

    @parametrize
    def test_method_create_image_with_all_params(self, client: Hetzner) -> None:
        action = client.servers.actions.create_image(
            0,
            description="my image",
            labels={"foo": "string"},
            type="snapshot",
        )
        assert_matches_type(ActionCreateImageResponse, action, path=["response"])

    @parametrize
    def test_method_detach_from_network(self, client: Hetzner) -> None:
        action = client.servers.actions.detach_from_network(
            0,
            network=4711,
        )
        assert_matches_type(ActionDetachFromNetworkResponse, action, path=["response"])

    @parametrize
    def test_method_detach_iso(self, client: Hetzner) -> None:
        action = client.servers.actions.detach_iso(
            0,
        )
        assert_matches_type(ActionDetachISOResponse, action, path=["response"])

    @parametrize
    def test_method_disable_backup(self, client: Hetzner) -> None:
        action = client.servers.actions.disable_backup(
            0,
        )
        assert_matches_type(ActionDisableBackupResponse, action, path=["response"])

    @parametrize
    def test_method_disable_rescue(self, client: Hetzner) -> None:
        action = client.servers.actions.disable_rescue(
            0,
        )
        assert_matches_type(ActionDisableRescueResponse, action, path=["response"])

    @parametrize
    def test_method_enable_backup(self, client: Hetzner) -> None:
        action = client.servers.actions.enable_backup(
            0,
        )
        assert_matches_type(ActionEnableBackupResponse, action, path=["response"])

    @parametrize
    def test_method_enable_rescue(self, client: Hetzner) -> None:
        action = client.servers.actions.enable_rescue(
            0,
        )
        assert_matches_type(ActionEnableRescueResponse, action, path=["response"])

    @parametrize
    def test_method_enable_rescue_with_all_params(self, client: Hetzner) -> None:
        action = client.servers.actions.enable_rescue(
            0,
            ssh_keys=[0, 0, 0],
            type="linux32",
        )
        assert_matches_type(ActionEnableRescueResponse, action, path=["response"])

    @parametrize
    def test_method_poweroff(self, client: Hetzner) -> None:
        action = client.servers.actions.poweroff(
            0,
        )
        assert_matches_type(ActionPoweroffResponse, action, path=["response"])

    @parametrize
    def test_method_poweron(self, client: Hetzner) -> None:
        action = client.servers.actions.poweron(
            0,
        )
        assert_matches_type(ActionPoweronResponse, action, path=["response"])

    @parametrize
    def test_method_reboot(self, client: Hetzner) -> None:
        action = client.servers.actions.reboot(
            0,
        )
        assert_matches_type(ActionRebootResponse, action, path=["response"])

    @parametrize
    def test_method_rebuild(self, client: Hetzner) -> None:
        action = client.servers.actions.rebuild(
            0,
            image="ubuntu-20.04",
        )
        assert_matches_type(ActionRebuildResponse, action, path=["response"])

    @parametrize
    def test_method_remove_from_placement_group(self, client: Hetzner) -> None:
        action = client.servers.actions.remove_from_placement_group(
            0,
        )
        assert_matches_type(ActionRemoveFromPlacementGroupResponse, action, path=["response"])

    @parametrize
    def test_method_request_console(self, client: Hetzner) -> None:
        action = client.servers.actions.request_console(
            0,
        )
        assert_matches_type(ActionRequestConsoleResponse, action, path=["response"])

    @parametrize
    def test_method_reset(self, client: Hetzner) -> None:
        action = client.servers.actions.reset(
            0,
        )
        assert_matches_type(ActionResetResponse, action, path=["response"])

    @parametrize
    def test_method_reset_password(self, client: Hetzner) -> None:
        action = client.servers.actions.reset_password(
            0,
        )
        assert_matches_type(ActionResetPasswordResponse, action, path=["response"])

    @parametrize
    def test_method_shutdown(self, client: Hetzner) -> None:
        action = client.servers.actions.shutdown(
            0,
        )
        assert_matches_type(ActionShutdownResponse, action, path=["response"])


class TestAsyncActions:
    strict_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.retrieve(
            0,
            id=0,
        )
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.list(
            0,
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.list(
            0,
            page=1,
            per_page=1,
            sort="id",
            status="running",
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    async def test_method_add_to_placement_group(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.add_to_placement_group(
            0,
            placement_group=1,
        )
        assert_matches_type(ActionAddToPlacementGroupResponse, action, path=["response"])

    @parametrize
    async def test_method_attach_iso(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.attach_iso(
            0,
            iso="FreeBSD-11.0-RELEASE-amd64-dvd1",
        )
        assert_matches_type(ActionAttachISOResponse, action, path=["response"])

    @parametrize
    async def test_method_attach_to_network(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.attach_to_network(
            0,
            network=4711,
        )
        assert_matches_type(ActionAttachToNetworkResponse, action, path=["response"])

    @parametrize
    async def test_method_attach_to_network_with_all_params(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.attach_to_network(
            0,
            network=4711,
            alias_ips=["string", "string", "string"],
            ip="10.0.1.1",
        )
        assert_matches_type(ActionAttachToNetworkResponse, action, path=["response"])

    @parametrize
    async def test_method_change_alias_ips(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.change_alias_ips(
            0,
            alias_ips=["string", "string", "string"],
            network=4711,
        )
        assert_matches_type(ActionChangeAliasIPsResponse, action, path=["response"])

    @parametrize
    async def test_method_change_dns_ptr(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.change_dns_ptr(
            0,
            dns_ptr="server01.example.com",
            ip="1.2.3.4",
        )
        assert_matches_type(ActionChangeDNSPtrResponse, action, path=["response"])

    @parametrize
    async def test_method_change_protection(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.change_protection(
            0,
        )
        assert_matches_type(ActionChangeProtectionResponse, action, path=["response"])

    @parametrize
    async def test_method_change_protection_with_all_params(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.change_protection(
            0,
            delete=True,
            rebuild=True,
        )
        assert_matches_type(ActionChangeProtectionResponse, action, path=["response"])

    @parametrize
    async def test_method_change_type(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.change_type(
            0,
            server_type="cx11",
            upgrade_disk=True,
        )
        assert_matches_type(ActionChangeTypeResponse, action, path=["response"])

    @parametrize
    async def test_method_create_image(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.create_image(
            0,
        )
        assert_matches_type(ActionCreateImageResponse, action, path=["response"])

    @parametrize
    async def test_method_create_image_with_all_params(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.create_image(
            0,
            description="my image",
            labels={"foo": "string"},
            type="snapshot",
        )
        assert_matches_type(ActionCreateImageResponse, action, path=["response"])

    @parametrize
    async def test_method_detach_from_network(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.detach_from_network(
            0,
            network=4711,
        )
        assert_matches_type(ActionDetachFromNetworkResponse, action, path=["response"])

    @parametrize
    async def test_method_detach_iso(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.detach_iso(
            0,
        )
        assert_matches_type(ActionDetachISOResponse, action, path=["response"])

    @parametrize
    async def test_method_disable_backup(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.disable_backup(
            0,
        )
        assert_matches_type(ActionDisableBackupResponse, action, path=["response"])

    @parametrize
    async def test_method_disable_rescue(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.disable_rescue(
            0,
        )
        assert_matches_type(ActionDisableRescueResponse, action, path=["response"])

    @parametrize
    async def test_method_enable_backup(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.enable_backup(
            0,
        )
        assert_matches_type(ActionEnableBackupResponse, action, path=["response"])

    @parametrize
    async def test_method_enable_rescue(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.enable_rescue(
            0,
        )
        assert_matches_type(ActionEnableRescueResponse, action, path=["response"])

    @parametrize
    async def test_method_enable_rescue_with_all_params(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.enable_rescue(
            0,
            ssh_keys=[0, 0, 0],
            type="linux32",
        )
        assert_matches_type(ActionEnableRescueResponse, action, path=["response"])

    @parametrize
    async def test_method_poweroff(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.poweroff(
            0,
        )
        assert_matches_type(ActionPoweroffResponse, action, path=["response"])

    @parametrize
    async def test_method_poweron(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.poweron(
            0,
        )
        assert_matches_type(ActionPoweronResponse, action, path=["response"])

    @parametrize
    async def test_method_reboot(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.reboot(
            0,
        )
        assert_matches_type(ActionRebootResponse, action, path=["response"])

    @parametrize
    async def test_method_rebuild(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.rebuild(
            0,
            image="ubuntu-20.04",
        )
        assert_matches_type(ActionRebuildResponse, action, path=["response"])

    @parametrize
    async def test_method_remove_from_placement_group(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.remove_from_placement_group(
            0,
        )
        assert_matches_type(ActionRemoveFromPlacementGroupResponse, action, path=["response"])

    @parametrize
    async def test_method_request_console(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.request_console(
            0,
        )
        assert_matches_type(ActionRequestConsoleResponse, action, path=["response"])

    @parametrize
    async def test_method_reset(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.reset(
            0,
        )
        assert_matches_type(ActionResetResponse, action, path=["response"])

    @parametrize
    async def test_method_reset_password(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.reset_password(
            0,
        )
        assert_matches_type(ActionResetPasswordResponse, action, path=["response"])

    @parametrize
    async def test_method_shutdown(self, client: AsyncHetzner) -> None:
        action = await client.servers.actions.shutdown(
            0,
        )
        assert_matches_type(ActionShutdownResponse, action, path=["response"])
