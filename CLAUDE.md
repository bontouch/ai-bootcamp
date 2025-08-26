
# Description
We're creating an AI Bootcamp for our colleagues at Framna. A digital product agency. The goal is to get our colleagues up to speed with how we're working with AI (notable generative AI) so that they can be confident in joining a client project on their own.

The idea is to run this over 3-4 weeks, doing a lot of hands-on work to maximize learning. We will do the teaching in workshop sessions where we touch upon specific subjects and combine presentational content with actually experimenting writing code for concise tasks.

# Workshop Structure
## Session 1: 9 – 12

Review of some concept together, plus a possible recap of yesterday with questions.

Smaller labs done together with us. We want them to write code.

We might have prepared two exercises that we expect them to complete.

## Session 2: 13 – 16:00

A more extensive lab done individually without our involvement.

Should have a clearly defined deliverable.

Should be possible to complete within three hours.

We can make use of external APIs, our own available data, or other resources.

## Demo: 16 – 16:30

Joint review of the solution.

# Directory Structure
- material
-- week_1
--- session_1
--- session_2
--- demo
-- week_2
---...
-- week_3
---...
-- week_4
---...
- some_dir_name (add other supporting/shared content here if it makes sense)

# Rules, API Providers, Ecosystem, Patterns
Since it's so much content out there we want to limit ourselves for you (Claude, the content creator) to bound yourself to certain providers of AI API's and so on so that you can know better what to create your content on.

