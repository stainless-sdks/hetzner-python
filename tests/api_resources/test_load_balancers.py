# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from hetzner import Hetzner, AsyncHetzner
from tests.utils import assert_matches_type
from hetzner.types import (
    LoadBalancerListResponse,
    LoadBalancerCreateResponse,
    LoadBalancerUpdateResponse,
    LoadBalancerRetrieveResponse,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_token = os.environ.get("API_KEY", "something1234")


class TestLoadBalancers:
    strict_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = Hetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Hetzner) -> None:
        load_balancer = client.load_balancers.create(
            algorithm={"type": "least_connections"},
            load_balancer_type="lb11",
            name="Web Frontend",
        )
        assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Hetzner) -> None:
        load_balancer = client.load_balancers.create(
            algorithm={"type": "least_connections"},
            load_balancer_type="lb11",
            name="Web Frontend",
            labels={"foo": "string"},
            location="string",
            network=123,
            network_zone="eu-central",
            public_interface=True,
            services=[
                {
                    "destination_port": 80,
                    "health_check": {
                        "http": {
                            "domain": "example.com",
                            "path": "/",
                            "response": '{"status": "ok"}',
                            "status_codes": ["string", "string", "string"],
                            "tls": False,
                        },
                        "interval": 15,
                        "port": 4711,
                        "protocol": "http",
                        "retries": 3,
                        "timeout": 10,
                    },
                    "http": {
                        "certificates": [0, 0, 0],
                        "cookie_lifetime": 300,
                        "cookie_name": "HCLBSTICKY",
                        "redirect_http": True,
                        "sticky_sessions": True,
                    },
                    "listen_port": 443,
                    "protocol": "https",
                    "proxyprotocol": False,
                },
                {
                    "destination_port": 80,
                    "health_check": {
                        "http": {
                            "domain": "example.com",
                            "path": "/",
                            "response": '{"status": "ok"}',
                            "status_codes": ["string", "string", "string"],
                            "tls": False,
                        },
                        "interval": 15,
                        "port": 4711,
                        "protocol": "http",
                        "retries": 3,
                        "timeout": 10,
                    },
                    "http": {
                        "certificates": [0, 0, 0],
                        "cookie_lifetime": 300,
                        "cookie_name": "HCLBSTICKY",
                        "redirect_http": True,
                        "sticky_sessions": True,
                    },
                    "listen_port": 443,
                    "protocol": "https",
                    "proxyprotocol": False,
                },
                {
                    "destination_port": 80,
                    "health_check": {
                        "http": {
                            "domain": "example.com",
                            "path": "/",
                            "response": '{"status": "ok"}',
                            "status_codes": ["string", "string", "string"],
                            "tls": False,
                        },
                        "interval": 15,
                        "port": 4711,
                        "protocol": "http",
                        "retries": 3,
                        "timeout": 10,
                    },
                    "http": {
                        "certificates": [0, 0, 0],
                        "cookie_lifetime": 300,
                        "cookie_name": "HCLBSTICKY",
                        "redirect_http": True,
                        "sticky_sessions": True,
                    },
                    "listen_port": 443,
                    "protocol": "https",
                    "proxyprotocol": False,
                },
            ],
            targets=[
                {
                    "health_status": [
                        {
                            "listen_port": 443,
                            "status": "healthy",
                        },
                        {
                            "listen_port": 443,
                            "status": "healthy",
                        },
                        {
                            "listen_port": 443,
                            "status": "healthy",
                        },
                    ],
                    "ip": {"ip": "203.0.113.1"},
                    "label_selector": {"selector": "env=prod"},
                    "server": {"id": 42},
                    "targets": [
                        {
                            "health_status": [
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                            ],
                            "server": {"id": 42},
                            "type": "server",
                            "use_private_ip": True,
                        },
                        {
                            "health_status": [
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                            ],
                            "server": {"id": 42},
                            "type": "server",
                            "use_private_ip": True,
                        },
                        {
                            "health_status": [
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                            ],
                            "server": {"id": 42},
                            "type": "server",
                            "use_private_ip": True,
                        },
                    ],
                    "type": "ip",
                    "use_private_ip": True,
                },
                {
                    "health_status": [
                        {
                            "listen_port": 443,
                            "status": "healthy",
                        },
                        {
                            "listen_port": 443,
                            "status": "healthy",
                        },
                        {
                            "listen_port": 443,
                            "status": "healthy",
                        },
                    ],
                    "ip": {"ip": "203.0.113.1"},
                    "label_selector": {"selector": "env=prod"},
                    "server": {"id": 42},
                    "targets": [
                        {
                            "health_status": [
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                            ],
                            "server": {"id": 42},
                            "type": "server",
                            "use_private_ip": True,
                        },
                        {
                            "health_status": [
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                            ],
                            "server": {"id": 42},
                            "type": "server",
                            "use_private_ip": True,
                        },
                        {
                            "health_status": [
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                            ],
                            "server": {"id": 42},
                            "type": "server",
                            "use_private_ip": True,
                        },
                    ],
                    "type": "ip",
                    "use_private_ip": True,
                },
                {
                    "health_status": [
                        {
                            "listen_port": 443,
                            "status": "healthy",
                        },
                        {
                            "listen_port": 443,
                            "status": "healthy",
                        },
                        {
                            "listen_port": 443,
                            "status": "healthy",
                        },
                    ],
                    "ip": {"ip": "203.0.113.1"},
                    "label_selector": {"selector": "env=prod"},
                    "server": {"id": 42},
                    "targets": [
                        {
                            "health_status": [
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                            ],
                            "server": {"id": 42},
                            "type": "server",
                            "use_private_ip": True,
                        },
                        {
                            "health_status": [
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                            ],
                            "server": {"id": 42},
                            "type": "server",
                            "use_private_ip": True,
                        },
                        {
                            "health_status": [
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                            ],
                            "server": {"id": 42},
                            "type": "server",
                            "use_private_ip": True,
                        },
                    ],
                    "type": "ip",
                    "use_private_ip": True,
                },
            ],
        )
        assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Hetzner) -> None:
        load_balancer = client.load_balancers.retrieve(
            0,
        )
        assert_matches_type(LoadBalancerRetrieveResponse, load_balancer, path=["response"])

    @parametrize
    def test_method_update(self, client: Hetzner) -> None:
        load_balancer = client.load_balancers.update(
            0,
        )
        assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Hetzner) -> None:
        load_balancer = client.load_balancers.update(
            0,
            labels={"foo": "string"},
            name="new-name",
        )
        assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

    @parametrize
    def test_method_list(self, client: Hetzner) -> None:
        load_balancer = client.load_balancers.list()
        assert_matches_type(LoadBalancerListResponse, load_balancer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Hetzner) -> None:
        load_balancer = client.load_balancers.list(
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
        )
        assert_matches_type(LoadBalancerListResponse, load_balancer, path=["response"])

    @parametrize
    def test_method_delete(self, client: Hetzner) -> None:
        load_balancer = client.load_balancers.delete(
            0,
        )
        assert load_balancer is None


