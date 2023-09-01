# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional
from typing_extensions import Literal

from ..shared import Action
from ..._models import BaseModel

__all__ = ["ActionCreateImageResponse", "Image", "ImageCreatedFrom", "ImageProtection"]


class ImageCreatedFrom(BaseModel):
    id: int
    """ID of the Server the Image was created from"""

    name: str
    """Server name at the time the Image was created"""


class ImageProtection(BaseModel):
    delete: bool
    """
    If true, prevents the Resource from being deleted | If true, prevents the
    Network from being deleted
    """


class Image(BaseModel):
    id: int
    """ID of the Resource"""

    architecture: Literal["arm", "x86"]
    """Type of cpu architecture this image is compatible with.

    | Type of cpu architecture
    """

    bound_to: Optional[int]
    """ID of Server the Image is bound to. Only set for Images of type `backup`."""

    created: str
    """Point in time when the Resource was created (in ISO-8601 format)"""

    created_from: Optional[ImageCreatedFrom]
    """Information about the Server the Image was created from"""

    deleted: Optional[str]
    """Point in time where the Image was deleted (in ISO-8601 format)"""

    deprecated: Optional[str]
    """
    Point in time when the Image is considered to be deprecated (in ISO-8601 format)
    """

    description: str
    """Description of the Image"""

    disk_size: float
    """Size of the disk contained in the Image in GB"""

    image_size: Optional[float]
    """Size of the Image file in our storage in GB.

    For snapshot Images this is the value relevant for calculating costs for the
    Image.
    """

    labels: Dict[str, str]
    """User-defined labels (key-value pairs)"""

    name: Optional[str]
    """Unique identifier of the Image. This value is only set for system Images."""

    os_flavor: Literal["alma", "centos", "debian", "fedora", "rocky", "ubuntu", "unknown"]
    """Flavor of operating system contained in the Image"""

    os_version: Optional[str]
    """Operating system version"""

    protection: ImageProtection
    """Protection configuration for the Resource"""

    status: Literal["available", "creating", "unavailable"]
    """Whether the Image can be used or if it's still being created or unavailable"""

    type: Literal["app", "backup", "snapshot", "system", "temporary"]
    """Type of the Image"""

    rapid_deploy: Optional[bool] = None
    """Indicates that rapid deploy of the Image is available"""


class ActionCreateImageResponse(BaseModel):
    action: Optional[Action] = None
    """Actions show the results and progress of asynchronous requests to the API."""

    image: Optional[Image] = None
