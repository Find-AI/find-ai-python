# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from find_ai import FindAI, AsyncFindAI
from find_ai._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: FindAI, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/searches").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        search = client.searches.create()
        assert search.is_closed
        assert search.json() == {"foo": "bar"}
        assert cast(Any, search.is_closed) is True
        assert isinstance(search, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_with_all_params(self, client: FindAI, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/searches").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        search = client.searches.create(
            max_matches=0,
            query="query",
            result_mode="result_mode",
            scope="scope",
        )
        assert search.is_closed
        assert search.json() == {"foo": "bar"}
        assert cast(Any, search.is_closed) is True
        assert isinstance(search, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: FindAI, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/searches").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        search = client.searches.with_raw_response.create()

        assert search.is_closed is True
        assert search.http_request.headers.get("X-Stainless-Lang") == "python"
        assert search.json() == {"foo": "bar"}
        assert isinstance(search, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: FindAI, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/searches").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.searches.with_streaming_response.create() as search:
            assert not search.is_closed
            assert search.http_request.headers.get("X-Stainless-Lang") == "python"

            assert search.json() == {"foo": "bar"}
            assert cast(Any, search.is_closed) is True
            assert isinstance(search, StreamedBinaryAPIResponse)

        assert cast(Any, search.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: FindAI) -> None:
        search = client.searches.retrieve(
            "id",
        )
        assert search is None

    @parametrize
    def test_raw_response_retrieve(self, client: FindAI) -> None:
        response = client.searches.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert search is None

    @parametrize
    def test_streaming_response_retrieve(self, client: FindAI) -> None:
        with client.searches.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert search is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: FindAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.searches.with_raw_response.retrieve(
                "",
            )


class TestAsyncSearches:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncFindAI, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/searches").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        search = await async_client.searches.create()
        assert search.is_closed
        assert await search.json() == {"foo": "bar"}
        assert cast(Any, search.is_closed) is True
        assert isinstance(search, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_with_all_params(self, async_client: AsyncFindAI, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/searches").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        search = await async_client.searches.create(
            max_matches=0,
            query="query",
            result_mode="result_mode",
            scope="scope",
        )
        assert search.is_closed
        assert await search.json() == {"foo": "bar"}
        assert cast(Any, search.is_closed) is True
        assert isinstance(search, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncFindAI, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/searches").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        search = await async_client.searches.with_raw_response.create()

        assert search.is_closed is True
        assert search.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await search.json() == {"foo": "bar"}
        assert isinstance(search, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncFindAI, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/searches").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.searches.with_streaming_response.create() as search:
            assert not search.is_closed
            assert search.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await search.json() == {"foo": "bar"}
            assert cast(Any, search.is_closed) is True
            assert isinstance(search, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, search.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFindAI) -> None:
        search = await async_client.searches.retrieve(
            "id",
        )
        assert search is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFindAI) -> None:
        response = await async_client.searches.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert search is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFindAI) -> None:
        async with async_client.searches.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert search is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFindAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.searches.with_raw_response.retrieve(
                "",
            )
