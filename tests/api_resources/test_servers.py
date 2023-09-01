# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from hetzner import Hetzner, AsyncHetzner
from tests.utils import assert_matches_type
from hetzner.types import (
    Server,
    ServerCreateResponse,
    ServerDeleteResponse,
    ServerUpdateResponse,
    ServerRetrieveResponse,
)
from hetzner.pagination import SyncServersPage, AsyncServersPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_token = os.environ.get("API_KEY", "something1234")


class TestServers:
    strict_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Hetzner) -> None:
        server = client.servers.create(
            image="ubuntu-20.04",
            name="my-server",
            server_type="cx11",
        )
        assert_matches_type(ServerCreateResponse, server, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Hetzner) -> None:
        server = client.servers.create(
            image="ubuntu-20.04",
            name="my-server",
            server_type="cx11",
            automount=False,
            datacenter="nbg1-dc3",
            firewalls=[{"firewall": 0}, {"firewall": 0}, {"firewall": 0}],
            labels={"foo": "string"},
            location="nbg1",
            networks=[0, 0, 0],
            placement_group=1,
            public_net={
                "enable_ipv4": True,
                "enable_ipv6": True,
                "ipv4": 0,
                "ipv6": 0,
            },
            ssh_keys=["string", "string", "string"],
            start_after_create=True,
            user_data="#cloud-config\nruncmd:\n- [touch, /root/cloud-init-worked]\n",
            volumes=[0, 0, 0],
        )
        assert_matches_type(ServerCreateResponse, server, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Hetzner) -> None:
        server = client.servers.retrieve(
            0,
        )
        assert_matches_type(ServerRetrieveResponse, server, path=["response"])

    @parametrize
    def test_method_update(self, client: Hetzner) -> None:
        server = client.servers.update(
            0,
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Hetzner) -> None:
        server = client.servers.update(
            0,
            labels={"foo": "string"},
            name="my-server",
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @parametrize
    def test_method_list(self, client: Hetzner) -> None:
        server = client.servers.list()
        assert_matches_type(SyncServersPage[Server], server, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hetzner) -> None:
        server = client.servers.list(
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
            status="initializing",
        )
        assert_matches_type(SyncServersPage[Server], server, path=["response"])

    @parametrize
    def test_method_delete(self, client: Hetzner) -> None:
        server = client.servers.delete(
            0,
        )
        assert_matches_type(ServerDeleteResponse, server, path=["response"])


class TestAsyncServers:
    strict_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncHetzner) -> None:
        server = await client.servers.create(
            image="ubuntu-20.04",
            name="my-server",
            server_type="cx11",
        )
        assert_matches_type(ServerCreateResponse, server, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncHetzner) -> None:
        server = await client.servers.create(
            image="ubuntu-20.04",
            name="my-server",
            server_type="cx11",
            automount=False,
            datacenter="nbg1-dc3",
            firewalls=[{"firewall": 0}, {"firewall": 0}, {"firewall": 0}],
            labels={"foo": "string"},
            location="nbg1",
            networks=[0, 0, 0],
            placement_group=1,
            public_net={
                "enable_ipv4": True,
                "enable_ipv6": True,
                "ipv4": 0,
                "ipv6": 0,
            },
            ssh_keys=["string", "string", "string"],
            start_after_create=True,
            user_data="#cloud-config\nruncmd:\n- [touch, /root/cloud-init-worked]\n",
            volumes=[0, 0, 0],
        )
        assert_matches_type(ServerCreateResponse, server, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncHetzner) -> None:
        server = await client.servers.retrieve(
            0,
        )
        assert_matches_type(ServerRetrieveResponse, server, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncHetzner) -> None:
        server = await client.servers.update(
            0,
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncHetzner) -> None:
        server = await client.servers.update(
            0,
            labels={"foo": "string"},
            name="my-server",
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncHetzner) -> None:
        server = await client.servers.list()
        assert_matches_type(AsyncServersPage[Server], server, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncHetzner) -> None:
        server = await client.servers.list(
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
            status="initializing",
        )
        assert_matches_type(AsyncServersPage[Server], server, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncHetzner) -> None:
        server = await client.servers.delete(
            0,
        )
        assert_matches_type(ServerDeleteResponse, server, path=["response"])