- We're mainly using OpenAI as our API provider of LLM's. Look mainly to their API reference when calling (https://platform.openai.com/docs/api-reference/introduction).
- We're using FastAPI when building API's.
- We're always writing code following latest standards and that's high quality. Think modularly and separate concerns of functionality in order to achieve maintainability.
- When it comes to agents and prompt chaining, we can learn much OpenAI agents SDK, Google's agent developer kit, and Pydantic AI. LangChain can be useful for particular featuresm but in general it's not a good practice.

## Content Creation Guidelines

**OpenAI API Usage:**
- Always use "gpt-4.1" as the standard model (not "gpt-4")
- For structured outputs, use `client.responses.parse()` with Pydantic BaseModel classes passed directly to the `text_format` parameter. Use `response.output_parsed`to get the parsed response.
- Don't use the old `response_format={"type": "json_object"}` pattern

**Code Style & Verbosity:**
- Keep code clean and concise - avoid excessive comments, print statements, and emojis
- Code should be readable but not over-documented for workshop use
- Focus on core concepts rather than comprehensive edge case handling
- Let instructors fill in gaps during workshops rather than trying to cover everything in code

**Documentation Style:**
- Keep READMEs concise and scannable - aim for 70% less content than typical documentation
- Focus on actionable steps rather than verbose explanations
- Remove redundant sections and excessive examples
- Students should be able to quickly understand what to do

**Package Management:**
- Use `uv` instead of `pip` for all dependency installation (`uv add` instead of `pip install`)
- Use `pyproject.toml` instead of `requirements.txt` for modern Python project structure

**Workshop Scope:**
- Reduce complexity to focus on learning core concepts
- Make scope smaller and more focused rather than comprehensive
- Prioritize hands-on learning over theoretical completeness

**Session Design Strategy:**
- Design sessions around specific AI techniques that students must master (e.g., few-shot prompting, structured outputs)
- Create scenarios where the target technique is essential, not optional
- Use deliberately ambiguous test cases that demonstrate why the technique is needed
- Focus sessions on single core concepts rather than trying to cover multiple techniques

**Starter Code Templates:**
- Provide class/method structure with TODO comments, not empty files or complete implementations
- Include method signatures and clear guidance comments on what each part should accomplish
- Use external sample data files (*.txt, *.json) rather than hardcoded strings in code
- Template files should give structural hints while leaving implementation as the learning exercise

**File Organization Standards:**
```
session_name/
├── sample_data.txt           # External test data used by both starter and solution  
├── starter_code/             # Templates with structural guidance
├── solution/                # Complete working implementation that loads external data
└── README.md                # Task description with expected outputs
```

**External Data Strategy:**
- Move all sample data to external files (.txt, .json, .csv) separate from code
- Both starter templates and complete solutions should load the same external data
- This teaches real-world file I/O patterns and makes data updates easier
- Allows instructors to modify test cases without touching code files

**Learning-Focused Validation:**
- Add Pydantic validators that catch common AI calculation errors (math, logic inconsistencies)
- Design validation rules that teach defensive programming when working with AI outputs
- Include realistic error scenarios that become learning opportunities
- Use structured outputs with meaningful field validation and business logic checks

**Task-Focused README Structure:**
- Start with clear learning objectives tied to specific AI techniques
- Include "Expected Output" sections showing realistic formatted results
- Highlight the core challenge that requires the target technique to solve
- Provide concrete examples of ambiguous cases that demonstrate technique necessity
- Keep implementation guidance focused on the core learning goal, not comprehensive coverage

# Content Plan
## Week 1 — AI & LLMs (no backend/cloud)

**Learning goals**

- Master prompting patterns, structured outputs, tool use, and orchestration.
- Build retrieval-augmented pipelines (RAG variants) and lightweight agents.
- Set up an eval-first mindset (without worrying about infra yet).

**Daily rhythm (recommended):**

09:00–10:30 lecture · 10:45–12:00 guided demo · 13:00–16:00 lab · 16:00–16:30 share-out

### Monday — Landscape & Foundations

- **AI Landscape** (providers, OSS, practical implications)
- **Eval-Driven System Design** (problem → V0 → data & evals → iterate)
- **Prompting 101**: prompt vs input vs context; prompt components
- **Lab:** Write prompts that separate instructions / input / context; test few-shot vs zero-shot

### Tuesday — Prompting Patterns & Structured Outputs

- Few-shot, Chain-of-Thought (when/when not), safety & guardrails in prompts
- **Structured outputs** (JSON schemas), function/tool call schemas, schema validation
- **Lab:** Build a mini “data extraction” pipeline using structured outputs

### Wednesday — Orchestration & MCP/Tools

- **Prompt chaining → orchestration**: task decomposition, retries, fallbacks
- **MCP, tool calls, agents**: capabilities, limits, handoffs
- **Lab:** Tool-using assistant (search/math/file-read mock tools) with deterministic schemas

### Thursday — Retrieval & Context Systems (RAG)

- Retrieval patterns: naive RAG, multi-step retrieval, reranking, hybrid search, metadata filters
- Context packaging strategies: chunking, citations, anti-hallucination patterns
- **Lab:** Build a local RAG prototype (in-memory or simple store) with eval hooks

### Friday — Multimodality & Mini Showcase

- **Modalities**: text ↔ image/audio basics; prompting multimodal models; structured outputs with vision
- **Lightweight evals**: golden sets, asserts, regression checks (no infra yet)
- **Lab:** Add a small multimodal task (e.g., receipt or chart caption → JSON)
- **Showcase:** 5–7 min demos of each team’s W1 prototype (no deployment)

**Week 1 deliverables**

- A repo with: prompts, orchestration graph, tool schemas, a RAG notebook, and a tiny eval set + script.
- A short README explaining decisions and what to measure next week.

---

## Week 2 — Backend, Docker, Cloud Deploy

**Learning goals**

- Wrap the Week-1 AI pipeline behind an API.
- Containerize, deploy, and operate it in the cloud with basic observability.
- Practice secure configs, secrets, and cost-aware choices.

**Daily rhythm (recommended):**

09:00–10:00 recap · 10:00–12:00 demo/deep dive · 13:00–16:30 hands-on deployment sprints

### Monday — FastAPI Service Design

- FastAPI patterns: routers, **Depends**, **Lifespan**, typing & Pydantic models
- Service layering: API ↔ service ↔ repositories (vector DB / cache as interfaces)
- **Lab:** Turn W1 pipeline into a clean FastAPI service with typed request/response models

### Tuesday — Dockerize & Run Locally

- Dockerfiles for Python apps (multi-stage builds, slim images, caching)
- Local prod-ish run: uvicorn/gunicorn, env vars, health checks, graceful shutdowns
- **Lab:** Containerize the service; run locally; add a `/healthz` and `/metrics` endpoint

### Wednesday — Deploy to Cloud

- Choose one target (e.g., managed container platform).
- Networking basics: ingress, TLS, domains; secrets management; runtime configs
- **Lab:** Deploy v1; verify with curl/postman; rotate a secret; set resource limits

### Thursday — Data & Observability

- Managed data options (vector DB, object storage, Postgres) + connection patterns
- Tracing & logs for AI apps: request IDs, spans across LLM/tool calls, latency/error budgets
- **Lab:** Add tracing & structured logs; wire a managed vector DB; seed minimal data

### Friday — CI/CD & SRE Basics

- CI: tests, type-checking, lint, small eval suite on PR
- CD: build → scan → push → deploy; blue/green or canary basics; rollback
- **Lab:** GitHub Actions (or equivalent) pipeline that builds the image, runs tests/evals, deploys on main
- **Milestone demo:** Cloud endpoint live, with tracing & a README “operational runbook”

**Week 2 deliverables**

- Public (or org-internal) API endpoint with:
    - OpenAPI docs, auth strategy noted, health/metrics endpoints
    - Deployed vector store / persistence (or mocked if not needed)
    - CI pipeline + one-click rollback documented

---

## Week 3 — Evaluation, Tracing, Fine-Tuning (unchanged focus)

- Recap; deepen **evaluation** (business metrics ↔ model metrics), **tracing** for debugging pipelines, and **fine-tuning** (when/why/how).
- Add **advanced multi-agent** patterns & richer **modalities** as stretch goals.

---

## Week 4 — Capstone (unchanged structure)

- Mon–Thu build; **Fri 19th** presentations.
- Aim for correctness, evals, and clean design over raw performance.