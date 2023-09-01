# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ResponseMeta", "Pagination"]


class Pagination(BaseModel):
    last_page: Optional[int]
    """ID of the last page available.

    Can be null if the current page is the last one. | The last page number
    """

    next_page: Optional[int]
    """ID of the next page.

    Can be null if the current page is the last one. | The next page number
    """

    page: int
    """Current page number | The current page number"""

    per_page: int
    """
    Maximum number of items shown per page in the response | The number of entries
    per page
    """

    previous_page: Optional[int]
    """ID of the previous page.

    Can be null if the current page is the first one. | The previous page number
    """

    total_entries: Optional[int]
    """The total number of entries that exist in the database for this query.

    Nullable if unknown. | The total number of entries
    """


class ResponseMeta(BaseModel):
    pagination: Pagination
    """Information about the current pagination.

    The keys previous_page, next_page, last_page, and total_entries may be null when
    on the first page, last page, or when the total number of entries is unknown
    """
