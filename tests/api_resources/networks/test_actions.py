# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from hetzner import Hetzner, AsyncHetzner
from tests.utils import assert_matches_type
from hetzner.types.networks import (
    ActionListResponse,
    ActionAddRouteResponse,
    ActionRetrieveResponse,
    ActionAddSubnetResponse,
    ActionDeleteRouteResponse,
    ActionDeleteSubnetResponse,
    ActionChangeIPRangeResponse,
    ActionChangeProtectionResponse,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_token = os.environ.get("API_KEY", "something1234")


class TestActions:
    strict_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Hetzner) -> None:
        action = client.networks.actions.retrieve(
            0,
            id=0,
        )
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @parametrize
    def test_method_list(self, client: Hetzner) -> None:
        action = client.networks.actions.list(
            0,
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hetzner) -> None:
        action = client.networks.actions.list(
            0,
            page=1,
            per_page=1,
            sort="id",
            status="running",
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    def test_method_add_route(self, client: Hetzner) -> None:
        action = client.networks.actions.add_route(
            0,
            destination="10.100.1.0/24",
            gateway="10.0.1.1",
        )
        assert_matches_type(ActionAddRouteResponse, action, path=["response"])

    @parametrize
    def test_method_add_subnet(self, client: Hetzner) -> None:
        action = client.networks.actions.add_subnet(
            0,
            network_zone="eu-central",
            type="cloud",
        )
        assert_matches_type(ActionAddSubnetResponse, action, path=["response"])

    @parametrize
    def test_method_add_subnet_with_all_params(self, client: Hetzner) -> None:
        action = client.networks.actions.add_subnet(
            0,
            network_zone="eu-central",
            type="cloud",
            ip_range="10.0.1.0/24",
            vswitch_id=1000,
        )
        assert_matches_type(ActionAddSubnetResponse, action, path=["response"])

    @parametrize
    def test_method_change_ip_range(self, client: Hetzner) -> None:
        action = client.networks.actions.change_ip_range(
            0,
            ip_range="10.0.0.0/12",
        )
        assert_matches_type(ActionChangeIPRangeResponse, action, path=["response"])

    @parametrize
    def test_method_change_protection(self, client: Hetzner) -> None:
        action = client.networks.actions.change_protection(
            0,
        )
        assert_matches_type(ActionChangeProtectionResponse, action, path=["response"])

    @parametrize
    def test_method_change_protection_with_all_params(self, client: Hetzner) -> None:
        action = client.networks.actions.change_protection(
            0,
            delete=True,
        )
        assert_matches_type(ActionChangeProtectionResponse, action, path=["response"])

    @parametrize
    def test_method_delete_route(self, client: Hetzner) -> None:
        action = client.networks.actions.delete_route(
            0,
            destination="10.100.1.0/24",
            gateway="10.0.1.1",
        )
        assert_matches_type(ActionDeleteRouteResponse, action, path=["response"])

    @parametrize
    def test_method_delete_subnet(self, client: Hetzner) -> None:
        action = client.networks.actions.delete_subnet(
            0,
            ip_range="10.0.1.0/24",
        )
        assert_matches_type(ActionDeleteSubnetResponse, action, path=["response"])


class TestAsyncActions:
    strict_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncHetzner) -> None:
        action = await client.networks.actions.retrieve(
            0,
            id=0,
        )
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncHetzner) -> None:
        action = await client.networks.actions.list(
            0,
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncHetzner) -> None:
        action = await client.networks.actions.list(
            0,
            page=1,
            per_page=1,
            sort="id",
            status="running",
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    async def test_method_add_route(self, client: AsyncHetzner) -> None:
        action = await client.networks.actions.add_route(
            0,
            destination="10.100.1.0/24",
            gateway="10.0.1.1",
        )
        assert_matches_type(ActionAddRouteResponse, action, path=["response"])

    @parametrize
    async def test_method_add_subnet(self, client: AsyncHetzner) -> None:
        action = await client.networks.actions.add_subnet(
            0,
            network_zone="eu-central",
            type="cloud",
        )
        assert_matches_type(ActionAddSubnetResponse, action, path=["response"])

    @parametrize
    async def test_method_add_subnet_with_all_params(self, client: AsyncHetzner) -> None:
        action = await client.networks.actions.add_subnet(
            0,
            network_zone="eu-central",
            type="cloud",
            ip_range="10.0.1.0/24",
            vswitch_id=1000,
        )
        assert_matches_type(ActionAddSubnetResponse, action, path=["response"])

    @parametrize
    async def test_method_change_ip_range(self, client: AsyncHetzner) -> None:
        action = await client.networks.actions.change_ip_range(
            0,
            ip_range="10.0.0.0/12",
        )
        assert_matches_type(ActionChangeIPRangeResponse, action, path=["response"])

    @parametrize
    async def test_method_change_protection(self, client: AsyncHetzner) -> None:
        action = await client.networks.actions.change_protection(
            0,
        )
        assert_matches_type(ActionChangeProtectionResponse, action, path=["response"])

    @parametrize
    async def test_method_change_protection_with_all_params(self, client: AsyncHetzner) -> None:
        action = await client.networks.actions.change_protection(
            0,
            delete=True,
        )
        assert_matches_type(ActionChangeProtectionResponse, action, path=["response"])

    @parametrize
    async def test_method_delete_route(self, client: AsyncHetzner) -> None:
        action = await client.networks.actions.delete_route(
            0,
            destination="10.100.1.0/24",
            gateway="10.0.1.1",
        )
        assert_matches_type(ActionDeleteRouteResponse, action, path=["response"])

    @parametrize
    async def test_method_delete_subnet(self, client: AsyncHetzner) -> None:
        action = await client.networks.actions.delete_subnet(
            0,
            ip_range="10.0.1.0/24",
        )
        assert_matches_type(ActionDeleteSubnetResponse, action, path=["response"])
