# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from hetzner import Hetzner, AsyncHetzner
from tests.utils import assert_matches_type
from hetzner.types import (
    CertificateListResponse,
    CertificateCreateResponse,
    CertificateUpdateResponse,
    CertificateRetrieveResponse,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_token = os.environ.get("API_KEY", "something1234")


class TestCertificates:
    strict_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Hetzner) -> None:
        certificate = client.certificates.create(
            name="my website cert",
        )
        assert_matches_type(CertificateCreateResponse, certificate, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Hetzner) -> None:
        certificate = client.certificates.create(
            name="my website cert",
            certificate="-----BEGIN CERTIFICATE-----\n...",
            domain_names=["string", "string", "string"],
            labels={"foo": "string"},
            private_key="-----BEGIN PRIVATE KEY-----\n...",
            type="uploaded",
        )
        assert_matches_type(CertificateCreateResponse, certificate, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Hetzner) -> None:
        certificate = client.certificates.retrieve(
            0,
        )
        assert_matches_type(CertificateRetrieveResponse, certificate, path=["response"])

    @parametrize
    def test_method_update(self, client: Hetzner) -> None:
        certificate = client.certificates.update(
            0,
        )
        assert_matches_type(CertificateUpdateResponse, certificate, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Hetzner) -> None:
        certificate = client.certificates.update(
            0,
            labels={"foo": "string"},
            name="my website cert",
        )
        assert_matches_type(CertificateUpdateResponse, certificate, path=["response"])

    @parametrize
    def test_method_list(self, client: Hetzner) -> None:
        certificate = client.certificates.list()
        assert_matches_type(CertificateListResponse, certificate, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hetzner) -> None:
        certificate = client.certificates.list(
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
            type="uploaded",
        )
        assert_matches_type(CertificateListResponse, certificate, path=["response"])

    @parametrize
    def test_method_delete(self, client: Hetzner) -> None:
        certificate = client.certificates.delete(
            0,
        )
        assert certificate is None


class TestAsyncCertificates:
    strict_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncHetzner) -> None:
        certificate = await client.certificates.create(
            name="my website cert",
        )
        assert_matches_type(CertificateCreateResponse, certificate, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncHetzner) -> None:
        certificate = await client.certificates.create(
            name="my website cert",
            certificate="-----BEGIN CERTIFICATE-----\n...",
            domain_names=["string", "string", "string"],
            labels={"foo": "string"},
            private_key="-----BEGIN PRIVATE KEY-----\n...",
            type="uploaded",
        )
        assert_matches_type(CertificateCreateResponse, certificate, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncHetzner) -> None:
        certificate = await client.certificates.retrieve(
            0,
        )
        assert_matches_type(CertificateRetrieveResponse, certificate, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncHetzner) -> None:
        certificate = await client.certificates.update(
            0,
        )
        assert_matches_type(CertificateUpdateResponse, certificate, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncHetzner) -> None:
        certificate = await client.certificates.update(
            0,
            labels={"foo": "string"},
            name="my website cert",
        )
        assert_matches_type(CertificateUpdateResponse, certificate, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncHetzner) -> None:
        certificate = await client.certificates.list()
        assert_matches_type(CertificateListResponse, certificate, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncHetzner) -> None:
        certificate = await client.certificates.list(
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
            type="uploaded",
        )
        assert_matches_type(CertificateListResponse, certificate, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncHetzner) -> None:
        certificate = await client.certificates.delete(
            0,
        )
        assert certificate is None
