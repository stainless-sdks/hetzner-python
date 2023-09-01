# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from ...types import shared_params

__all__ = ["ActionListParams"]


class ActionListParams(TypedDict, total=False):
    page: int
    """Specifies the page to fetch. The number of the first page is 1"""

    per_page: int
    """Specifies the number of items returned per page.

    The default value is 25, the maximum value is 50 except otherwise specified in
    the documentation.
    """

    sort: shared_params.SortParam
    """Can be used multiple times."""

    status: shared_params.StatusParam
    """
    Can be used multiple times, the response will contain only Actions with
    specified statuses
    """
