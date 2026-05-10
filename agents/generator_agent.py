from providers.openrouter_provider import ask_model

def generate_answer(question):

    response = ask_model(
        "deepseek/deepseek-chat",
        f"""
        You are a helpful AI assistant.

        Answer this question clearly:

        {question}
        """
    )

    return response