# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LoadBalancerServiceModel", "HealthCheck", "HealthCheckHTTP", "HTTP"]


class HealthCheckHTTP(BaseModel):
    domain: Optional[str]
    """Host header to send in the HTTP request.

    May not contain spaces, percent or backslash symbols. Can be null, in that case
    no host header is sent.
    """

    path: str
    """HTTP path to use for health checks.

    May not contain literal spaces, use percent-encoding instead.
    """

    response: Optional[str] = None
    """
    String that must be contained in HTTP response in order to pass the health check
    """

    status_codes: Optional[List[str]] = None
    """List of returned HTTP status codes in order to pass the health check.

    Supports the wildcards `?` for exactly one character and `*` for multiple ones.
    The default is to pass the health check for any status code between 2?? and 3??.
    """

    tls: Optional[bool] = None
    """Use HTTPS for health check"""


class HealthCheck(BaseModel):
    interval: int
    """Time interval in seconds health checks are performed"""

    port: int
    """Port the health check will be performed on"""

    protocol: Literal["http", "tcp"]
    """Type of the health check"""

    retries: int
    """
    Unsuccessful retries needed until a target is considered unhealthy; an unhealthy
    target needs the same number of successful retries to become healthy again
    """

    timeout: int
    """Time in seconds after an attempt is considered a timeout"""

    http: Optional[HealthCheckHTTP] = None
    """Additional configuration for protocol http"""


class HTTP(BaseModel):
    certificates: Optional[List[int]] = None
    """
    IDs of the Certificates to use for TLS/SSL termination by the Load Balancer;
    empty for TLS/SSL passthrough or if `protocol` is "http"
    """

    cookie_lifetime: Optional[int] = None
    """Lifetime of the cookie used for sticky sessions"""

    cookie_name: Optional[str] = None
    """Name of the cookie used for sticky sessions"""

    redirect_http: Optional[bool] = None
    """Redirect HTTP requests to HTTPS.

    Only available if protocol is "https". Default `false`
    """

    sticky_sessions: Optional[bool] = None
    """Use sticky sessions.

    Only available if protocol is "http" or "https". Default `false`
    """


class LoadBalancerServiceModel(BaseModel):
    destination_port: int
    """Port the Load Balancer will balance to"""

    health_check: HealthCheck
    """Service health check"""

    listen_port: int
    """Port the Load Balancer listens on"""

    protocol: Literal["http", "https", "tcp"]
    """Protocol of the Load Balancer"""

    proxyprotocol: bool
    """Is Proxyprotocol enabled or not"""

    http: Optional[HTTP] = None
    """Configuration option for protocols http and https"""
