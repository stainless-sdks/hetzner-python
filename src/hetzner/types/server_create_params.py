# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ServerCreateParams", "Firewall", "PublicNet"]


class ServerCreateParams(TypedDict, total=False):
    image: Required[str]
    """ID or name of the Image the Server is created from"""

    name: Required[str]
    """
    Name of the Server to create (must be unique per Project and a valid hostname as
    per RFC 1123)
    """

    server_type: Required[str]
    """ID or name of the Server type this Server should be created with"""

    automount: bool
    """Auto-mount Volumes after attach"""

    datacenter: str
    """
    ID or name of Datacenter to create Server in (must not be used together with
    location)
    """

    firewalls: List[Firewall]
    """
    Firewalls which should be applied on the Server's public network interface at
    creation time
    """

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    location: str
    """
    ID or name of Location to create Server in (must not be used together with
    datacenter)
    """

    networks: List[int]
    """
    Network IDs which should be attached to the Server private network interface at
    the creation time
    """

    placement_group: int
    """ID of the Placement Group the server should be in"""

    public_net: PublicNet
    """Public Network options"""

    ssh_keys: List[str]
    """
    SSH key IDs (`integer`) or names (`string`) which should be injected into the
    Server at creation time
    """

    start_after_create: bool
    """Start Server right after creation. Defaults to true."""

    user_data: str
    """Cloud-Init user data to use during Server creation.

    This field is limited to 32KiB.
    """

    volumes: List[int]
    """Volume IDs which should be attached to the Server at the creation time.

    Volumes must be in the same Location.
    """


class Firewall(TypedDict, total=False):
    firewall: Required[int]
    """ID of the Firewall"""


class PublicNet(TypedDict, total=False):
    enable_ipv4: bool
    """Attach an IPv4 on the public NIC.

    If false, no IPv4 address will be attached. Defaults to true.
    """

    enable_ipv6: bool
    """Attach an IPv6 on the public NIC.

    If false, no IPv6 address will be attached. Defaults to true.
    """

    ipv4: Optional[int]
    """ID of the ipv4 Primary IP to use.

    If omitted and enable_ipv4 is true, a new ipv4 Primary IP will automatically be
    created.
    """

    ipv6: Optional[int]
    """ID of the ipv6 Primary IP to use.

    If omitted and enable_ipv6 is true, a new ipv6 Primary IP will automatically be
    created.
    """
