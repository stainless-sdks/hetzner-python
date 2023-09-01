# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List

from ...types import RuleParam, shared_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.firewalls import (
    ActionListResponse,
    ActionRetrieveResponse,
    ActionSetRulesResponse,
    ActionApplyToResourcesResponse,
    ActionRemoveFromResourcesResponse,
    action_list_params,
    action_set_rules_params,
    action_apply_to_resources_params,
    action_remove_from_resources_params,
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
        """
        Returns a specific Action for a Firewall.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/firewalls/{id}/actions/{action_id}",
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
        """Returns all Action objects for a Firewall.

        You can sort the results by using the
        `sort` URI parameter, and filter them with the `status` parameter.

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
            f"/firewalls/{id}/actions",
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

    def apply_to_resources(
        self,
        id: int,
        *,
        apply_to: List[action_apply_to_resources_params.ApplyTo],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionApplyToResourcesResponse:
        """
        Applies one Firewall to multiple resources.

        Currently servers (public network interface) and label selectors are supported.

        #### Call specific error codes

        | Code                          | Description                                                   |
        | ----------------------------- | ------------------------------------------------------------- |
        | `firewall_already_applied`    | Firewall was already applied on resource                      |
        | `incompatible_network_type`   | The Network type is incompatible for the given resource       |
        | `firewall_resource_not_found` | The resource the Firewall should be attached to was not found |

        Args:
          apply_to: Resources the Firewall should be applied to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/firewalls/{id}/actions/apply_to_resources",
            body=maybe_transform({"apply_to": apply_to}, action_apply_to_resources_params.ActionApplyToResourcesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionApplyToResourcesResponse,
        )

    def remove_from_resources(
        self,
        id: int,
        *,
        remove_from: List[action_remove_from_resources_params.RemoveFrom],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionRemoveFromResourcesResponse:
        """
        Removes one Firewall from multiple resources.

        Currently only Servers (and their public network interfaces) are supported.

        #### Call specific error codes

        | Code                                 | Description                                                            |
        | ------------------------------------ | ---------------------------------------------------------------------- |
        | `firewall_already_removed`           | Firewall was already removed from the resource                         |
        | `firewall_resource_not_found`        | The resource the Firewall should be attached to was not found          |
        | `firewall_managed_by_label_selector` | Firewall was applied via label selector and cannot be removed manually |

        Args:
          remove_from: Resources the Firewall should be removed from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/firewalls/{id}/actions/remove_from_resources",
            body=maybe_transform(
                {"remove_from": remove_from}, action_remove_from_resources_params.ActionRemoveFromResourcesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRemoveFromResourcesResponse,
        )

    def set_rules(
        self,
        id: int,
        *,
        rules: List[RuleParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionSetRulesResponse:
        """Sets the rules of a Firewall.

        All existing rules will be overwritten.

        Pass an empty `rules` array to remove
        all rules. The maximum amount of rules that can be defined is 50.

        #### Call specific error codes

        | Code                          | Description                                                   |
        | ----------------------------- | ------------------------------------------------------------- |
        | `firewall_resource_not_found` | The resource the Firewall should be attached to was not found |

        Args:
          rules: Array of rules

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/firewalls/{id}/actions/set_rules",
            body=maybe_transform({"rules": rules}, action_set_rules_params.ActionSetRulesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSetRulesResponse,
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
        """
        Returns a specific Action for a Firewall.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/firewalls/{id}/actions/{action_id}",
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
        """Returns all Action objects for a Firewall.

        You can sort the results by using the
        `sort` URI parameter, and filter them with the `status` parameter.

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
            f"/firewalls/{id}/actions",
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

    async def apply_to_resources(
        self,
        id: int,
        *,
        apply_to: List[action_apply_to_resources_params.ApplyTo],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionApplyToResourcesResponse:
        """
        Applies one Firewall to multiple resources.

        Currently servers (public network interface) and label selectors are supported.

        #### Call specific error codes

        | Code                          | Description                                                   |
        | ----------------------------- | ------------------------------------------------------------- |
        | `firewall_already_applied`    | Firewall was already applied on resource                      |
        | `incompatible_network_type`   | The Network type is incompatible for the given resource       |
        | `firewall_resource_not_found` | The resource the Firewall should be attached to was not found |

        Args:
          apply_to: Resources the Firewall should be applied to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/firewalls/{id}/actions/apply_to_resources",
            body=maybe_transform({"apply_to": apply_to}, action_apply_to_resources_params.ActionApplyToResourcesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionApplyToResourcesResponse,
        )

    async def remove_from_resources(
        self,
        id: int,
        *,
        remove_from: List[action_remove_from_resources_params.RemoveFrom],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionRemoveFromResourcesResponse:
        """
        Removes one Firewall from multiple resources.

        Currently only Servers (and their public network interfaces) are supported.

        #### Call specific error codes

        | Code                                 | Description                                                            |
        | ------------------------------------ | ---------------------------------------------------------------------- |
        | `firewall_already_removed`           | Firewall was already removed from the resource                         |
        | `firewall_resource_not_found`        | The resource the Firewall should be attached to was not found          |
        | `firewall_managed_by_label_selector` | Firewall was applied via label selector and cannot be removed manually |

        Args:
          remove_from: Resources the Firewall should be removed from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/firewalls/{id}/actions/remove_from_resources",
            body=maybe_transform(
                {"remove_from": remove_from}, action_remove_from_resources_params.ActionRemoveFromResourcesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRemoveFromResourcesResponse,
        )

    async def set_rules(
        self,
        id: int,
        *,
        rules: List[RuleParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ActionSetRulesResponse:
        """Sets the rules of a Firewall.

        All existing rules will be overwritten.

        Pass an empty `rules` array to remove
        all rules. The maximum amount of rules that can be defined is 50.

        #### Call specific error codes

        | Code                          | Description                                                   |
        | ----------------------------- | ------------------------------------------------------------- |
        | `firewall_resource_not_found` | The resource the Firewall should be attached to was not found |

        Args:
          rules: Array of rules

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/firewalls/{id}/actions/set_rules",
            body=maybe_transform({"rules": rules}, action_set_rules_params.ActionSetRulesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSetRulesResponse,
        )
