# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from hetzner import Hetzner, AsyncHetzner
from tests.utils import assert_matches_type
from hetzner.types import ImageListResponse, ImageUpdateResponse, ImageRetrieveResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_token = os.environ.get("API_KEY", "something1234")


class TestImages:
    strict_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Hetzner) -> None:
        image = client.images.retrieve(
            0,
        )
        assert_matches_type(ImageRetrieveResponse, image, path=["response"])

    @parametrize
    def test_method_update(self, client: Hetzner) -> None:
        image = client.images.update(
            0,
        )
        assert_matches_type(ImageUpdateResponse, image, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Hetzner) -> None:
        image = client.images.update(
            0,
            description="My new Image description",
            labels={"foo": "string"},
            type="snapshot",
        )
        assert_matches_type(ImageUpdateResponse, image, path=["response"])

    @parametrize
    def test_method_list(self, client: Hetzner) -> None:
        image = client.images.list()
        assert_matches_type(ImageListResponse, image, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hetzner) -> None:
        image = client.images.list(
            architecture="string",
            bound_to="string",
            include_deprecated=True,
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
            status="available",
            type="system",
        )
        assert_matches_type(ImageListResponse, image, path=["response"])

    @parametrize
    def test_method_delete(self, client: Hetzner) -> None:
        image = client.images.delete(
            0,
        )
        assert image is None


class TestAsyncImages:
    strict_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncHetzner) -> None:
        image = await client.images.retrieve(
            0,
        )
        assert_matches_type(ImageRetrieveResponse, image, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncHetzner) -> None:
        image = await client.images.update(
            0,
        )
        assert_matches_type(ImageUpdateResponse, image, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncHetzner) -> None:
        image = await client.images.update(
            0,
            description="My new Image description",
            labels={"foo": "string"},
            type="snapshot",
        )
        assert_matches_type(ImageUpdateResponse, image, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncHetzner) -> None:
        image = await client.images.list()
        assert_matches_type(ImageListResponse, image, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncHetzner) -> None:
        image = await client.images.list(
            architecture="string",
            bound_to="string",
            include_deprecated=True,
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
            status="available",
            type="system",
        )
        assert_matches_type(ImageListResponse, image, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncHetzner) -> None:
        image = await client.images.delete(
            0,
        )
        assert image is None
