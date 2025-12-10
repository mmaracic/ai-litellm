from fastapi.testclient import TestClient

from app.main import app

# When testing lifecycle events, use TestClient as a context manager (using 'with' statement, not defined outside the test)
# https://fastapi.tiangolo.com/advanced/testing-events/
# https://fastapi.tiangolo.com/tutorial/testing/#extended-testing-file


def test_read_main():
    with TestClient(app) as client:
        response = client.post(
            url="/query-llm",
            json={"query": "What is the capital of France?"},
        )
        assert response.status_code == 200
        assert "paris" in str(response.json()).lower()
