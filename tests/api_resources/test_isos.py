# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from hetzner import Hetzner, AsyncHetzner
from tests.utils import assert_matches_type
from hetzner.types import ISOListResponse, ISORetrieveResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_token = os.environ.get("API_KEY", "something1234")


class TestISOs:
    strict_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Hetzner) -> None:
        iso = client.isos.retrieve(
            0,
        )
        assert_matches_type(ISORetrieveResponse, iso, path=["response"])

    @parametrize
    def test_method_list(self, client: Hetzner) -> None:
        iso = client.isos.list()
        assert_matches_type(ISOListResponse, iso, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hetzner) -> None:
        iso = client.isos.list(
            architecture="string",
            include_architecture_wildcard=True,
            name="string",
            page=1,
            per_page=1,
        )
        assert_matches_type(ISOListResponse, iso, path=["response"])


class TestAsyncISOs:
    strict_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncHetzner) -> None:
        iso = await client.isos.retrieve(
            0,
        )
        assert_matches_type(ISORetrieveResponse, iso, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncHetzner) -> None:
        iso = await client.isos.list()
        assert_matches_type(ISOListResponse, iso, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncHetzner) -> None:
        iso = await client.isos.list(
            architecture="string",
            include_architecture_wildcard=True,
            name="string",
            page=1,
            per_page=1,
        )
        assert_matches_type(ISOListResponse, iso, path=["response"])
