
import os
import openai
from utils.readability import evaluate_readability
from utils.style_guide import evaluate_style
from utils.fetcher import extract_text_from_html

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_documentation(url, html_content):
    text = extract_text_from_html(html_content)
    readability = evaluate_readability(text)
    structure = analyze_with_gpt(text, "structure and flow")
    completeness = analyze_with_gpt(text, "completeness and examples")
    style = evaluate_style(text)

    report = f"""# Documentation Analysis Report
**URL:** {url}

## Readability
{readability}

## Structure and Flow
{structure}

## Completeness and Examples
{completeness}

## Style Guide Assessment
{style}
"""
    return report

def analyze_with_gpt(text, criterion):
    prompt = f"""You are a technical writing assistant. Evaluate the following documentation text for its {criterion}.
Provide specific, actionable feedback for improvement.

TEXT:
{text[:4000]}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    from utils.fetcher import fetch_article_content
    url = input("Enter MoEngage Documentation URL: ")
    html = fetch_article_content(url)
    print(analyze_documentation(url, html))
