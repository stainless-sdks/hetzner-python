# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List
from typing_extensions import Literal

from ...types import (
    CertificateListResponse,
    CertificateCreateResponse,
    CertificateUpdateResponse,
    CertificateRetrieveResponse,
    certificate_list_params,
    certificate_create_params,
    certificate_update_params,
)
from .actions import Actions, AsyncActions
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Hetzner, AsyncHetzner

__all__ = ["Certificates", "AsyncCertificates"]


class Certificates(SyncAPIResource):
    actions: Actions

    def __init__(self, client: Hetzner) -> None:
        super().__init__(client)
        self.actions = Actions(client)

    def create(
        self,
        *,
        name: str,
        certificate: str | NotGiven = NOT_GIVEN,
        domain_names: List[str] | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        private_key: str | NotGiven = NOT_GIVEN,
        type: Literal["managed", "uploaded"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CertificateCreateResponse:
        """
        Creates a new Certificate.

        The default type **uploaded** allows for uploading your existing `certificate`
        and `private_key` in PEM format. You have to monitor its expiration date and
        handle renewal yourself.

        In contrast, type **managed** requests a new Certificate from _Let's Encrypt_
        for the specified `domain_names`. Only domains managed by _Hetzner DNS_ are
        supported. We handle renewal and timely alert the project owner via email if
        problems occur.

        For type `managed` Certificates the `action` key of the response contains the
        Action that allows for tracking the issuance process. For type `uploaded`
        Certificates the `action` is always null.

        Args:
          name: Name of the Certificate

          certificate: Certificate and chain in PEM format, in order so that each record directly
              certifies the one preceding. Required for type `uploaded` Certificates.

          domain_names: Domains and subdomains that should be contained in the Certificate issued by
              _Let's Encrypt_. Required for type `managed` Certificates.

          labels: User-defined labels (key-value pairs)

          private_key: Certificate key in PEM format. Required for type `uploaded` Certificates.

          type: Choose between uploading a Certificate in PEM format or requesting a managed
              _Let's Encrypt_ Certificate. If omitted defaults to `uploaded`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/certificates",
            body=maybe_transform(
                {
                    "name": name,
                    "certificate": certificate,
                    "domain_names": domain_names,
                    "labels": labels,
                    "private_key": private_key,
                    "type": type,
                },
                certificate_create_params.CertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CertificateCreateResponse,
        )

    def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CertificateRetrieveResponse:
        """
        Gets a specific Certificate object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/certificates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CertificateRetrieveResponse,
        )

    def update(
        self,
        id: int,
        *,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CertificateUpdateResponse:
        """
        Updates the Certificate properties.

        Note that when updating labels, the Certificate’s current set of labels will be
        replaced with the labels provided in the request body. So, for example, if you
        want to add a new label, you have to provide all existing labels plus the new
        label in the request body.

        Note: if the Certificate object changes during the request, the response will be
        a “conflict” error.

        Args:
          labels: User-defined labels (key-value pairs)

          name: New Certificate name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/certificates/{id}",
            body=maybe_transform(
                {
                    "labels": labels,
                    "name": name,
                },
                certificate_update_params.CertificateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CertificateUpdateResponse,
        )

    def list(
        self,
        *,
        label_selector: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal[
            "id", "id:asc", "id:desc", "name", "name:asc", "name:desc", "created", "created:asc", "created:desc"
        ]
        | NotGiven = NOT_GIVEN,
        type: Literal["uploaded", "managed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CertificateListResponse:
        """
        Returns all Certificate objects.

        Args:
          label_selector: Can be used to filter resources by labels. The response will only contain
              resources matching the label selector.

          name: Can be used to filter resources by their name. The response will only contain
              the resources matching the specified name

          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          sort: Can be used multiple times.

          type: Can be used multiple times. The response will only contain Certificates matching
              the type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/certificates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "label_selector": label_selector,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "type": type,
                    },
                    certificate_list_params.CertificateListParams,
                ),
            ),
            cast_to=CertificateListResponse,
        )

    def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a Certificate.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/certificates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCertificates(AsyncAPIResource):
    actions: AsyncActions

    def __init__(self, client: AsyncHetzner) -> None:
        super().__init__(client)
        self.actions = AsyncActions(client)

    async def create(
        self,
        *,
        name: str,
        certificate: str | NotGiven = NOT_GIVEN,
        domain_names: List[str] | NotGiven = NOT_GIVEN,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        private_key: str | NotGiven = NOT_GIVEN,
        type: Literal["managed", "uploaded"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CertificateCreateResponse:
        """
        Creates a new Certificate.

        The default type **uploaded** allows for uploading your existing `certificate`
        and `private_key` in PEM format. You have to monitor its expiration date and
        handle renewal yourself.

        In contrast, type **managed** requests a new Certificate from _Let's Encrypt_
        for the specified `domain_names`. Only domains managed by _Hetzner DNS_ are
        supported. We handle renewal and timely alert the project owner via email if
        problems occur.

        For type `managed` Certificates the `action` key of the response contains the
        Action that allows for tracking the issuance process. For type `uploaded`
        Certificates the `action` is always null.

        Args:
          name: Name of the Certificate

          certificate: Certificate and chain in PEM format, in order so that each record directly
              certifies the one preceding. Required for type `uploaded` Certificates.

          domain_names: Domains and subdomains that should be contained in the Certificate issued by
              _Let's Encrypt_. Required for type `managed` Certificates.

          labels: User-defined labels (key-value pairs)

          private_key: Certificate key in PEM format. Required for type `uploaded` Certificates.

          type: Choose between uploading a Certificate in PEM format or requesting a managed
              _Let's Encrypt_ Certificate. If omitted defaults to `uploaded`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/certificates",
            body=maybe_transform(
                {
                    "name": name,
                    "certificate": certificate,
                    "domain_names": domain_names,
                    "labels": labels,
                    "private_key": private_key,
                    "type": type,
                },
                certificate_create_params.CertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CertificateCreateResponse,
        )

    async def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CertificateRetrieveResponse:
        """
        Gets a specific Certificate object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/certificates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CertificateRetrieveResponse,
        )

    async def update(
        self,
        id: int,
        *,
        labels: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CertificateUpdateResponse:
        """
        Updates the Certificate properties.

        Note that when updating labels, the Certificate’s current set of labels will be
        replaced with the labels provided in the request body. So, for example, if you
        want to add a new label, you have to provide all existing labels plus the new
        label in the request body.

        Note: if the Certificate object changes during the request, the response will be
        a “conflict” error.

        Args:
          labels: User-defined labels (key-value pairs)

          name: New Certificate name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/certificates/{id}",
            body=maybe_transform(
                {
                    "labels": labels,
                    "name": name,
                },
                certificate_update_params.CertificateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CertificateUpdateResponse,
        )

    async def list(
        self,
        *,
        label_selector: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal[
            "id", "id:asc", "id:desc", "name", "name:asc", "name:desc", "created", "created:asc", "created:desc"
        ]
        | NotGiven = NOT_GIVEN,
        type: Literal["uploaded", "managed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CertificateListResponse:
        """
        Returns all Certificate objects.

        Args:
          label_selector: Can be used to filter resources by labels. The response will only contain
              resources matching the label selector.

          name: Can be used to filter resources by their name. The response will only contain
              the resources matching the specified name

          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          sort: Can be used multiple times.

          type: Can be used multiple times. The response will only contain Certificates matching
              the type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/certificates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "label_selector": label_selector,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "type": type,
                    },
                    certificate_list_params.CertificateListParams,
                ),
            ),
            cast_to=CertificateListResponse,
        )

    async def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a Certificate.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/certificates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )
