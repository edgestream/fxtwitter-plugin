#!/usr/bin/env python3
"""Read one public X post. Usage: read_post.py URL [--context]"""

import sys

from common import api_get, post_id, print_json


arguments = sys.argv[1:]
context = "--context" in arguments
arguments = [argument for argument in arguments if argument != "--context"]
if len(arguments) != 1:
    raise SystemExit("Usage: read_post.py URL [--context]")

status_id = post_id(arguments[0])
print_json(api_get(f"thread/{status_id}" if context else f"status/{status_id}"))
