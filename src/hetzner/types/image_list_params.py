# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ImageListParams"]


class ImageListParams(TypedDict, total=False):
    architecture: str
    """Return only Images with the given architecture."""

    bound_to: str
    """Can be used multiple times.

    Server ID linked to the Image. Only available for Images of type `backup`
    """

    include_deprecated: bool
    """Can be used multiple times."""

    label_selector: str
    """Can be used to filter resources by labels.

    The response will only contain resources matching the label selector.
    """

    name: str
    """Can be used to filter resources by their name.

    The response will only contain the resources matching the specified name
    """

    page: int
    """Specifies the page to fetch. The number of the first page is 1"""

    per_page: int
    """Specifies the number of items returned per page.

    The default value is 25, the maximum value is 50 except otherwise specified in
    the documentation.
    """

    sort: Literal["id", "id:asc", "id:desc", "name", "name:asc", "name:desc", "created", "created:asc", "created:desc"]
    """Can be used multiple times."""

    status: Literal["available", "creating"]
    """Can be used multiple times.

    The response will only contain Images matching the status.
    """

    type: Literal["system", "snapshot", "backup", "app"]
    """Can be used multiple times."""
