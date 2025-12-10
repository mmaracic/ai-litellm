import os

from dotenv import load_dotenv
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException

from app.schemas import QueryRequest, QueryResponse
from app.llm_client import LLMClient


@asynccontextmanager
async def lifespan(app: FastAPI):
    """FastAPI lifespan: initialize LLM on startup and clean up on shutdown."""
    try:
        load_dotenv()
        llm_client: LLMClient = LLMClient(os.getenv("OPENROUTER_API_KEY", ""))
        app.state.llm_client = llm_client
        yield
    finally:
        pass


app: FastAPI = FastAPI(lifespan=lifespan)


@app.post("/query-llm", response_model=QueryResponse)
async def query_llm(request: QueryRequest) -> QueryResponse:
    """Endpoint to query the LLM.

    The prompt is hardcoded and combined with the user's query.
    """
    try:
        llm_client: LLMClient = app.state.llm_client
        response_text: str = llm_client.generate(
            "openrouter/openai/gpt-5-nano", request.query
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return QueryResponse(response=response_text)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
