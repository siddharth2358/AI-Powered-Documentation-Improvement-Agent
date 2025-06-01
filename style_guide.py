import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def evaluate_style(text):
    prompt = f"""You are an expert in writing documentation. Evaluate the following content for:
- Voice and Tone (customer-focused, clear)
- Clarity and Conciseness
- Action-oriented Language

Suggest specific changes to improve these aspects.

TEXT:
{text[:3000]}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    test_text = input("Paste documentation text to evaluate style:\n")
    print(evaluate_style(test_text))
