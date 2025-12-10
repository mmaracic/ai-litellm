from litellm import completion


class LLMClient:
    """Client to interact with a lite-llm model."""

    def __init__(self, api_key: str) -> None:
        """Initialize the LLM client with the given API key."""
        self.api_key = api_key

    def generate(self, model: str, query: str) -> str:
        """Generate a response from the model using the provided query.

        Returns the generated string.
        """
        response = completion(
            stream=False,
            model=model,
            api_key=self.api_key,
            messages=[{"content": query, "role": "user"}],
        )
        return response.choices[0].message["content"]
