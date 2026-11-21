# intent-engine-backend

Chronos Intent Engine: translates operator intents into validated DSL rules (Python, uv).

```sh
uv sync
uv run python -m intent_engine.main   # run the app
uv run pytest                         # tests
uv run ruff check                     # lint
uv run ruff format                    # format
```

Images are published to `ghcr.io/chronos-packet-scheduler/intent-engine-backend` on every push to `main` and on `v*` tags.
