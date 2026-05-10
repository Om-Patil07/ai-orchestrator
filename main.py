from agents.generator_agent import generate_answer
from agents.critic_agent import critique_answer
from agents.judge_agent import judge_answer

question = input("Ask something: ")

# Generator Agent
generated_answer = generate_answer(question)

print("\n=== GENERATOR ANSWER ===\n")
print(generated_answer)

# Critic Agent
critic_response = critique_answer(
    question,
    generated_answer
)

print("\n=== CRITIC RESPONSE ===\n")
print(critic_response)

# Judge Agent
final_response = judge_answer(
    question,
    generated_answer,
    critic_response
)

print("\n=== FINAL JUDGED ANSWER ===\n")
print(final_response)