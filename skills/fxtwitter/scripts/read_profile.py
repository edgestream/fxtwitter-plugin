#!/usr/bin/env python3
"""Read one public X profile. Usage: read_profile.py HANDLE_OR_URL"""

import sys

from common import api_get, encoded_handle, print_json


if len(sys.argv) != 2:
    raise SystemExit("Usage: read_profile.py HANDLE_OR_URL")

print_json(api_get(f"profile/{encoded_handle(sys.argv[1])}"))
