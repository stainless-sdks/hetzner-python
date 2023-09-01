# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from hetzner import Hetzner, AsyncHetzner
from tests.utils import assert_matches_type
from hetzner.types import (
    FirewallListResponse,
    FirewallCreateResponse,
    FirewallUpdateResponse,
    FirewallRetrieveResponse,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_token = os.environ.get("API_KEY", "something1234")


class TestFirewalls:
    strict_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Hetzner) -> None:
        firewall = client.firewalls.create(
            name="Corporate Intranet Protection",
        )
        assert_matches_type(FirewallCreateResponse, firewall, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Hetzner) -> None:
        firewall = client.firewalls.create(
            name="Corporate Intranet Protection",
            apply_to=[
                {
                    "label_selector": {"selector": "env=prod"},
                    "server": {"id": 42},
                    "type": "label_selector",
                },
                {
                    "label_selector": {"selector": "env=prod"},
                    "server": {"id": 42},
                    "type": "label_selector",
                },
                {
                    "label_selector": {"selector": "env=prod"},
                    "server": {"id": 42},
                    "type": "label_selector",
                },
            ],
            labels={"foo": "string"},
            rules=[
                {
                    "description": "string",
                    "destination_ips": ["string", "string", "string"],
                    "direction": "in",
                    "port": "80",
                    "protocol": "esp",
                    "source_ips": ["string", "string", "string"],
                },
                {
                    "description": "string",
                    "destination_ips": ["string", "string", "string"],
                    "direction": "in",
                    "port": "80",
                    "protocol": "esp",
                    "source_ips": ["string", "string", "string"],
                },
                {
                    "description": "string",
                    "destination_ips": ["string", "string", "string"],
                    "direction": "in",
                    "port": "80",
                    "protocol": "esp",
                    "source_ips": ["string", "string", "string"],
                },
            ],
        )
        assert_matches_type(FirewallCreateResponse, firewall, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Hetzner) -> None:
        firewall = client.firewalls.retrieve(
            0,
        )
        assert_matches_type(FirewallRetrieveResponse, firewall, path=["response"])

    @parametrize
    def test_method_update(self, client: Hetzner) -> None:
        firewall = client.firewalls.update(
            0,
        )
        assert_matches_type(FirewallUpdateResponse, firewall, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Hetzner) -> None:
        firewall = client.firewalls.update(
            0,
            labels={"foo": "string"},
            name="new-name",
        )
        assert_matches_type(FirewallUpdateResponse, firewall, path=["response"])

    @parametrize
    def test_method_list(self, client: Hetzner) -> None:
        firewall = client.firewalls.list()
        assert_matches_type(FirewallListResponse, firewall, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hetzner) -> None:
        firewall = client.firewalls.list(
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
        )
        assert_matches_type(FirewallListResponse, firewall, path=["response"])

    @parametrize
    def test_method_delete(self, client: Hetzner) -> None:
        firewall = client.firewalls.delete(
            0,
        )
        assert firewall is None


class TestAsyncFirewalls:
    strict_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncHetzner) -> None:
        firewall = await client.firewalls.create(
            name="Corporate Intranet Protection",
        )
        assert_matches_type(FirewallCreateResponse, firewall, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncHetzner) -> None:
        firewall = await client.firewalls.create(
            name="Corporate Intranet Protection",
            apply_to=[
                {
                    "label_selector": {"selector": "env=prod"},
                    "server": {"id": 42},
                    "type": "label_selector",
                },
                {
                    "label_selector": {"selector": "env=prod"},
                    "server": {"id": 42},
                    "type": "label_selector",
                },
                {
                    "label_selector": {"selector": "env=prod"},
                    "server": {"id": 42},
                    "type": "label_selector",
                },
            ],
            labels={"foo": "string"},
            rules=[
                {
                    "description": "string",
                    "destination_ips": ["string", "string", "string"],
                    "direction": "in",
                    "port": "80",
                    "protocol": "esp",
                    "source_ips": ["string", "string", "string"],
                },
                {
                    "description": "string",
                    "destination_ips": ["string", "string", "string"],
                    "direction": "in",
                    "port": "80",
                    "protocol": "esp",
                    "source_ips": ["string", "string", "string"],
                },
                {
                    "description": "string",
                    "destination_ips": ["string", "string", "string"],
                    "direction": "in",
                    "port": "80",
                    "protocol": "esp",
                    "source_ips": ["string", "string", "string"],
                },
            ],
        )
        assert_matches_type(FirewallCreateResponse, firewall, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncHetzner) -> None:
        firewall = await client.firewalls.retrieve(
            0,
        )
        assert_matches_type(FirewallRetrieveResponse, firewall, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncHetzner) -> None:
        firewall = await client.firewalls.update(
            0,
        )
        assert_matches_type(FirewallUpdateResponse, firewall, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncHetzner) -> None:
        firewall = await client.firewalls.update(
            0,
            labels={"foo": "string"},
            name="new-name",
        )
        assert_matches_type(FirewallUpdateResponse, firewall, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncHetzner) -> None:
        firewall = await client.firewalls.list()
        assert_matches_type(FirewallListResponse, firewall, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncHetzner) -> None:
        firewall = await client.firewalls.list(
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
        )
        assert_matches_type(FirewallListResponse, firewall, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncHetzner) -> None:
        firewall = await client.firewalls.delete(
            0,
        )
        assert firewall is None
