# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PrimaryIpListParams"]


class PrimaryIpListParams(TypedDict, total=False):
    ip: str
    """Can be used to filter resources by their ip.

    The response will only contain the resources matching the specified ip.
    """

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

    sort: Literal["id", "id:asc", "id:desc", "created", "created:asc", "created:desc"]
    """Can be used multiple times.

    Choices id id:asc id:desc created created:asc created:desc
    """
