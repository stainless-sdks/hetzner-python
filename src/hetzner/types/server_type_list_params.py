# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ServerTypeListParams"]


class ServerTypeListParams(TypedDict, total=False):
    name: str
    """Can be used to filter Server types by their name.

    The response will only contain the Server type matching the specified name.
    """

    page: int
    """Specifies the page to fetch. The number of the first page is 1"""

    per_page: int
    """Specifies the number of items returned per page.

    The default value is 25, the maximum value is 50 except otherwise specified in
    the documentation.
    """
