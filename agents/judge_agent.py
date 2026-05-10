from providers.openrouter_provider import ask_model

def judge_answer(question, generated_answer, critic_response):

    response = ask_model(
        "deepseek/deepseek-chat",
        f"""
        You are an AI judge.

        Your job is to evaluate:

        1. Original Question
        2. Generated Answer
        3. Critic Response

        Then provide the BEST final answer.

        ORIGINAL QUESTION:
        {question}

        GENERATED ANSWER:
        {generated_answer}

        CRITIC RESPONSE:
        {critic_response}
        """
    )

    return response