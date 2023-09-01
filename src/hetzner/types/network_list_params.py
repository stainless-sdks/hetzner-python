# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NetworkListParams"]


class NetworkListParams(TypedDict, total=False):
    label_selector: str
    """Can be used to filter networks by labels.

    The response will only contain networks with a matching label selector pattern.
    """

    name: str
    """Can be used to filter networks by their name.

    The response will only contain the networks matching the specified name.
    """

    page: int
    """Specifies the page to fetch. The number of the first page is 1"""

    per_page: int
    """Specifies the number of items returned per page.

    The default value is 25, the maximum value is 50 except otherwise specified in
    the documentation.
    """
