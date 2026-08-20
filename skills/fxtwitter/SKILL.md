---
name: fxtwitter
description: Read public X posts, conversations, profiles, and author feeds directly from fxTwitter API v2. Use this skill for x.com, twitter.com, or mobile.twitter.com URLs and requests for public X content.
---

# fxTwitter

Use this plugin's local Python script exclusively for public X content.

## Commands

Run the request directly and use the JSON output as the source:

```bash
python3 scripts/read_post.py 'https://x.com/OpenAI/status/2082577277246972300' --context
python3 scripts/read_conversation.py 'https://x.com/OpenAI/status/2082577277246972300' --sort recent
python3 scripts/read_profile.py OpenAI
python3 scripts/read_author_feed.py OpenAI --limit 10
```

- `read_post.py` accepts an X post URL. `--context` uses the thread endpoint.
- `read_conversation.py` accepts an X post URL. `--sort relevance` (default) sorts by
  likes; `--sort recent` sorts by recency. Pass the returned opaque cursor back
  unchanged with `--cursor` when another page is needed.
- `read_profile.py` and `read_author_feed.py` accept `@handle`, a handle, or an X profile URL.
- `--include-replies` includes replies in a feed. By default, replies and
  reposts are excluded. `--since YYYY-MM-DD` limits feed results by date.

Do not silently switch to browsers, mirrors, or other sources when the API fails.
