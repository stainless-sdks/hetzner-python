# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...types import shared_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.certificates import (
    ActionListResponse,
    ActionRetryResponse,
    ActionRetrieveResponse,
    action_list_params,
)

__all__ = ["Actions", "AsyncActions"]


class Actions(SyncAPIResource):
    def retrieve(
        self,
        action_id: int,
        *,
        id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionRetrieveResponse:
        """Returns a specific Action for a Certificate.

        Only type `managed` Certificates
        have Actions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/certificates/{id}/actions/{action_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRetrieveResponse,
        )

    def list(
        self,
        id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: shared_params.SortParam | NotGiven = NOT_GIVEN,
        status: shared_params.StatusParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionListResponse:
        """Returns all Action objects for a Certificate.

        You can sort the results by using
        the `sort` URI parameter, and filter them with the `status` parameter.

        Only type `managed` Certificates can have Actions. For type `uploaded`
        Certificates the `actions` key will always contain an empty array.

        Args:
          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          sort: Can be used multiple times.

          status: Can be used multiple times, the response will contain only Actions with
              specified statuses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/certificates/{id}/actions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "status": status,
                    },
                    action_list_params.ActionListParams,
                ),
            ),
            cast_to=ActionListResponse,
        )

    def retry(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionRetryResponse:
        """
        Retry a failed Certificate issuance or renewal.

        Only applicable if the type of the Certificate is `managed` and the issuance or
        renewal status is `failed`.

        #### Call specific error codes

        | Code                                                    | Description                                                               |
        | ------------------------------------------------------- | ------------------------------------------------------------------------- |
        | `caa_record_does_not_allow_ca`                          | CAA record does not allow certificate authority                           |
        | `ca_dns_validation_failed`                              | Certificate Authority: DNS validation failed                              |
        | `ca_too_many_authorizations_failed_recently`            | Certificate Authority: Too many authorizations failed recently            |
        | `ca_too_many_certificates_issued_for_registered_domain` | Certificate Authority: Too many certificates issued for registered domain |
        | `ca_too_many_duplicate_certificates`                    | Certificate Authority: Too many duplicate certificates                    |
        | `could_not_verify_domain_delegated_to_zone`             | Could not verify domain delegated to zone                                 |
        | `dns_zone_not_found`                                    | DNS zone not found                                                        |
        | `dns_zone_is_secondary_zone`                            | DNS zone is a secondary zone                                              |

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/certificates/{id}/actions/retry",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRetryResponse,
        )


class AsyncActions(AsyncAPIResource):
    async def retrieve(
        self,
        action_id: int,
        *,
        id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionRetrieveResponse:
        """Returns a specific Action for a Certificate.

        Only type `managed` Certificates
        have Actions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/certificates/{id}/actions/{action_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRetrieveResponse,
        )

    async def list(
        self,
        id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: shared_params.SortParam | NotGiven = NOT_GIVEN,
        status: shared_params.StatusParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionListResponse:
        """Returns all Action objects for a Certificate.

        You can sort the results by using
        the `sort` URI parameter, and filter them with the `status` parameter.

        Only type `managed` Certificates can have Actions. For type `uploaded`
        Certificates the `actions` key will always contain an empty array.

        Args:
          page: Specifies the page to fetch. The number of the first page is 1

          per_page: Specifies the number of items returned per page. The default value is 25, the
              maximum value is 50 except otherwise specified in the documentation.

          sort: Can be used multiple times.

          status: Can be used multiple times, the response will contain only Actions with
              specified statuses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/certificates/{id}/actions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "status": status,
                    },
                    action_list_params.ActionListParams,
                ),
            ),
            cast_to=ActionListResponse,
        )

    async def retry(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionRetryResponse:
        """
        Retry a failed Certificate issuance or renewal.

        Only applicable if the type of the Certificate is `managed` and the issuance or
        renewal status is `failed`.

        #### Call specific error codes

        | Code                                                    | Description                                                               |
        | ------------------------------------------------------- | ------------------------------------------------------------------------- |
        | `caa_record_does_not_allow_ca`                          | CAA record does not allow certificate authority                           |
        | `ca_dns_validation_failed`                              | Certificate Authority: DNS validation failed                              |
        | `ca_too_many_authorizations_failed_recently`            | Certificate Authority: Too many authorizations failed recently            |
        | `ca_too_many_certificates_issued_for_registered_domain` | Certificate Authority: Too many certificates issued for registered domain |
        | `ca_too_many_duplicate_certificates`                    | Certificate Authority: Too many duplicate certificates                    |
        | `could_not_verify_domain_delegated_to_zone`             | Could not verify domain delegated to zone                                 |
        | `dns_zone_not_found`                                    | DNS zone not found                                                        |
        | `dns_zone_is_secondary_zone`                            | DNS zone is a secondary zone                                              |

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/certificates/{id}/actions/retry",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRetryResponse,
        )
