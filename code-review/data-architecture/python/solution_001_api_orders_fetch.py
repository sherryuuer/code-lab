"""
Solution Example: Safer API Orders Fetch

This example focuses only on the API extraction part.
It demonstrates safer pagination, timeout, retry, and error handling.
"""

import os
import time
from typing import Any

import requests


API_URL = "https://external.example.com/api/orders"
API_KEY = os.environ["EXTERNAL_API_KEY"]

REQUEST_TIMEOUT_SECONDS = 30
PAGE_LIMIT = 1000
MAX_PAGES = 1000
MAX_RETRIES = 3
RATE_LIMIT_STATUS_CODE = 429
RETRYABLE_SERVER_ERROR_STATUS_CODES = {500, 502, 503, 504}


class ExternalApiError(Exception):
    pass


class ExternalApiRateLimitError(ExternalApiError):
    pass


def get_retry_delay(response: requests.Response, attempt: int) -> int:
    retry_after = response.headers.get("Retry-After")
    if retry_after and retry_after.isdigit():
        return int(retry_after)
    return 2**attempt


def request_orders_page(
    session: requests.Session,
    start_date: str,
    end_date: str,
    page: int,
) -> dict[str, Any]:
    params = {
        "start_date": start_date,
        "end_date": end_date,
        "page": page,
        "limit": PAGE_LIMIT,
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json",
    }

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = session.get(
                API_URL,
                params=params,
                headers=headers,
                timeout=REQUEST_TIMEOUT_SECONDS,
            )
        except requests.Timeout as exc:
            if attempt == MAX_RETRIES:
                raise ExternalApiError(f"API request timed out on page {page}") from exc
            time.sleep(2**attempt)
            continue

        if response.status_code == RATE_LIMIT_STATUS_CODE:
            if attempt == MAX_RETRIES:
                raise ExternalApiRateLimitError(
                    f"API rate limit exceeded after retries: status={response.status_code}, page={page}"
                )
            time.sleep(get_retry_delay(response, attempt))
            continue

        if response.status_code in RETRYABLE_SERVER_ERROR_STATUS_CODES:
            if attempt == MAX_RETRIES:
                raise ExternalApiError(
                    f"API server error after retries: status={response.status_code}, page={page}"
                )
            time.sleep(get_retry_delay(response, attempt))
            continue

        if response.status_code != 200:
            raise ExternalApiError(
                f"API request failed: status={response.status_code}, page={page}"
            )

        try:
            return response.json()
        except ValueError as exc:
            raise ExternalApiError(f"Invalid JSON response on page {page}") from exc

    raise ExternalApiError(f"API request failed unexpectedly on page {page}")


def fetch_orders(start_date: str, end_date: str) -> list[dict[str, Any]]:
    all_orders: list[dict[str, Any]] = []
    page = 1

    with requests.Session() as session:
        while page <= MAX_PAGES:
            data = request_orders_page(session, start_date, end_date, page)

            orders = data.get("orders")
            if not isinstance(orders, list):
                raise ExternalApiError(f"Missing or invalid orders field on page {page}")

            all_orders.extend(orders)

            has_more = data.get("has_more")
            next_page = data.get("next_page")

            if has_more is False:
                return all_orders

            if isinstance(next_page, int) and next_page > page:
                page = next_page
                continue

            if len(orders) < PAGE_LIMIT:
                return all_orders

            page += 1

    raise ExternalApiError(f"Exceeded max pages: {MAX_PAGES}")


if __name__ == "__main__":
    result = fetch_orders("2026-06-01", "2026-06-26")
    print(f"Fetched orders: {len(result)}")
