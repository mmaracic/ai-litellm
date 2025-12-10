from litellm import completion, acompletion, Router


class LLMClient:
    """Client to interact with a lite-llm model."""

    def __init__(
        self,
        api_key: str,
        model: str,
    ) -> None:
        """Initialize the LLM client with the given API key."""

        model_list = [
            {
                "model_name": model,
                "litellm_params": {  # params for litellm completion/embedding call
                    "model": model,
                    "api_key": api_key,
                },
            }
        ]
        self.model = model
        self.api_key = api_key
        self.router = Router(model_list=model_list)

    def generate(self, query: str) -> str:
        """Generate a response from the model using the provided query.

        Returns the generated string.
        """
        # Both router and litellm also have async methods if needed and support streaming as additional functionality
        response = self.router.completion(
            stream=False,
            model=self.model,
            api_key=self.api_key,
            messages=[{"content": query, "role": "user"}],
        )
        return response.choices[0].message["content"]
