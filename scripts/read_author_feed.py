#!/usr/bin/env python3
"""Read a public X author feed."""

import sys
from datetime import datetime, timezone

from common import api_get, encoded_handle, handle, print_json


arguments = sys.argv[1:]
if not arguments:
    raise SystemExit("Usage: read_author_feed.py HANDLE_OR_URL [--limit 1-100] [--cursor CURSOR] [--since YYYY-MM-DD] [--include-replies]")
profile = arguments.pop(0)
limit = 25
cursor = None
since = None
include_replies = False
while arguments:
    option = arguments.pop(0)
    if option == "--include-replies":
        include_replies = True
    elif option == "--limit" and arguments:
        limit = int(arguments.pop(0))
    elif option == "--cursor" and arguments:
        cursor = arguments.pop(0)
    elif option == "--since" and arguments:
        since = arguments.pop(0)
    else:
        raise SystemExit("Usage: read_author_feed.py HANDLE_OR_URL [--limit 1-100] [--cursor CURSOR] [--since YYYY-MM-DD] [--include-replies]")
if not 1 <= limit <= 100:
    raise ValueError("--limit must be between 1 and 100")

profile_handle = handle(profile)
params = {"count": str(limit)}
if cursor:
    params["cursor"] = cursor
if include_replies:
    params["with_replies"] = "1"
payload = api_get(f"profile/{encoded_handle(profile)}/statuses", params)
since_timestamp = datetime.strptime(since, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp() if since else None
results = []
for entry in payload.get("results", []):
    statuses = entry.get("statuses", []) if isinstance(entry, dict) and entry.get("type") == "thread" else [entry]
    for status in statuses:
        if not isinstance(status, dict):
            continue
        author = status.get("author")
        author_handle = author.get("screen_name") if isinstance(author, dict) else None
        timestamp = status.get("created_timestamp")
        if author_handle and str(author_handle).casefold() != profile_handle.casefold():
            continue
        if status.get("reposted_by") is not None or (not include_replies and status.get("replying_to")):
            continue
        if since_timestamp is not None and isinstance(timestamp, (int, float)) and timestamp < since_timestamp:
            continue
        results.append(status)
        if len(results) == limit:
            break
    if len(results) == limit:
        break
payload["results"] = results
print_json(payload)
