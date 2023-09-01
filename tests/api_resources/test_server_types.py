# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from hetzner import Hetzner, AsyncHetzner
from tests.utils import assert_matches_type
from hetzner.types import ServerTypeListResponse, ServerTypeRetrieveResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_token = os.environ.get("API_KEY", "something1234")


class TestServerTypes:
    strict_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Hetzner) -> None:
        server_type = client.server_types.retrieve(
            0,
        )
        assert_matches_type(ServerTypeRetrieveResponse, server_type, path=["response"])

    @parametrize
    def test_method_list(self, client: Hetzner) -> None:
        server_type = client.server_types.list()
        assert_matches_type(ServerTypeListResponse, server_type, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hetzner) -> None:
        server_type = client.server_types.list(
            name="string",
            page=1,
            per_page=1,
        )
        assert_matches_type(ServerTypeListResponse, server_type, path=["response"])


class TestAsyncServerTypes:
    strict_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncHetzner) -> None:
        server_type = await client.server_types.retrieve(
            0,
        )
        assert_matches_type(ServerTypeRetrieveResponse, server_type, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncHetzner) -> None:
        server_type = await client.server_types.list()
        assert_matches_type(ServerTypeListResponse, server_type, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncHetzner) -> None:
        server_type = await client.server_types.list(
            name="string",
            page=1,
            per_page=1,
        )
        assert_matches_type(ServerTypeListResponse, server_type, path=["response"])
