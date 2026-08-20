"""Shared direct fxTwitter API v2 helpers for the command scripts."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote, urlencode, urlparse
from urllib.request import Request, urlopen


API_ROOT = "https://api.fxtwitter.com/2"
USER_AGENT = "fxtwitter-plugin-dev/0.0.1-dev (read-only)"
X_HOSTS = {"x.com", "twitter.com", "mobile.twitter.com", "www.x.com", "www.twitter.com"}


def api_get(path: str, params: dict[str, str] | None = None) -> dict[str, Any]:
    query = urlencode(params or {})
    url = f"{API_ROOT}/{path.lstrip('/')}" + (f"?{query}" if query else "")
    request = Request(url, headers={"Accept": "application/json", "User-Agent": USER_AGENT})
    with urlopen(request, timeout=20) as response:
        payload = json.load(response)
    if not isinstance(payload, dict):
        raise TypeError("fxTwitter returned a non-object JSON response.")
    return payload


def post_id(url: str) -> str:
    parsed = urlparse(url)
    parts = [part for part in parsed.path.split("/") if part]
    if parsed.netloc.lower() not in X_HOSTS or len(parts) < 3 or parts[1] != "status" or not parts[2].isdigit():
        raise ValueError("Expected an X post URL: https://x.com/handle/status/id")
    return parts[2]


def handle(value: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme:
        if parsed.netloc.lower() not in X_HOSTS:
            raise ValueError("Expected an X handle or profile URL")
        value = next((part for part in parsed.path.split("/") if part), "")
    result = value.strip().lstrip("@")
    if not result or any(char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_" for char in result):
        raise ValueError("An X handle may contain only letters, numbers, and underscores")
    return result


def encoded_handle(value: str) -> str:
    return quote(handle(value))


def print_json(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
