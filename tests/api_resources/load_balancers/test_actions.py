# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from hetzner import Hetzner, AsyncHetzner
from tests.utils import assert_matches_type
from hetzner.types.load_balancers import (
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
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_token = os.environ.get("API_KEY", "something1234")


class TestActions:
    strict_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.retrieve(
            0,
            id=0,
        )
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @parametrize
    def test_method_list(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.list(
            0,
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.list(
            0,
            page=1,
            per_page=1,
            sort="id",
            status="running",
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    def test_method_add_service(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.add_service(
            0,
            destination_port=80,
            health_check={
                "interval": 15,
                "port": 4711,
                "protocol": "http",
                "retries": 3,
                "timeout": 10,
            },
            listen_port=443,
            protocol="https",
            proxyprotocol=False,
        )
        assert_matches_type(ActionAddServiceResponse, action, path=["response"])

    @parametrize
    def test_method_add_service_with_all_params(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.add_service(
            0,
            destination_port=80,
            health_check={
                "http": {
                    "domain": "example.com",
                    "path": "/",
                    "response": '{"status": "ok"}',
                    "status_codes": ["string", "string", "string"],
                    "tls": False,
                },
                "interval": 15,
                "port": 4711,
                "protocol": "http",
                "retries": 3,
                "timeout": 10,
            },
            listen_port=443,
            protocol="https",
            proxyprotocol=False,
            http={
                "certificates": [0, 0, 0],
                "cookie_lifetime": 300,
                "cookie_name": "HCLBSTICKY",
                "redirect_http": True,
                "sticky_sessions": True,
            },
        )
        assert_matches_type(ActionAddServiceResponse, action, path=["response"])

    @parametrize
    def test_method_ass_target(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.ass_target(
            0,
            type="ip",
        )
        assert_matches_type(ActionAssTargetResponse, action, path=["response"])

    @parametrize
    def test_method_ass_target_with_all_params(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.ass_target(
            0,
            type="ip",
            ip={"ip": "203.0.113.1"},
            label_selector={"selector": "env=prod"},
            server={"id": 80},
            use_private_ip=True,
        )
        assert_matches_type(ActionAssTargetResponse, action, path=["response"])

    @parametrize
    def test_method_attach_to_network(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.attach_to_network(
            0,
            network=4711,
        )
        assert_matches_type(ActionAttachToNetworkResponse, action, path=["response"])

    @parametrize
    def test_method_attach_to_network_with_all_params(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.attach_to_network(
            0,
            network=4711,
            ip="10.0.1.1",
        )
        assert_matches_type(ActionAttachToNetworkResponse, action, path=["response"])

    @parametrize
    def test_method_change_algorithm(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.change_algorithm(
            0,
            type="least_connections",
        )
        assert_matches_type(ActionChangeAlgorithmResponse, action, path=["response"])

    @parametrize
    def test_method_change_dns_ptr(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.change_dns_ptr(
            0,
            dns_ptr="lb1.example.com",
            ip="1.2.3.4",
        )
        assert_matches_type(ActionChangeDNSPtrResponse, action, path=["response"])

    @parametrize
    def test_method_change_protection(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.change_protection(
            0,
        )
        assert_matches_type(ActionChangeProtectionResponse, action, path=["response"])

    @parametrize
    def test_method_change_protection_with_all_params(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.change_protection(
            0,
            delete=True,
        )
        assert_matches_type(ActionChangeProtectionResponse, action, path=["response"])

    @parametrize
    def test_method_change_type(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.change_type(
            0,
            load_balancer_type="lb21",
        )
        assert_matches_type(ActionChangeTypeResponse, action, path=["response"])

    @parametrize
    def test_method_delete_service(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.delete_service(
            0,
            listen_port=4711,
        )
        assert_matches_type(ActionDeleteServiceResponse, action, path=["response"])

    @parametrize
    def test_method_detach_from_network(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.detach_from_network(
            0,
            network=4711,
        )
        assert_matches_type(ActionDetachFromNetworkResponse, action, path=["response"])

    @parametrize
    def test_method_disable_public_interface(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.disable_public_interface(
            0,
        )
        assert_matches_type(ActionDisablePublicInterfaceResponse, action, path=["response"])

    @parametrize
    def test_method_enable_public_interface(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.enable_public_interface(
            0,
        )
        assert_matches_type(ActionEnablePublicInterfaceResponse, action, path=["response"])

    @parametrize
    def test_method_remove_target(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.remove_target(
            0,
            type="ip",
        )
        assert_matches_type(ActionRemoveTargetResponse, action, path=["response"])

    @parametrize
    def test_method_remove_target_with_all_params(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.remove_target(
            0,
            type="ip",
            ip={"ip": "203.0.113.1"},
            label_selector={"selector": "env=prod"},
            server={"id": 80},
        )
        assert_matches_type(ActionRemoveTargetResponse, action, path=["response"])

    @parametrize
    def test_method_update_service(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.update_service(
            0,
            destination_port=80,
            health_check={
                "interval": 15,
                "port": 4711,
                "protocol": "http",
                "retries": 3,
                "timeout": 10,
            },
            listen_port=443,
            protocol="https",
            proxyprotocol=False,
        )
        assert_matches_type(ActionUpdateServiceResponse, action, path=["response"])

    @parametrize
    def test_method_update_service_with_all_params(self, client: Hetzner) -> None:
        action = client.load_balancers.actions.update_service(
            0,
            destination_port=80,
            health_check={
                "http": {
                    "domain": "example.com",
                    "path": "/",
                    "response": '{"status": "ok"}',
                    "status_codes": ["string", "string", "string"],
                    "tls": False,
                },
                "interval": 15,
                "port": 4711,
                "protocol": "http",
                "retries": 3,
                "timeout": 10,
            },
            listen_port=443,
            protocol="https",
            proxyprotocol=False,
            http={
                "certificates": [0, 0, 0],
                "cookie_lifetime": 300,
                "cookie_name": "HCLBSTICKY",
                "redirect_http": True,
                "sticky_sessions": True,
            },
        )
        assert_matches_type(ActionUpdateServiceResponse, action, path=["response"])


class TestAsyncActions:
    strict_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.retrieve(
            0,
            id=0,
        )
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.list(
            0,
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.list(
            0,
            page=1,
            per_page=1,
            sort="id",
            status="running",
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    async def test_method_add_service(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.add_service(
            0,
            destination_port=80,
            health_check={
                "interval": 15,
                "port": 4711,
                "protocol": "http",
                "retries": 3,
                "timeout": 10,
            },
            listen_port=443,
            protocol="https",
            proxyprotocol=False,
        )
        assert_matches_type(ActionAddServiceResponse, action, path=["response"])

    @parametrize
    async def test_method_add_service_with_all_params(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.add_service(
            0,
            destination_port=80,
            health_check={
                "http": {
                    "domain": "example.com",
                    "path": "/",
                    "response": '{"status": "ok"}',
                    "status_codes": ["string", "string", "string"],
                    "tls": False,
                },
                "interval": 15,
                "port": 4711,
                "protocol": "http",
                "retries": 3,
                "timeout": 10,
            },
            listen_port=443,
            protocol="https",
            proxyprotocol=False,
            http={
                "certificates": [0, 0, 0],
                "cookie_lifetime": 300,
                "cookie_name": "HCLBSTICKY",
                "redirect_http": True,
                "sticky_sessions": True,
            },
        )
        assert_matches_type(ActionAddServiceResponse, action, path=["response"])

    @parametrize
    async def test_method_ass_target(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.ass_target(
            0,
            type="ip",
        )
        assert_matches_type(ActionAssTargetResponse, action, path=["response"])

    @parametrize
    async def test_method_ass_target_with_all_params(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.ass_target(
            0,
            type="ip",
            ip={"ip": "203.0.113.1"},
            label_selector={"selector": "env=prod"},
            server={"id": 80},
            use_private_ip=True,
        )
        assert_matches_type(ActionAssTargetResponse, action, path=["response"])

    @parametrize
    async def test_method_attach_to_network(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.attach_to_network(
            0,
            network=4711,
        )
        assert_matches_type(ActionAttachToNetworkResponse, action, path=["response"])

    @parametrize
    async def test_method_attach_to_network_with_all_params(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.attach_to_network(
            0,
            network=4711,
            ip="10.0.1.1",
        )
        assert_matches_type(ActionAttachToNetworkResponse, action, path=["response"])

    @parametrize
    async def test_method_change_algorithm(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.change_algorithm(
            0,
            type="least_connections",
        )
        assert_matches_type(ActionChangeAlgorithmResponse, action, path=["response"])

    @parametrize
    async def test_method_change_dns_ptr(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.change_dns_ptr(
            0,
            dns_ptr="lb1.example.com",
            ip="1.2.3.4",
        )
        assert_matches_type(ActionChangeDNSPtrResponse, action, path=["response"])

    @parametrize
    async def test_method_change_protection(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.change_protection(
            0,
        )
        assert_matches_type(ActionChangeProtectionResponse, action, path=["response"])

    @parametrize
    async def test_method_change_protection_with_all_params(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.change_protection(
            0,
            delete=True,
        )
        assert_matches_type(ActionChangeProtectionResponse, action, path=["response"])

    @parametrize
    async def test_method_change_type(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.change_type(
            0,
            load_balancer_type="lb21",
        )
        assert_matches_type(ActionChangeTypeResponse, action, path=["response"])

    @parametrize
    async def test_method_delete_service(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.delete_service(
            0,
            listen_port=4711,
        )
        assert_matches_type(ActionDeleteServiceResponse, action, path=["response"])

    @parametrize
    async def test_method_detach_from_network(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.detach_from_network(
            0,
            network=4711,
        )
        assert_matches_type(ActionDetachFromNetworkResponse, action, path=["response"])

    @parametrize
    async def test_method_disable_public_interface(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.disable_public_interface(
            0,
        )
        assert_matches_type(ActionDisablePublicInterfaceResponse, action, path=["response"])

    @parametrize
    async def test_method_enable_public_interface(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.enable_public_interface(
            0,
        )
        assert_matches_type(ActionEnablePublicInterfaceResponse, action, path=["response"])

    @parametrize
    async def test_method_remove_target(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.remove_target(
            0,
            type="ip",
        )
        assert_matches_type(ActionRemoveTargetResponse, action, path=["response"])

    @parametrize
    async def test_method_remove_target_with_all_params(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.remove_target(
            0,
            type="ip",
            ip={"ip": "203.0.113.1"},
            label_selector={"selector": "env=prod"},
            server={"id": 80},
        )
        assert_matches_type(ActionRemoveTargetResponse, action, path=["response"])

    @parametrize
    async def test_method_update_service(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.update_service(
            0,
            destination_port=80,
            health_check={
                "interval": 15,
                "port": 4711,
                "protocol": "http",
                "retries": 3,
                "timeout": 10,
            },
            listen_port=443,
            protocol="https",
            proxyprotocol=False,
        )
        assert_matches_type(ActionUpdateServiceResponse, action, path=["response"])

    @parametrize
    async def test_method_update_service_with_all_params(self, client: AsyncHetzner) -> None:
        action = await client.load_balancers.actions.update_service(
            0,
            destination_port=80,
            health_check={
                "http": {
                    "domain": "example.com",
                    "path": "/",
                    "response": '{"status": "ok"}',
                    "status_codes": ["string", "string", "string"],
                    "tls": False,
                },
                "interval": 15,
                "port": 4711,
                "protocol": "http",
                "retries": 3,
                "timeout": 10,
            },
            listen_port=443,
            protocol="https",
            proxyprotocol=False,
            http={
                "certificates": [0, 0, 0],
                "cookie_lifetime": 300,
                "cookie_name": "HCLBSTICKY",
                "redirect_http": True,
                "sticky_sessions": True,
            },
        )
        assert_matches_type(ActionUpdateServiceResponse, action, path=["response"])
