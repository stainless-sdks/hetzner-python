# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["VolumeCreateParams"]


class VolumeCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the volume"""

    size: Required[int]
    """Size of the Volume in GB"""

    automount: bool
    """Auto-mount Volume after attach. `server` must be provided."""

    format: str
    """Format Volume after creation. One of: `xfs`, `ext4`"""

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    location: str
    """Location to create the Volume in (can be omitted if Server is specified)"""

    server: int
    """
    Server to which to attach the Volume once it's created (Volume will be created
    in the same Location as the server)
    """
