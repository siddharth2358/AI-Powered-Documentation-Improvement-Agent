# MoEngage AI Documentation Agent

## Overview

This project contains an AI-powered agent system that analyzes public MoEngage documentation pages and provides structured, actionable suggestions for improving readability, structure, completeness, and style.

## Features

- Fetches and parses article HTML from given MoEngage docs URLs
- Uses LLMs (via OpenAI API) to assess content based on:
  - Readability for marketers
  - Structure and flow
  - Completeness and clarity
  - Adherence to simplified style guide
- Generates structured markdown reports
- Optional: Revises the original article content based on improvement suggestions

## Setup

1. Clone the repository
2. Create a virtual environment and install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key as an environment variable:
```bash
export OPENAI_API_KEY=your_key_here
```

## Running the Analyzer

```bash
python main.py https://help.moengage.com/hc/en-us/articles/123456789
```

## Project Structure

- `agents/analyzer_agent.py`: LLM-based analyzer logic
- `agents/revision_agent.py`: (Optional) revision generator logic
- `utils/`: Utility modules for fetching, readability scoring, and style evaluation
- `examples/`: Example markdown output for two MoEngage articles

## Assumptions

- OpenAI GPT-4 is available via API
- Only content under MoEngage documentation domain is used

