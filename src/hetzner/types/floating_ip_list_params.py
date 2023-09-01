# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FloatingIpListParams"]


class FloatingIpListParams(TypedDict, total=False):
    label_selector: str
    """Can be used to filter Floating IPs by labels.

    The response will only contain Floating IPs matching the label selector.
    """

    name: str
    """Can be used to filter Floating IPs by their name.

    The response will only contain the Floating IP matching the specified name.
    """

    page: int
    """Specifies the page to fetch. The number of the first page is 1"""

    per_page: int
    """Specifies the number of items returned per page.

    The default value is 25, the maximum value is 50 except otherwise specified in
    the documentation.
    """

    sort: Literal["id", "id:asc", "id:desc", "created", "created:asc", "created:desc"]
    """Can be used multiple times.

    Choices id id:asc id:desc created created:asc created:desc
    """
