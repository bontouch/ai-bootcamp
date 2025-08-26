# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
AI Bootcamp for Framna colleagues - a 4-week hands-on program designed to train digital product agency engineers in generative AI techniques. The bootcamp emphasizes practical, workshop-based learning with progressive complexity.

## Architecture & Structure

### Workshop Material Organization
The codebase follows a strict hierarchical structure:
```
material/
-- week_1/
----tuesday/        # Prompting Patterns & Structured Outputs
----wednesday/      # Orchestration & MCP/Tools  
----thursday/       # Retrieval & Context Systems (RAG)
----friday/         # Multimodality & Mini Showcase
--week_2/             # Backend, Docker, Cloud Deploy
--week_3/             # Evaluation, Tracing, Fine-Tuning
--week_4/             # Capstone Projects
```

Each session contains:
- `starter_code/` - Template files with TODO comments for students
- `solution/` - Complete implementations demonstrating best practices
- External data files (.txt, .json) used by both starter and solution code
- README.md with session objectives and instructions

### Key Patterns

**Dual Implementation Approach**: Every exercise provides both starter templates and complete solutions, enabling students to attempt implementation before seeing the answer.

**External Data Strategy**: Sample data lives in separate files rather than hardcoded strings, teaching real-world file I/O patterns and enabling easy data updates.

**Progressive Validation**: Solutions include Pydantic validators that catch common AI output errors, teaching defensive programming with AI systems.

## Development Environment

### Package Management
Uses `uv` for modern Python dependency management:
```bash
uv add package_name        # Install new dependency
uv run script.py          # Run with proper virtual environment
uv sync                   # Sync dependencies with lockfile
```

### Key Dependencies
- `openai>=1.100.1` - OpenAI API integration
- `pydantic>=2.11.7` - Data validation and structured outputs  
- `openai-agents>=0.2.8` - Agent orchestration patterns
- `chromadb>=1.0.20` - Vector database for RAG exercises

## AI Integration Standards

### OpenAI API Usage
**Always use "gpt-5" as the standard model** (not "gpt-4" or older versions).

**For structured outputs**, use `client.responses.parse()` with Pydantic BaseModel classes:
```python
response = client.responses.parse(
    model="gpt-5",
    input=[{"role": "user", "content": prompt}],
    text_format=YourPydanticModel,
)
result = response.output_parsed
```

**Avoid deprecated patterns** like `response_format={"type": "json_object"}`.

### Code Quality Standards
- Include type hints for all function parameters and return values
- Use Pydantic models for all structured data
- Implement proper error handling that teaches defensive programming
- Add validation that catches common AI calculation/logic errors
- Keep code clean and concise - avoid excessive comments or print statements

## Specialized Agents

The project includes two specialized Claude Code agents:

### bootcamp-workshop-planner
Creates comprehensive workshop plans with:
- Learning objectives tied to specific AI techniques
- Progressive exercise structures with time estimates
- Instructor notes and common pitfall guidance
- References to relevant OpenAI API documentation

**Usage**: Invoke when designing new workshop sessions or educational content.

### bootcamp-notebook-creator  
Generates Jupyter notebooks from workshop plans:
- Creates both starter and solution notebooks
- Implements external data file strategy
- Includes validation cells and progressive exercises
- Follows modern Python practices with proper error handling

**Usage**: Invoke after workshop planning to create the actual coding exercises.

## Content Creation Guidelines

### Workshop Design Principles
- Focus on single core concepts per session rather than multiple techniques
- Design exercises where the target technique is essential, not optional
- Include deliberately ambiguous test cases that demonstrate why techniques are needed
- Use business-relevant scenarios that engineers can relate to

### External Data Requirements
- Create realistic sample data in separate .txt, .json, or .csv files
- Include edge cases that reveal why the target technique is necessary
- Size data appropriately for workshop time constraints
- Make data files reusable across multiple exercises

### Validation Strategy
- Add Pydantic validators that catch common AI output errors
- Design tests that pass only when the target technique is properly applied
- Include examples that break with naive approaches
- Provide clear error messages that guide students toward correct solutions

## OpenAI API Documentation Reference

The project maintains comprehensive OpenAI API documentation in `.claude/docs/openai-api/`:
- `structured-output.md` - JSON schema enforcement patterns
- `function-calling.md` - Tool integration and external system access
- `text-generation.md` - Core prompting and generation techniques  
- `images-and-vision.md` - Multimodal capabilities
- `conversation-state.md` - Multi-turn conversation management
- `using-tools.md` - Extended capabilities with built-in tools and MCP

Reference these docs when creating workshop content to ensure alignment with current OpenAI API best practices.