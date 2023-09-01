# File generated from our OpenAPI spec by Stainless.

from typing import List, Generic, TypeVar, Optional

from ._types import ModelT
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage
from .types.shared import ResponseMeta

__all__ = ["SyncFloatingIPsPage", "AsyncFloatingIPsPage", "SyncServersPage", "AsyncServersPage"]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)


class SyncFloatingIPsPage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    floating_ips: List[ModelT]
    meta: ResponseMeta

    def _get_page_items(self) -> List[ModelT]:
        return self.floating_ips

    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.meta.pagination.page
        return PageInfo(params={"page": current_page + 1})


class AsyncFloatingIPsPage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    floating_ips: List[ModelT]
    meta: ResponseMeta

    def _get_page_items(self) -> List[ModelT]:
        return self.floating_ips

    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.meta.pagination.page
        return PageInfo(params={"page": current_page + 1})


class SyncServersPage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    meta: ResponseMeta
    servers: List[ModelT]

    def _get_page_items(self) -> List[ModelT]:
        return self.servers

    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.meta.pagination.page
        return PageInfo(params={"page": current_page + 1})


class AsyncServersPage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    meta: ResponseMeta
    servers: List[ModelT]

    def _get_page_items(self) -> List[ModelT]:
        return self.servers

    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.meta.pagination.page
        return PageInfo(params={"page": current_page + 1})
