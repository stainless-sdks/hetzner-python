# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from hetzner import Hetzner, AsyncHetzner
from tests.utils import assert_matches_type
from hetzner.types import (
    NetworkListResponse,
    NetworkCreateResponse,
    NetworkUpdateResponse,
    NetworkRetrieveResponse,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_token = os.environ.get("API_KEY", "something1234")


class TestNetworks:
    strict_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Hetzner) -> None:
        network = client.networks.create(
            ip_range="10.0.0.0/16",
            name="mynet",
        )
        assert_matches_type(NetworkCreateResponse, network, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Hetzner) -> None:
        network = client.networks.create(
            ip_range="10.0.0.0/16",
            name="mynet",
            expose_routes_to_vswitch=False,
            labels={"foo": "string"},
            routes=[
                {
                    "destination": "10.100.1.0/24",
                    "gateway": "10.0.1.1",
                },
                {
                    "destination": "10.100.1.0/24",
                    "gateway": "10.0.1.1",
                },
                {
                    "destination": "10.100.1.0/24",
                    "gateway": "10.0.1.1",
                },
            ],
            subnets=[
                {
                    "ip_range": "10.0.1.0/24",
                    "network_zone": "eu-central",
                    "type": "cloud",
                    "vswitch_id": 1000,
                },
                {
                    "ip_range": "10.0.1.0/24",
                    "network_zone": "eu-central",
                    "type": "cloud",
                    "vswitch_id": 1000,
                },
                {
                    "ip_range": "10.0.1.0/24",
                    "network_zone": "eu-central",
                    "type": "cloud",
                    "vswitch_id": 1000,
                },
            ],
        )
        assert_matches_type(NetworkCreateResponse, network, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Hetzner) -> None:
        network = client.networks.retrieve(
            0,
        )
        assert_matches_type(NetworkRetrieveResponse, network, path=["response"])

    @parametrize
    def test_method_update(self, client: Hetzner) -> None:
        network = client.networks.update(
            0,
        )
        assert_matches_type(NetworkUpdateResponse, network, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Hetzner) -> None:
        network = client.networks.update(
            0,
            expose_routes_to_vswitch=False,
            labels={"foo": "string"},
            name="new-name",
        )
        assert_matches_type(NetworkUpdateResponse, network, path=["response"])

    @parametrize
    def test_method_list(self, client: Hetzner) -> None:
        network = client.networks.list()
        assert_matches_type(NetworkListResponse, network, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hetzner) -> None:
        network = client.networks.list(
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
        )
        assert_matches_type(NetworkListResponse, network, path=["response"])

    @parametrize
    def test_method_delete(self, client: Hetzner) -> None:
        network = client.networks.delete(
            0,
        )
        assert network is None


class TestAsyncNetworks:
    strict_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncHetzner) -> None:
        network = await client.networks.create(
            ip_range="10.0.0.0/16",
            name="mynet",
        )
        assert_matches_type(NetworkCreateResponse, network, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncHetzner) -> None:
        network = await client.networks.create(
            ip_range="10.0.0.0/16",
            name="mynet",
            expose_routes_to_vswitch=False,
            labels={"foo": "string"},
            routes=[
                {
                    "destination": "10.100.1.0/24",
                    "gateway": "10.0.1.1",
                },
                {
                    "destination": "10.100.1.0/24",
                    "gateway": "10.0.1.1",
                },
                {
                    "destination": "10.100.1.0/24",
                    "gateway": "10.0.1.1",
                },
            ],
            subnets=[
                {
                    "ip_range": "10.0.1.0/24",
                    "network_zone": "eu-central",
                    "type": "cloud",
                    "vswitch_id": 1000,
                },
                {
                    "ip_range": "10.0.1.0/24",
                    "network_zone": "eu-central",
                    "type": "cloud",
                    "vswitch_id": 1000,
                },
                {
                    "ip_range": "10.0.1.0/24",
                    "network_zone": "eu-central",
                    "type": "cloud",
                    "vswitch_id": 1000,
                },
            ],
        )
        assert_matches_type(NetworkCreateResponse, network, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncHetzner) -> None:
        network = await client.networks.retrieve(
            0,
        )
        assert_matches_type(NetworkRetrieveResponse, network, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncHetzner) -> None:
        network = await client.networks.update(
            0,
        )
        assert_matches_type(NetworkUpdateResponse, network, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncHetzner) -> None:
        network = await client.networks.update(
            0,
            expose_routes_to_vswitch=False,
            labels={"foo": "string"},
            name="new-name",
        )
        assert_matches_type(NetworkUpdateResponse, network, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncHetzner) -> None:
        network = await client.networks.list()
        assert_matches_type(NetworkListResponse, network, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncHetzner) -> None:
        network = await client.networks.list(
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
        )
        assert_matches_type(NetworkListResponse, network, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncHetzner) -> None:
        network = await client.networks.delete(
            0,
        )
        assert network is None
