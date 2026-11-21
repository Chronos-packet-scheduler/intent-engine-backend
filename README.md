# intent-engine-backend

Chronos Intent Engine: translates operator intents into validated DSL rules (Python, uv).

```sh
uv sync
uv run uvicorn intent_engine.main:app --reload   # serves /healthz on :8000
uv run pytest
uv run ruff check
```

Images are published to `ghcr.io/chronos-packet-scheduler/intent-engine-backend` on every push to `main` and on `v*` tags.
