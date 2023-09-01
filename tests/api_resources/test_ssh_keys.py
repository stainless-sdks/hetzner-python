# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from hetzner import Hetzner, AsyncHetzner
from tests.utils import assert_matches_type
from hetzner.types import (
    SshKeyListResponse,
    SshKeyCreateResponse,
    SshKeyUpdateResponse,
    SshKeyRetrieveResponse,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_token = os.environ.get("API_KEY", "something1234")


class TestSshKeys:
    strict_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Hetzner) -> None:
        ssh_key = client.ssh_keys.create(
            name="My ssh key",
            public_key="ssh-rsa AAAjjk76kgf...Xt",
        )
        assert_matches_type(SshKeyCreateResponse, ssh_key, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Hetzner) -> None:
        ssh_key = client.ssh_keys.create(
            name="My ssh key",
            public_key="ssh-rsa AAAjjk76kgf...Xt",
            labels={"foo": "string"},
        )
        assert_matches_type(SshKeyCreateResponse, ssh_key, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Hetzner) -> None:
        ssh_key = client.ssh_keys.retrieve(
            0,
        )
        assert_matches_type(SshKeyRetrieveResponse, ssh_key, path=["response"])

    @parametrize
    def test_method_update(self, client: Hetzner) -> None:
        ssh_key = client.ssh_keys.update(
            0,
        )
        assert_matches_type(SshKeyUpdateResponse, ssh_key, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Hetzner) -> None:
        ssh_key = client.ssh_keys.update(
            0,
            labels={"foo": "string"},
            name="My ssh key",
        )
        assert_matches_type(SshKeyUpdateResponse, ssh_key, path=["response"])

    @parametrize
    def test_method_list(self, client: Hetzner) -> None:
        ssh_key = client.ssh_keys.list()
        assert_matches_type(SshKeyListResponse, ssh_key, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hetzner) -> None:
        ssh_key = client.ssh_keys.list(
            fingerprint="string",
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
        )
        assert_matches_type(SshKeyListResponse, ssh_key, path=["response"])

    @parametrize
    def test_method_delete(self, client: Hetzner) -> None:
        ssh_key = client.ssh_keys.delete(
            0,
        )
        assert ssh_key is None


class TestAsyncSshKeys:
    strict_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncHetzner) -> None:
        ssh_key = await client.ssh_keys.create(
            name="My ssh key",
            public_key="ssh-rsa AAAjjk76kgf...Xt",
        )
        assert_matches_type(SshKeyCreateResponse, ssh_key, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncHetzner) -> None:
        ssh_key = await client.ssh_keys.create(
            name="My ssh key",
            public_key="ssh-rsa AAAjjk76kgf...Xt",
            labels={"foo": "string"},
        )
        assert_matches_type(SshKeyCreateResponse, ssh_key, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncHetzner) -> None:
        ssh_key = await client.ssh_keys.retrieve(
            0,
        )
        assert_matches_type(SshKeyRetrieveResponse, ssh_key, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncHetzner) -> None:
        ssh_key = await client.ssh_keys.update(
            0,
        )
        assert_matches_type(SshKeyUpdateResponse, ssh_key, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncHetzner) -> None:
        ssh_key = await client.ssh_keys.update(
            0,
            labels={"foo": "string"},
            name="My ssh key",
        )
        assert_matches_type(SshKeyUpdateResponse, ssh_key, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncHetzner) -> None:
        ssh_key = await client.ssh_keys.list()
        assert_matches_type(SshKeyListResponse, ssh_key, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncHetzner) -> None:
        ssh_key = await client.ssh_keys.list(
            fingerprint="string",
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
        )
        assert_matches_type(SshKeyListResponse, ssh_key, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncHetzner) -> None:
        ssh_key = await client.ssh_keys.delete(
            0,
        )
        assert ssh_key is None
