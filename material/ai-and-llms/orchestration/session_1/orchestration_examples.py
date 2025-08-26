"""
Orchestration Concepts - Week 1 Wednesday Session 1

Demonstrates key orchestration concepts through meal price calculation examples.
Focus: Understanding concepts, not building complete systems.
"""

import json
from openai import OpenAI
from pydantic import BaseModel
from typing import List, Optional

client = OpenAI()


# ============================================================================
# CONCEPT 1: Structured Outputs as Orchestration Triggers
# ============================================================================


class MealAnalysis(BaseModel):
    """Structured output that contains orchestration instructions"""

    items: List[str]
    action: str  # This field determines what happens next!
    restaurant: Optional[str] = None
    confidence: float


def analyze_meal_order(order: str) -> MealAnalysis:
    """
    CONCEPT: The LLM returns structured data that tells us what to do next
    """
    response = client.responses.parse(
        model="gpt-4.1",
        messages=[
            {
                "role": "user",
                "content": f"""Analyze this meal order: "{order}"
            
            Break it into individual items and decide the next action.
            Set action to:
            - 'search_database' if it's a common restaurant meal
            - 'search_web' if it's an unusual or specific item
            - 'estimate' if it's too vague to search
            
            Be specific about restaurant chains when mentioned.""",
            }
        ],
        response_format=MealAnalysis,
    )
    return response.output_parsed


# Demo: Show how structured output determines next steps
def demo_structured_triggers():
    """Demonstrate how structured outputs trigger different actions"""

    print("=== CONCEPT 1: Structured Outputs as Triggers ===\n")

    test_orders = [
        "Big Mac meal from McDonald's",
        "homemade chicken sandwich",
        "some lunch food",
    ]

    for order in test_orders:
        print(f"📝 Order: '{order}'")
        analysis = analyze_meal_order(order)

        print(f"🔍 Structured Output:")
        print(f"   Items: {analysis.items}")
        print(f"   Action: {analysis.action} ← This determines what happens next!")
        print(f"   Restaurant: {analysis.restaurant}")
        print(f"   Confidence: {analysis.confidence}")

        # Show what the action triggers
        if analysis.action == "search_database":
            print("   ✅ Would trigger: Database lookup for restaurant prices")
        elif analysis.action == "search_web":
            print("   ✅ Would trigger: Web search for price information")
        elif analysis.action == "estimate":
            print("   ✅ Would trigger: Price estimation based on similar items")

        print("-" * 50)


# ============================================================================
# CONCEPT 2: Context Management Across Calls
# ============================================================================


class PriceContext(BaseModel):
    """Context that accumulates through the orchestration chain"""

    original_order: str
    items: List[str]
    prices_found: List[dict] = []
    total_price: Optional[float] = None
    search_method: str = ""


def mock_database_lookup(item: str) -> Optional[dict]:
    """Mock database that sometimes fails (to demonstrate fallbacks)"""

    # Mock database with limited data
    database = {
        "Big Mac": {"price": 45.0, "currency": "SEK"},
        "medium fries": {"price": 25.0, "currency": "SEK"},
        "medium Coke": {"price": 20.0, "currency": "SEK"},
    }

    return database.get(item.lower())


def mock_web_search(item: str) -> dict:
    """Mock web search fallback"""
    # In real implementation, this would search the web
    estimated_prices = {"chicken sandwich": 65.0, "homemade": 35.0, "lunch": 50.0}

    # Find best match or use default
    for key in estimated_prices:
        if key in item.lower():
            return {
                "price": estimated_prices[key],
                "currency": "SEK",
                "source": "web_estimate",
            }

    return {"price": 50.0, "currency": "SEK", "source": "default_estimate"}


