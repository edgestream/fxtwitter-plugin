# fxTwitter Dev Plugin

A Codex plugin for direct, read-only access to public X content through
fxTwitter API v2. It contains no MCP server and requires no credentials.
This development version is published as `fxtwitter-plugin-dev`.

## Usage

```bash
python3 skills/fxtwitter/scripts/read_post.py 'https://x.com/OpenAI/status/2082577277246972300' --context
python3 skills/fxtwitter/scripts/read_conversation.py 'https://x.com/OpenAI/status/2082577277246972300' --sort recent
python3 skills/fxtwitter/scripts/read_profile.py OpenAI
python3 skills/fxtwitter/scripts/read_author_feed.py OpenAI --limit 10
```

See the full usage instructions in [`skills/fxtwitter/SKILL.md`](skills/fxtwitter/SKILL.md).

## API documentation

See the official [FxTwitter API documentation](https://docs.fxembed.com/api/introduction/)
and its [OpenAPI v2 specification](https://api.fxtwitter.com/2/openapi.json).
