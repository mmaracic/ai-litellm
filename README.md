# README

Simple FastAPI app exposing POST `/query-llm` that forwards queries to a lite-llm
model.

## Enviroment Variables
- `OPENROUTER_API_KEY`: API key for OpenRouter service.

## Functionality

LiteLLM and router both have synchronous and asynchronous APIs (completion vs acompletion).

## Run

```bash
uv run python -m app.main
```

