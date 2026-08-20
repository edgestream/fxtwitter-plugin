#!/usr/bin/env python3
"""Read replies to a public X post."""

import sys

from common import api_get, post_id, print_json


arguments = sys.argv[1:]
if not arguments:
    raise SystemExit("Usage: read_conversation.py URL [--sort relevance|recent] [--cursor CURSOR]")
url = arguments.pop(0)
sort = "relevance"
cursor = None
while arguments:
    option = arguments.pop(0)
    if option == "--sort" and arguments:
        sort = arguments.pop(0)
    elif option == "--cursor" and arguments:
        cursor = arguments.pop(0)
    else:
        raise SystemExit("Usage: read_conversation.py URL [--sort relevance|recent] [--cursor CURSOR]")
if sort not in {"relevance", "recent"}:
    raise ValueError("--sort must be relevance or recent")

params = {"ranking_mode": "likes" if sort == "relevance" else "recency"}
if cursor:
    params["cursor"] = cursor
print_json(api_get(f"conversation/{post_id(url)}", params))