def demo_context_management():
    """Show how context flows and accumulates through orchestration steps"""

    print("=== CONCEPT 2: Context Management ===\n")

    order = "Big Mac meal"

    # Step 1: Initial analysis (creates context)
    print("🔗 Step 1: Parse order and create context")
    analysis = analyze_meal_order(order)

    context = PriceContext(
        original_order=order, items=analysis.items, search_method="starting"
    )
    print(f"   Context created: {context.original_order}")
    print(f"   Items to price: {context.items}")

    # Step 2: Try database lookup (context accumulates)
    print("\n🔗 Step 2: Database lookup (context accumulates)")
    for item in context.items:
        price_data = mock_database_lookup(item)
        if price_data:
            context.prices_found.append({"item": item, **price_data})
            print(f"   ✅ Found {item}: {price_data['price']} {price_data['currency']}")
        else:
            print(f"   ❌ No database entry for: {item}")

    # Step 3: Calculate total (context completes)
    print("\n🔗 Step 3: Calculate total (context completion)")
    if context.prices_found:
        context.total_price = sum(item["price"] for item in context.prices_found)
        context.search_method = "database"
        print(f"   💰 Total: {context.total_price} SEK")
        print(f"   📊 Method: {context.search_method}")

    print(f"\n📦 Final Context State:")
    print(f"   Original: {context.original_order}")
    print(f"   Total Price: {context.total_price}")
    print(f"   Items Priced: {len(context.prices_found)}")
    print("-" * 50)


# ============================================================================
# CONCEPT 3: Fallback Strategies
# ============================================================================


def demo_fallback_patterns():
    """Show how fallbacks work when primary methods fail"""

    print("=== CONCEPT 3: Fallback Patterns ===\n")

    # Test with item not in our mock database
    item = "chicken sandwich"

    print(f"🔍 Pricing: '{item}'")

    # Primary: Try database
    print("   1️⃣ Primary: Database lookup")
    db_result = mock_database_lookup(item)
    if db_result:
        print(f"      ✅ Found: {db_result}")
        return db_result
    else:
        print(f"      ❌ Not found in database")

    # Fallback: Try web search
    print("   2️⃣ Fallback: Web search")
    web_result = mock_web_search(item)
    print(f"      ✅ Web estimate: {web_result}")

    print("\n💡 Key Insight: Fallbacks let us handle missing data gracefully")
    print("   Without fallbacks → System breaks")
    print("   With fallbacks → System provides best available answer")
    print("-" * 50)


# ============================================================================
# CONCEPT 4: When Orchestration is Needed vs Single Calls
# ============================================================================


def demo_when_to_orchestrate():
    """Show scenarios where orchestration is necessary vs single calls"""

    print("=== CONCEPT 4: When to Use Orchestration ===\n")

    scenarios = [
        {
            "task": "Write a creative story",
            "needs_orchestration": False,
            "reason": "Single LLM call is sufficient - no external data needed",
        },
        {
            "task": "Find cheapest lunch nearby",
            "needs_orchestration": True,
            "reason": "Needs: location → restaurants → prices → comparison",
        },
        {
            "task": "Calculate meal price for 'Big Mac meal'",
            "needs_orchestration": True,
            "reason": "Needs: parse items → lookup prices → calculate total",
        },
        {
            "task": "Explain what photosynthesis is",
            "needs_orchestration": False,
            "reason": "Single LLM call with knowledge is sufficient",
        },
    ]

    for scenario in scenarios:
        print(f"📋 Task: {scenario['task']}")
        print(
            f"   Orchestration needed: {'✅ YES' if scenario['needs_orchestration'] else '❌ NO'}"
        )
        print(f"   Reason: {scenario['reason']}")
        print()

    print(
        "🎯 Rule of thumb: Orchestrate when you need external data or multi-step processing"
    )
    print("-" * 50)


# ============================================================================
# Interactive Demo Runner
# ============================================================================

if __name__ == "__main__":
    print("🥘 Orchestration Concepts Demo")
    print("=" * 50)

    # Run all concept demonstrations
    demo_structured_triggers()
    print("\n")

    demo_context_management()
    print("\n")

    demo_fallback_patterns()
    print("\n")

    demo_when_to_orchestrate()

    print("\n🎓 Key Takeaways:")
    print("1. Structured outputs contain orchestration instructions")
    print("2. Context must be carefully managed across calls")
    print("3. Fallbacks are essential for robust systems")
    print("4. Not every task needs orchestration")
