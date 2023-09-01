# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from hetzner import Hetzner, AsyncHetzner
from tests.utils import assert_matches_type
from hetzner.types import (
    PrimaryIPListResponse,
    PrimaryIPCreateResponse,
    PrimaryIPUpdateResponse,
    PrimaryIPRetrieveResponse,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_token = os.environ.get("API_KEY", "something1234")


class TestPrimaryIPs:
    strict_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Hetzner) -> None:
        primary_ip = client.primary_ips.create(
            assignee_type="server",
            name="my-ip",
            type="ipv4",
        )
        assert_matches_type(PrimaryIPCreateResponse, primary_ip, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Hetzner) -> None:
        primary_ip = client.primary_ips.create(
            assignee_type="server",
            name="my-ip",
            type="ipv4",
            assignee_id=17,
            auto_delete=False,
            datacenter="fsn1-dc8",
            labels={"foo": "string"},
        )
        assert_matches_type(PrimaryIPCreateResponse, primary_ip, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Hetzner) -> None:
        primary_ip = client.primary_ips.retrieve(
            0,
        )
        assert_matches_type(PrimaryIPRetrieveResponse, primary_ip, path=["response"])

    @parametrize
    def test_method_update(self, client: Hetzner) -> None:
        primary_ip = client.primary_ips.update(
            0,
        )
        assert_matches_type(PrimaryIPUpdateResponse, primary_ip, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Hetzner) -> None:
        primary_ip = client.primary_ips.update(
            0,
            auto_delete=True,
            labels={"foo": "string"},
            name="my-ip",
        )
        assert_matches_type(PrimaryIPUpdateResponse, primary_ip, path=["response"])

    @parametrize
    def test_method_list(self, client: Hetzner) -> None:
        primary_ip = client.primary_ips.list()
        assert_matches_type(PrimaryIPListResponse, primary_ip, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hetzner) -> None:
        primary_ip = client.primary_ips.list(
            ip="string",
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
        )
        assert_matches_type(PrimaryIPListResponse, primary_ip, path=["response"])

    @parametrize
    def test_method_delete(self, client: Hetzner) -> None:
        primary_ip = client.primary_ips.delete(
            0,
        )
        assert primary_ip is None


class TestAsyncPrimaryIPs:
    strict_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncHetzner) -> None:
        primary_ip = await client.primary_ips.create(
            assignee_type="server",
            name="my-ip",
            type="ipv4",
        )
        assert_matches_type(PrimaryIPCreateResponse, primary_ip, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncHetzner) -> None:
        primary_ip = await client.primary_ips.create(
            assignee_type="server",
            name="my-ip",
            type="ipv4",
            assignee_id=17,
            auto_delete=False,
            datacenter="fsn1-dc8",
            labels={"foo": "string"},
        )
        assert_matches_type(PrimaryIPCreateResponse, primary_ip, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncHetzner) -> None:
        primary_ip = await client.primary_ips.retrieve(
            0,
        )
        assert_matches_type(PrimaryIPRetrieveResponse, primary_ip, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncHetzner) -> None:
        primary_ip = await client.primary_ips.update(
            0,
        )
        assert_matches_type(PrimaryIPUpdateResponse, primary_ip, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncHetzner) -> None:
        primary_ip = await client.primary_ips.update(
            0,
            auto_delete=True,
            labels={"foo": "string"},
            name="my-ip",
        )
        assert_matches_type(PrimaryIPUpdateResponse, primary_ip, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncHetzner) -> None:
        primary_ip = await client.primary_ips.list()
        assert_matches_type(PrimaryIPListResponse, primary_ip, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncHetzner) -> None:
        primary_ip = await client.primary_ips.list(
            ip="string",
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
        )
        assert_matches_type(PrimaryIPListResponse, primary_ip, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncHetzner) -> None:
        primary_ip = await client.primary_ips.delete(
            0,
        )
        assert primary_ip is None