class TestAsyncLoadBalancers:
    strict_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=True)
    loose_client = AsyncHetzner(base_url=base_url, api_token=api_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncHetzner) -> None:
        load_balancer = await client.load_balancers.create(
            algorithm={"type": "least_connections"},
            load_balancer_type="lb11",
            name="Web Frontend",
        )
        assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncHetzner) -> None:
        load_balancer = await client.load_balancers.create(
            algorithm={"type": "least_connections"},
            load_balancer_type="lb11",
            name="Web Frontend",
            labels={"foo": "string"},
            location="string",
            network=123,
            network_zone="eu-central",
            public_interface=True,
            services=[
                {
                    "destination_port": 80,
                    "health_check": {
                        "http": {
                            "domain": "example.com",
                            "path": "/",
                            "response": '{"status": "ok"}',
                            "status_codes": ["string", "string", "string"],
                            "tls": False,
                        },
                        "interval": 15,
                        "port": 4711,
                        "protocol": "http",
                        "retries": 3,
                        "timeout": 10,
                    },
                    "http": {
                        "certificates": [0, 0, 0],
                        "cookie_lifetime": 300,
                        "cookie_name": "HCLBSTICKY",
                        "redirect_http": True,
                        "sticky_sessions": True,
                    },
                    "listen_port": 443,
                    "protocol": "https",
                    "proxyprotocol": False,
                },
                {
                    "destination_port": 80,
                    "health_check": {
                        "http": {
                            "domain": "example.com",
                            "path": "/",
                            "response": '{"status": "ok"}',
                            "status_codes": ["string", "string", "string"],
                            "tls": False,
                        },
                        "interval": 15,
                        "port": 4711,
                        "protocol": "http",
                        "retries": 3,
                        "timeout": 10,
                    },
                    "http": {
                        "certificates": [0, 0, 0],
                        "cookie_lifetime": 300,
                        "cookie_name": "HCLBSTICKY",
                        "redirect_http": True,
                        "sticky_sessions": True,
                    },
                    "listen_port": 443,
                    "protocol": "https",
                    "proxyprotocol": False,
                },
                {
                    "destination_port": 80,
                    "health_check": {
                        "http": {
                            "domain": "example.com",
                            "path": "/",
                            "response": '{"status": "ok"}',
                            "status_codes": ["string", "string", "string"],
                            "tls": False,
                        },
                        "interval": 15,
                        "port": 4711,
                        "protocol": "http",
                        "retries": 3,
                        "timeout": 10,
                    },
                    "http": {
                        "certificates": [0, 0, 0],
                        "cookie_lifetime": 300,
                        "cookie_name": "HCLBSTICKY",
                        "redirect_http": True,
                        "sticky_sessions": True,
                    },
                    "listen_port": 443,
                    "protocol": "https",
                    "proxyprotocol": False,
                },
            ],
            targets=[
                {
                    "health_status": [
                        {
                            "listen_port": 443,
                            "status": "healthy",
                        },
                        {
                            "listen_port": 443,
                            "status": "healthy",
                        },
                        {
                            "listen_port": 443,
                            "status": "healthy",
                        },
                    ],
                    "ip": {"ip": "203.0.113.1"},
                    "label_selector": {"selector": "env=prod"},
                    "server": {"id": 42},
                    "targets": [
                        {
                            "health_status": [
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                            ],
                            "server": {"id": 42},
                            "type": "server",
                            "use_private_ip": True,
                        },
                        {
                            "health_status": [
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                            ],
                            "server": {"id": 42},
                            "type": "server",
                            "use_private_ip": True,
                        },
                        {
                            "health_status": [
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                            ],
                            "server": {"id": 42},
                            "type": "server",
                            "use_private_ip": True,
                        },
                    ],
                    "type": "ip",
                    "use_private_ip": True,
                },
                {
                    "health_status": [
                        {
                            "listen_port": 443,
                            "status": "healthy",
                        },
                        {
                            "listen_port": 443,
                            "status": "healthy",
                        },
                        {
                            "listen_port": 443,
                            "status": "healthy",
                        },
                    ],
                    "ip": {"ip": "203.0.113.1"},
                    "label_selector": {"selector": "env=prod"},
                    "server": {"id": 42},
                    "targets": [
                        {
                            "health_status": [
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                            ],
                            "server": {"id": 42},
                            "type": "server",
                            "use_private_ip": True,
                        },
                        {
                            "health_status": [
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                            ],
                            "server": {"id": 42},
                            "type": "server",
                            "use_private_ip": True,
                        },
                        {
                            "health_status": [
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                            ],
                            "server": {"id": 42},
                            "type": "server",
                            "use_private_ip": True,
                        },
                    ],
                    "type": "ip",
                    "use_private_ip": True,
                },
                {
                    "health_status": [
                        {
                            "listen_port": 443,
                            "status": "healthy",
                        },
                        {
                            "listen_port": 443,
                            "status": "healthy",
                        },
                        {
                            "listen_port": 443,
                            "status": "healthy",
                        },
                    ],
                    "ip": {"ip": "203.0.113.1"},
                    "label_selector": {"selector": "env=prod"},
                    "server": {"id": 42},
                    "targets": [
                        {
                            "health_status": [
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                            ],
                            "server": {"id": 42},
                            "type": "server",
                            "use_private_ip": True,
                        },
                        {
                            "health_status": [
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                            ],
                            "server": {"id": 42},
                            "type": "server",
                            "use_private_ip": True,
                        },
                        {
                            "health_status": [
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                                {
                                    "listen_port": 443,
                                    "status": "healthy",
                                },
                            ],
                            "server": {"id": 42},
                            "type": "server",
                            "use_private_ip": True,
                        },
                    ],
                    "type": "ip",
                    "use_private_ip": True,
                },
            ],
        )
        assert_matches_type(LoadBalancerCreateResponse, load_balancer, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncHetzner) -> None:
        load_balancer = await client.load_balancers.retrieve(
            0,
        )
        assert_matches_type(LoadBalancerRetrieveResponse, load_balancer, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncHetzner) -> None:
        load_balancer = await client.load_balancers.update(
            0,
        )
        assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncHetzner) -> None:
        load_balancer = await client.load_balancers.update(
            0,
            labels={"foo": "string"},
            name="new-name",
        )
        assert_matches_type(LoadBalancerUpdateResponse, load_balancer, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncHetzner) -> None:
        load_balancer = await client.load_balancers.list()
        assert_matches_type(LoadBalancerListResponse, load_balancer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncHetzner) -> None:
        load_balancer = await client.load_balancers.list(
            label_selector="string",
            name="string",
            page=1,
            per_page=1,
            sort="id",
        )
        assert_matches_type(LoadBalancerListResponse, load_balancer, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncHetzner) -> None:
        load_balancer = await client.load_balancers.delete(
            0,
        )
        assert load_balancer is None
