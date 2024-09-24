# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import search_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["SearchesResource", "AsyncSearchesResource"]


class SearchesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/find-ai-python#accessing-raw-response-data-eg-headers
        """
        return SearchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/find-ai-python#with_streaming_response
        """
        return SearchesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        max_matches: float | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        result_mode: str | NotGiven = NOT_GIVEN,
        scope: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """Starts a search.

        Args:
          max_matches: The maximum number of results to return.

        optional for result_mode exact

          query: Search query.

          result_mode: The mode of the search. Valid values are 'exact' or 'best'.

          scope: The scope of the search. Valid values are 'people' or 'companies'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/searches",
            body=maybe_transform(
                {
                    "max_matches": max_matches,
                    "query": query,
                    "result_mode": result_mode,
                    "scope": scope,
                },
                search_create_params.SearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The endpoint to poll to check the latest results of a search.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/v1/searches/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSearchesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/find-ai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/find-ai-python#with_streaming_response
        """
        return AsyncSearchesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        max_matches: float | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        result_mode: str | NotGiven = NOT_GIVEN,
        scope: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """Starts a search.

        Args:
          max_matches: The maximum number of results to return.

        optional for result_mode exact

          query: Search query.

          result_mode: The mode of the search. Valid values are 'exact' or 'best'.

          scope: The scope of the search. Valid values are 'people' or 'companies'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/searches",
            body=await async_maybe_transform(
                {
                    "max_matches": max_matches,
                    "query": query,
                    "result_mode": result_mode,
                    "scope": scope,
                },
                search_create_params.SearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The endpoint to poll to check the latest results of a search.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/v1/searches/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SearchesResourceWithRawResponse:
    def __init__(self, searches: SearchesResource) -> None:
        self._searches = searches

        self.create = to_custom_raw_response_wrapper(
            searches.create,
            BinaryAPIResponse,
        )
        self.retrieve = to_raw_response_wrapper(
            searches.retrieve,
        )


class AsyncSearchesResourceWithRawResponse:
    def __init__(self, searches: AsyncSearchesResource) -> None:
        self._searches = searches

        self.create = async_to_custom_raw_response_wrapper(
            searches.create,
            AsyncBinaryAPIResponse,
        )
        self.retrieve = async_to_raw_response_wrapper(
            searches.retrieve,
        )


class SearchesResourceWithStreamingResponse:
    def __init__(self, searches: SearchesResource) -> None:
        self._searches = searches

        self.create = to_custom_streamed_response_wrapper(
            searches.create,
            StreamedBinaryAPIResponse,
        )
        self.retrieve = to_streamed_response_wrapper(
            searches.retrieve,
        )


class AsyncSearchesResourceWithStreamingResponse:
    def __init__(self, searches: AsyncSearchesResource) -> None:
        self._searches = searches

        self.create = async_to_custom_streamed_response_wrapper(
            searches.create,
            AsyncStreamedBinaryAPIResponse,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            searches.retrieve,
        )
