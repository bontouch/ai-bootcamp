# Orchestration Concepts

## Learning Goals
- Understand the difference between single calls and orchestration
- See how structured outputs become orchestration triggers
- Learn context management strategies across calls
- Understand error handling and fallback patterns

## Session Plan

### 9:00 - 9:45: What is Orchestration?

**The Core Problem**
Real AI applications need multiple steps:
- "Find me a cheap lunch nearby" requires: location → restaurants → prices → comparison
- Single LLM calls can't access external data or perform calculations
- Orchestration = chaining actions based on LLM decisions

**Single Call vs Orchestration**
```
Single Call:     User Input → LLM → Response (limited)
Orchestration:   User Input → LLM → Tool Call → LLM → Tool Call → Response (powerful)
```

### 9:45 - 10:30: Structured Outputs as Orchestration Triggers

**The Key Insight**: Structured outputs tell us what to do next

```python
# This structured response contains our next actions:
{
  "items": ["Big Mac", "medium fries", "Coke"],
  "action": "search_prices",  # ← This triggers the next step
  "restaurant": "McDonald's",
  "confidence": 0.95
}
```

**Demo**: Show actual structured output objects and explain each field's role

### 10:30 - 11:15: Context Management & Error Handling

### 11:15 - 12:00: Interactive Demo - Meal Price Calculator

**Live Coding Session**: Build conceptual examples showing:

1. **Structured Analysis**: Parse "McDonald's Big Mac meal" → items + actions
2. **Tool Triggers**: How `"action": "search_prices"` leads to database lookup
3. **Fallback Pattern**: When database fails → trigger web search
4. **Context Accumulation**: Carry prices through to final calculation

**Focus**: Understanding concepts, not building complete system

## Key Takeaways
- Orchestration = LLM decisions triggering subsequent actions
- Structured outputs are the "control flow" of AI systems  
- Context management is harder than it looks
