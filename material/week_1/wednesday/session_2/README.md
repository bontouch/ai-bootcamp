# Meal Price Calculator Agent Lab

## Learning Objectives

- Build multi-agent systems using OpenAI Agents SDK
- Orchestrate tools: WebSearch, calculator functions, and agent-as-tool patterns  
- Understand agent coordination and error handling
- Apply orchestration concepts to real-world scenarios

## The Challenge

Create a **Meal Price Calculator Agent** that processes complex food orders and returns total cost with budget context.

**Example Input:** "Big Mac + medium fries + Coke"  
**Expected Output:** "That's about 90 SEK total, roughly a mid-range fast food meal."

## Agent Architecture

### Main Price Calculator Agent
**Tools available:**
- **WebSearchTool** (built-in): Search for pricing data online
- **Calculator function** (custom): Sum prices and calculate budget categories  
- **Food Parser Agent** (agent-as-tool): Break complex orders into items

### Food Parser Agent
**Purpose:** Convert complex food orders into searchable items
- Input: "Big Mac meal" 
- Output: ["Big Mac", "McDonald's medium fries", "medium Coca-Cola"]

## Task Overview

Build a system that:

1. **Parses complex food orders** using a specialist agent
2. **Searches for pricing data** using web search for each item
3. **Calculates totals** using custom calculator functions
4. **Provides budget context** about meal cost categories

## Key Technical Requirements

### 1. Agent Coordination
- Main agent coordinates multiple tools and sub-agents
- Food parser agent used as tool for complex order breakdown
- Error handling when searches fail or items aren't found

### 2. Tool Functions
```python
from agents import function_tool
from pydantic import BaseModel

class MealPriceResult(BaseModel):
    total_price: float
    budget_category: str
    budget_advice: str

@function_tool
def calculate_meal_price(price_list: List[float]) -> MealPriceResult:
    """Calculate total price and budget category"""
    # Return structured result

@function_tool
def categorize_meal_budget(price: float) -> str:
    """Categorize meal cost: budget, moderate, expensive"""
```

### 3. Agent Integration
```python
from agents import Agent, WebSearchTool, Runner

# Food parser as agent tool
parser_agent = Agent(name="food_parser", instructions="...")
main_agent = Agent(
    tools=[
        parser_agent.as_tool(),
        WebSearchTool(), 
        calculate_meal_price
    ]
)

# Run the agent
result = Runner.run_sync(main_agent, "Calculate price for Big Mac meal")
print(result.final_output)
```

## Expected Workflow

1. **User Input:** "Thai green curry with jasmine rice"
2. **Parser Agent:** → ["Thai green curry", "jasmine rice portion"]  
3. **Web Search:** Search pricing data for each item
4. **Calculator:** Sum prices and determine budget category
5. **Budget Context:** Generate advice about meal cost

**Sample Output:**
```
🥘 Thai green curry with jasmine rice
Total: 145 SEK

Breakdown:
• Thai green curry: 95 SEK
• Jasmine rice portion: 50 SEK  

📊 That's a moderate-priced restaurant meal.
💡 Good value for a full meal - typical for Thai restaurants in Sweden.
```

## Files Provided

- `meal_queries.txt` - Test meal combinations to process
- `starter_code/price_agent.py` - Main agent template with TODOs
- `starter_code/parser_agent.py` - Food parser agent template  
- `starter_code/tools.py` - Calculator functions template
- `starter_code/main.py` - CLI interface template

## Getting Started

```bash
uv add openai-agents pydantic
export OPENAI_API_KEY="your-key"
python main.py
```

## Implementation Strategy

### Phase 1: Build Tools (30 min)
- Implement price calculator functions
- Test with sample data

### Phase 2: Food Parser Agent (45 min)  
- Create agent that breaks down complex orders
- Test with various meal types

### Phase 3: Main Agent (60 min)
- Integrate WebSearch, calculator, and parser agent
- Handle tool coordination and errors

### Phase 4: Refinement (45 min)
- Test with provided meal queries
- Improve error handling and user experience

## Success Criteria

✅ **Agent Coordination** - Parser agent works as tool for main agent  
✅ **Web Search Integration** - Finds real pricing data online  
✅ **Calculator Tools** - Accurate price totals and budget categories  
✅ **Error Handling** - Graceful failures when items not found  
✅ **Budget Context** - Meaningful advice about meal cost  

## Challenge Extensions

- **Multiple portion sizes** - Handle "large", "small" modifiers  
- **Restaurant chains** - Specify "McDonald's Big Mac" vs generic
- **Currency conversion** - Support different currencies
- **Location-based pricing** - Consider regional price differences
