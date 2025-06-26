from openai import OpenAI

def query_openai(prompt: str, api_key: str, model: str = "gpt-3.5-turbo") -> str:
    """
    Sends a prompt to the OpenAI API using ChatCompletion and returns the response.
    """
    try:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"