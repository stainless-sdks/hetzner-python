# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
import asyncio
from typing import Union, Mapping, Optional

import httpx

from . import resources
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._version import __version__
from ._streaming import Stream as Stream
from ._streaming import AsyncStream as AsyncStream
from ._base_client import (
    DEFAULT_LIMITS,
    DEFAULT_TIMEOUT,
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Hetzner",
    "AsyncHetzner",
    "Client",
    "AsyncClient",
]


class Hetzner(SyncAPIClient):
    actions: resources.Actions
    certificates: resources.Certificates
    datacenters: resources.Datacenters
    firewalls: resources.Firewalls
    floating_ips: resources.FloatingIps
    images: resources.Images
    isos: resources.Isos
    load_balancer_types: resources.LoadBalancerTypes
    load_balancers: resources.LoadBalancers
    locations: resources.Locations
    networks: resources.Networks
    placement_groups: resources.PlacementGroups
    pricing: resources.Pricing
    primary_ips: resources.PrimaryIps
    server_types: resources.ServerTypes
    servers: resources.Servers
    ssh_keys: resources.SshKeys
    volumes: resources.Volumes

    # client options
    api_token: str

    def __init__(
        self,
        *,
        base_url: Optional[str] = None,
        api_token: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Optional[Transport] = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: Optional[ProxiesTypes] = None,
        # See httpx documentation for [limits](https://www.python-httpx.org/advanced/#pool-limit-configuration)
        connection_pool_limits: httpx.Limits | None = DEFAULT_LIMITS,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous hetzner client instance.

        This automatically infers the `api_token` argument from the `HETZNER_API_TOKEN` environment variable if it is not provided.
        """
        api_token = api_token or os.environ.get("HETZNER_API_TOKEN", None)
        if not api_token:
            raise Exception(
                "The api_token client option must be set either by passing api_token to the client or by setting the HETZNER_API_TOKEN environment variable"
            )
        self.api_token = api_token

        if base_url is None:
            base_url = f"https://api.hetzner.cloud/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            transport=transport,
            proxies=proxies,
            limits=connection_pool_limits,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.actions = resources.Actions(self)
        self.certificates = resources.Certificates(self)
        self.datacenters = resources.Datacenters(self)
        self.firewalls = resources.Firewalls(self)
        self.floating_ips = resources.FloatingIps(self)
        self.images = resources.Images(self)
        self.isos = resources.Isos(self)
        self.load_balancer_types = resources.LoadBalancerTypes(self)
        self.load_balancers = resources.LoadBalancers(self)
        self.locations = resources.Locations(self)
        self.networks = resources.Networks(self)
        self.placement_groups = resources.PlacementGroups(self)
        self.pricing = resources.Pricing(self)
        self.primary_ips = resources.PrimaryIps(self)
        self.server_types = resources.ServerTypes(self)
        self.servers = resources.Servers(self)
        self.ssh_keys = resources.SshKeys(self)
        self.volumes = resources.Volumes(self)

    @property
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    def auth_headers(self) -> dict[str, str]:
        api_token = self.api_token
        return {"Authorization": f"Bearer {api_token}"}

    def copy(
        self,
        *,
        api_token: str | None = None,
        base_url: str | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        connection_pool_limits: httpx.Limits | NotGiven = NOT_GIVEN,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
    ) -> Hetzner:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.

        It should be noted that this does not share the underlying httpx client class which may lead
        to performance issues.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        # TODO: share the same httpx client between instances
        return self.__class__(
            base_url=base_url or str(self.base_url),
            api_token=api_token or self.api_token,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            connection_pool_limits=self._limits
            if isinstance(connection_pool_limits, NotGiven)
            else connection_pool_limits,
            max_retries=self.max_retries if isinstance(max_retries, NotGiven) else max_retries,
            default_headers=headers,
            default_query=params,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def __del__(self) -> None:
        self.close()


class AsyncHetzner(AsyncAPIClient):
    actions: resources.AsyncActions
    certificates: resources.AsyncCertificates
    datacenters: resources.AsyncDatacenters
    firewalls: resources.AsyncFirewalls
    floating_ips: resources.AsyncFloatingIps
    images: resources.AsyncImages
    isos: resources.AsyncIsos
    load_balancer_types: resources.AsyncLoadBalancerTypes
    load_balancers: resources.AsyncLoadBalancers
    locations: resources.AsyncLocations
    networks: resources.AsyncNetworks
    placement_groups: resources.AsyncPlacementGroups
    pricing: resources.AsyncPricing
    primary_ips: resources.AsyncPrimaryIps
    server_types: resources.AsyncServerTypes
    servers: resources.AsyncServers
    ssh_keys: resources.AsyncSshKeys
    volumes: resources.AsyncVolumes

    # client options
    api_token: str

    def __init__(
        self,
        *,
        base_url: Optional[str] = None,
        api_token: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Optional[Transport] = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: Optional[ProxiesTypes] = None,
        # See httpx documentation for [limits](https://www.python-httpx.org/advanced/#pool-limit-configuration)
        connection_pool_limits: httpx.Limits | None = DEFAULT_LIMITS,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async hetzner client instance.

        This automatically infers the `api_token` argument from the `HETZNER_API_TOKEN` environment variable if it is not provided.
        """
        api_token = api_token or os.environ.get("HETZNER_API_TOKEN", None)
        if not api_token:
            raise Exception(
                "The api_token client option must be set either by passing api_token to the client or by setting the HETZNER_API_TOKEN environment variable"
            )
        self.api_token = api_token

        if base_url is None:
            base_url = f"https://api.hetzner.cloud/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            transport=transport,
            proxies=proxies,
            limits=connection_pool_limits,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.actions = resources.AsyncActions(self)
        self.certificates = resources.AsyncCertificates(self)
        self.datacenters = resources.AsyncDatacenters(self)
        self.firewalls = resources.AsyncFirewalls(self)
        self.floating_ips = resources.AsyncFloatingIps(self)
        self.images = resources.AsyncImages(self)
        self.isos = resources.AsyncIsos(self)
        self.load_balancer_types = resources.AsyncLoadBalancerTypes(self)
        self.load_balancers = resources.AsyncLoadBalancers(self)
        self.locations = resources.AsyncLocations(self)
        self.networks = resources.AsyncNetworks(self)
        self.placement_groups = resources.AsyncPlacementGroups(self)
        self.pricing = resources.AsyncPricing(self)
        self.primary_ips = resources.AsyncPrimaryIps(self)
        self.server_types = resources.AsyncServerTypes(self)
        self.servers = resources.AsyncServers(self)
        self.ssh_keys = resources.AsyncSshKeys(self)
        self.volumes = resources.AsyncVolumes(self)

    @property
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    def auth_headers(self) -> dict[str, str]:
        api_token = self.api_token
        return {"Authorization": f"Bearer {api_token}"}

    def copy(
        self,
        *,
        api_token: str | None = None,
        base_url: str | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        connection_pool_limits: httpx.Limits | NotGiven = NOT_GIVEN,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
    ) -> AsyncHetzner:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.

        It should be noted that this does not share the underlying httpx client class which may lead
        to performance issues.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        # TODO: share the same httpx client between instances
        return self.__class__(
            base_url=base_url or str(self.base_url),
            api_token=api_token or self.api_token,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            connection_pool_limits=self._limits
            if isinstance(connection_pool_limits, NotGiven)
            else connection_pool_limits,
            max_retries=self.max_retries if isinstance(max_retries, NotGiven) else max_retries,
            default_headers=headers,
            default_query=params,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def __del__(self) -> None:
        try:
            asyncio.get_running_loop().create_task(self.close())
        except Exception:
            pass


Client = Hetzner

AsyncClient = AsyncHetzner
