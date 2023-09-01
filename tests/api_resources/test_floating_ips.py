# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from hetzner import Hetzner, AsyncHetzner
from tests.utils import assert_matches_type
from hetzner.types import (
    FloatingIp,
    FloatingIpCreateResponse,
    FloatingIpUpdateResponse,
    FloatingIpRetrieveResponse,
)
from hetzner.pagination import SyncFloatingIpsPage, AsyncFloatingIpsPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_token = os.environ.get("API_KEY", "something1234")


class TestFloatingIps:
    strict_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Hetzner) -> None:
        floating_ip = client.floating_ips.create(
            type="ipv4",
        )
        assert_matches_type(FloatingIpCreateResponse, floating_ip, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Hetzner) -> None:
        floating_ip = client.floating_ips.create(
            type="ipv4",
            description="Web Frontend",
            home_location="fsn1",
            labels={"foo": "string"},
            name="Web Frontend",
            server=42,
        )
        assert_matches_type(FloatingIpCreateResponse, floating_ip, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Hetzner) -> None:
        floating_ip = client.floating_ips.retrieve(
            0,
        )
        assert_matches_type(FloatingIpRetrieveResponse, floating_ip, path=["response"])

    @parametrize
    def test_method_update(self, client: Hetzner) -> None:
        floating_ip = client.floating_ips.update(
            0,
        )
        assert_matches_type(FloatingIpUpdateResponse, floating_ip, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Hetzner) -> None:
        floating_ip = client.floating_ips.update(
            0,
            description="Web Frontend",
            labels={"foo": "string"},
            name="Web Frontend",
        )
        assert_matches_type(FloatingIpUpdateResponse, floating_ip, path=["response"])

    @parametrize
    def test_method_list(self, client: Hetzner) -> None:
        floating_ip = client.floating_ips.list()
        assert_matches_type(SyncFloatingIpsPage[FloatingIp], floating_ip, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hetzner) -> None:
        floating_ip = client.floating_ips.list(
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
        )
        assert_matches_type(SyncFloatingIpsPage[FloatingIp], floating_ip, path=["response"])

    @parametrize
    def test_method_delete(self, client: Hetzner) -> None:
        floating_ip = client.floating_ips.delete(
            0,
        )
        assert floating_ip is None


class TestAsyncFloatingIps:
    strict_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncHetzner) -> None:
        floating_ip = await client.floating_ips.create(
            type="ipv4",
        )
        assert_matches_type(FloatingIpCreateResponse, floating_ip, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncHetzner) -> None:
        floating_ip = await client.floating_ips.create(
            type="ipv4",
            description="Web Frontend",
            home_location="fsn1",
            labels={"foo": "string"},
            name="Web Frontend",
            server=42,
        )
        assert_matches_type(FloatingIpCreateResponse, floating_ip, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncHetzner) -> None:
        floating_ip = await client.floating_ips.retrieve(
            0,
        )
        assert_matches_type(FloatingIpRetrieveResponse, floating_ip, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncHetzner) -> None:
        floating_ip = await client.floating_ips.update(
            0,
        )
        assert_matches_type(FloatingIpUpdateResponse, floating_ip, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncHetzner) -> None:
        floating_ip = await client.floating_ips.update(
            0,
            description="Web Frontend",
            labels={"foo": "string"},
            name="Web Frontend",
        )
        assert_matches_type(FloatingIpUpdateResponse, floating_ip, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncHetzner) -> None:
        floating_ip = await client.floating_ips.list()
        assert_matches_type(AsyncFloatingIpsPage[FloatingIp], floating_ip, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncHetzner) -> None:
        floating_ip = await client.floating_ips.list(
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
        )
        assert_matches_type(AsyncFloatingIpsPage[FloatingIp], floating_ip, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncHetzner) -> None:
        floating_ip = await client.floating_ips.delete(
            0,
        )
        assert floating_ip is None
