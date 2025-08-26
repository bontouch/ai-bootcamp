# Prompting Patterns & Structured Outputs

## Learning Goals
- Master few-shot and chain-of-thought prompting
- Use structured outputs with Pydantic models
- Implement safety guardrails

## Session Plan

### 9:00 - 10:30: Core Concepts

**Few-Shot Prompting**
- Provide examples to guide model behavior
- Use for complex tasks requiring specific formats
- Best practice: Clear, diverse examples

**Chain-of-Thought**
- Step-by-step reasoning for complex problems
- When to use: Multi-step analysis, calculations
- When NOT to use: Simple tasks, creative writing

**Structured Outputs**
- Define Pydantic schemas for consistent data
- Use `client.beta.chat.completions.parse()` 
- Handle validation errors gracefully

### 10:45 - 12:00: Demo
Build a customer feedback analyzer using all patterns.

## Materials
- OpenAI API key (gpt-4.1)
- Python: `openai`, `pydantic`