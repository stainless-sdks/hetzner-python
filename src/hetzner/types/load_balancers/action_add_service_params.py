# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionAddServiceParams", "HealthCheck", "HealthCheckHTTP", "HTTP"]


class ActionAddServiceParams(TypedDict, total=False):
    destination_port: Required[int]
    """Port the Load Balancer will balance to"""

    health_check: Required[HealthCheck]
    """Service health check"""

    listen_port: Required[int]
    """Port the Load Balancer listens on"""

    protocol: Required[Literal["http", "https", "tcp"]]
    """Protocol of the Load Balancer"""

    proxyprotocol: Required[bool]
    """Is Proxyprotocol enabled or not"""

    http: HTTP
    """Configuration option for protocols http and https"""


class HealthCheckHTTP(TypedDict, total=False):
    domain: Required[Optional[str]]
    """Host header to send in the HTTP request.

    May not contain spaces, percent or backslash symbols. Can be null, in that case
    no host header is sent.
    """

    path: Required[str]
    """HTTP path to use for health checks.

    May not contain literal spaces, use percent-encoding instead.
    """

    response: str
    """
    String that must be contained in HTTP response in order to pass the health check
    """

    status_codes: List[str]
    """List of returned HTTP status codes in order to pass the health check.

    Supports the wildcards `?` for exactly one character and `*` for multiple ones.
    The default is to pass the health check for any status code between 2?? and 3??.
    """

    tls: bool
    """Use HTTPS for health check"""


class HealthCheck(TypedDict, total=False):
    interval: Required[int]
    """Time interval in seconds health checks are performed"""

    port: Required[int]
    """Port the health check will be performed on"""

    protocol: Required[Literal["http", "tcp"]]
    """Type of the health check"""

    retries: Required[int]
    """
    Unsuccessful retries needed until a target is considered unhealthy; an unhealthy
    target needs the same number of successful retries to become healthy again
    """

    timeout: Required[int]
    """Time in seconds after an attempt is considered a timeout"""

    http: HealthCheckHTTP
    """Additional configuration for protocol http"""


class HTTP(TypedDict, total=False):
    certificates: List[int]
    """
    IDs of the Certificates to use for TLS/SSL termination by the Load Balancer;
    empty for TLS/SSL passthrough or if `protocol` is "http"
    """

    cookie_lifetime: int
    """Lifetime of the cookie used for sticky sessions"""

    cookie_name: str
    """Name of the cookie used for sticky sessions"""

    redirect_http: bool
    """Redirect HTTP requests to HTTPS.

    Only available if protocol is "https". Default `false`
    """

    sticky_sessions: bool
    """Use sticky sessions.

    Only available if protocol is "http" or "https". Default `false`
    """
