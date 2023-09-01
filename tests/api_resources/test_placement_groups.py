# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from hetzner import Hetzner, AsyncHetzner
from tests.utils import assert_matches_type
from hetzner.types import (
    PlacementGroupListResponse,
    PlacementGroupCreateResponse,
    PlacementGroupUpdateResponse,
    PlacementGroupRetrieveResponse,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_token = os.environ.get("API_KEY", "something1234")


class TestPlacementGroups:
    strict_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Hetzner) -> None:
        placement_group = client.placement_groups.create(
            name="my Placement Group",
            type="spread",
        )
        assert_matches_type(PlacementGroupCreateResponse, placement_group, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Hetzner) -> None:
        placement_group = client.placement_groups.create(
            name="my Placement Group",
            type="spread",
            labels={"foo": "string"},
        )
        assert_matches_type(PlacementGroupCreateResponse, placement_group, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Hetzner) -> None:
        placement_group = client.placement_groups.retrieve(
            0,
        )
        assert_matches_type(PlacementGroupRetrieveResponse, placement_group, path=["response"])

    @parametrize
    def test_method_update(self, client: Hetzner) -> None:
        placement_group = client.placement_groups.update(
            0,
        )
        assert_matches_type(PlacementGroupUpdateResponse, placement_group, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Hetzner) -> None:
        placement_group = client.placement_groups.update(
            0,
            labels={"foo": "string"},
            name="my Placement Group",
        )
        assert_matches_type(PlacementGroupUpdateResponse, placement_group, path=["response"])

    @parametrize
    def test_method_list(self, client: Hetzner) -> None:
        placement_group = client.placement_groups.list()
        assert_matches_type(PlacementGroupListResponse, placement_group, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hetzner) -> None:
        placement_group = client.placement_groups.list(
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
            type="spread",
        )
        assert_matches_type(PlacementGroupListResponse, placement_group, path=["response"])

    @parametrize
    def test_method_delete(self, client: Hetzner) -> None:
        placement_group = client.placement_groups.delete(
            0,
        )
        assert placement_group is None


class TestAsyncPlacementGroups:
    strict_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncHetzner) -> None:
        placement_group = await client.placement_groups.create(
            name="my Placement Group",
            type="spread",
        )
        assert_matches_type(PlacementGroupCreateResponse, placement_group, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncHetzner) -> None:
        placement_group = await client.placement_groups.create(
            name="my Placement Group",
            type="spread",
            labels={"foo": "string"},
        )
        assert_matches_type(PlacementGroupCreateResponse, placement_group, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncHetzner) -> None:
        placement_group = await client.placement_groups.retrieve(
            0,
        )
        assert_matches_type(PlacementGroupRetrieveResponse, placement_group, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncHetzner) -> None:
        placement_group = await client.placement_groups.update(
            0,
        )
        assert_matches_type(PlacementGroupUpdateResponse, placement_group, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncHetzner) -> None:
        placement_group = await client.placement_groups.update(
            0,
            labels={"foo": "string"},
            name="my Placement Group",
        )
        assert_matches_type(PlacementGroupUpdateResponse, placement_group, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncHetzner) -> None:
        placement_group = await client.placement_groups.list()
        assert_matches_type(PlacementGroupListResponse, placement_group, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncHetzner) -> None:
        placement_group = await client.placement_groups.list(
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
            type="spread",
        )
        assert_matches_type(PlacementGroupListResponse, placement_group, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncHetzner) -> None:
        placement_group = await client.placement_groups.delete(
            0,
        )
        assert placement_group is None
