# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from hetzner import Hetzner, AsyncHetzner
from tests.utils import assert_matches_type
from hetzner.types import (
    VolumeListResponse,
    VolumeCreateResponse,
    VolumeUpdateResponse,
    VolumeRetrieveResponse,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_token = os.environ.get("API_KEY", "something1234")


class TestVolumes:
    strict_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Hetzner) -> None:
        volume = client.volumes.create(
            name="databases-storage",
            size=42,
        )
        assert_matches_type(VolumeCreateResponse, volume, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Hetzner) -> None:
        volume = client.volumes.create(
            name="databases-storage",
            size=42,
            automount=False,
            format="xfs",
            labels={"foo": "string"},
            location="nbg1",
            server=0,
        )
        assert_matches_type(VolumeCreateResponse, volume, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Hetzner) -> None:
        volume = client.volumes.retrieve(
            0,
        )
        assert_matches_type(VolumeRetrieveResponse, volume, path=["response"])

    @parametrize
    def test_method_update(self, client: Hetzner) -> None:
        volume = client.volumes.update(
            0,
            name="database-storage",
        )
        assert_matches_type(VolumeUpdateResponse, volume, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Hetzner) -> None:
        volume = client.volumes.update(
            0,
            name="database-storage",
            labels={"foo": "string"},
        )
        assert_matches_type(VolumeUpdateResponse, volume, path=["response"])

    @parametrize
    def test_method_list(self, client: Hetzner) -> None:
        volume = client.volumes.list()
        assert_matches_type(VolumeListResponse, volume, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hetzner) -> None:
        volume = client.volumes.list(
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
            status="available",
        )
        assert_matches_type(VolumeListResponse, volume, path=["response"])

    @parametrize
    def test_method_delete(self, client: Hetzner) -> None:
        volume = client.volumes.delete(
            0,
        )
        assert volume is None


class TestAsyncVolumes:
    strict_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncHetzner) -> None:
        volume = await client.volumes.create(
            name="databases-storage",
            size=42,
        )
        assert_matches_type(VolumeCreateResponse, volume, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncHetzner) -> None:
        volume = await client.volumes.create(
            name="databases-storage",
            size=42,
            automount=False,
            format="xfs",
            labels={"foo": "string"},
            location="nbg1",
            server=0,
        )
        assert_matches_type(VolumeCreateResponse, volume, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncHetzner) -> None:
        volume = await client.volumes.retrieve(
            0,
        )
        assert_matches_type(VolumeRetrieveResponse, volume, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncHetzner) -> None:
        volume = await client.volumes.update(
            0,
            name="database-storage",
        )
        assert_matches_type(VolumeUpdateResponse, volume, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncHetzner) -> None:
        volume = await client.volumes.update(
            0,
            name="database-storage",
            labels={"foo": "string"},
        )
        assert_matches_type(VolumeUpdateResponse, volume, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncHetzner) -> None:
        volume = await client.volumes.list()
        assert_matches_type(VolumeListResponse, volume, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncHetzner) -> None:
        volume = await client.volumes.list(
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
            status="available",
        )
        assert_matches_type(VolumeListResponse, volume, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncHetzner) -> None:
        volume = await client.volumes.delete(
            0,
        )
        assert volume is None
