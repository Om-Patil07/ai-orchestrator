from providers.openrouter_provider import ask_model

def critique_answer(question, answer):

    response = ask_model(
        "deepseek/deepseek-chat",
        f"""
        You are an AI critic.

        Review the following answer.

        Question:
        {question}

        Answer:
        {answer}

        Improve the answer if needed.
        """
    )

    return response