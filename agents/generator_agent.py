from providers.openrouter_provider import ask_model
from config import GENERATOR_MODEL

SYSTEM_PROMPT = """
You are an expert AI assistant with broad knowledge.

Your job is to answer the user's question with:
- Accuracy: only state things you are confident about
- Clarity: explain in simple, direct language
- Completeness: cover the key points, don't leave gaps
- Structure: use paragraphs or bullet points where it helps

Do not pad your answer. Do not say "Great question!".
Just answer.
"""

def generate_answer(question):

    response = ask_model(
        GENERATOR_MODEL,
        user_prompt=question,
        system_prompt=SYSTEM_PROMPT
    )

    return response