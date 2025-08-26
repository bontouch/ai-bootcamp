"""
Main Price Calculator Agent - Complete Implementation
"""

from agents import Agent, WebSearchTool, Runner
from parser_agent import create_food_parser_agent
from tools import calculate_meal_price


def create_price_agent() -> Agent:
    """
    Create the main price calculator agent with all tools.

    Returns:
        Agent configured with WebSearch, calculator tools, and parser agent
    """

    parser_agent = create_food_parser_agent()

    instructions = """
    You are a meal price calculator that helps users understand the cost of their food
    orders.

    Your workflow:
    1. Use the food_parser tool to break complex orders into individual searchable items
    2. Use web_search to find accurate pricing information for each food item
    3. Extract price numbers from search results carefully
    4. Use calculate_meal_price to sum totals and get budget advice
    5. Format results in a clear, helpful summary

    Search Strategy:
    - Search for "{food item} price {restaurant} Sweden" or "{food item} cost SEK"
    - Look for reputable sources (restaurant websites, food delivery apps, price
    comparison sites)
    - Extract price numbers carefully - look for "SEK", "kr", or Swedish pricing
    - If multiple values found, use the most reasonable/average one
    - For restaurant items, prefer official restaurant pricing or delivery app prices
    - Convert other currencies to SEK if needed (1 EUR ≈ 11 SEK, 1 USD ≈ 10 SEK)

    Be accurate with pricing data and provide realistic budget advice.
    Always double-check your price extractions before calculating totals.
    """

    price_agent = Agent(
        name="price_calculator",
        instructions=instructions,
        tools=[
            parser_agent.as_tool(
                tool_name="food_parser",
                tool_description=(
                    "Break complex food orders into individual searchable items"
                ),
            ),
            WebSearchTool(),
            calculate_meal_price,
        ],
    )

    return price_agent


def estimate_meal_price(food_order: str) -> str:
    """
    Main function to estimate price for a food order.

    Args:
        food_order: Complex food order string

    Returns:
        Formatted price summary
    """

    agent = create_price_agent()

    try:
        # Run the agent with a comprehensive prompt
        prompt = f"""
        Calculate the total price for this food order: "{food_order}"

        Follow this process:
        1. Parse the order into individual food items
        2. Search for current pricing information for each item in Sweden
        3. Calculate the total price and budget category
        4. Provide a formatted summary with budget advice

        Be thorough in your searches and accurate with price extraction.
        Focus on Swedish pricing (SEK) and current market rates.
        """

        result = Runner.run_sync(agent, prompt)
        return result.final_output

    except Exception as e:
        return f"❌ Error processing food order: {str(e)}"


# Test the price agent
if __name__ == "__main__":
    test_orders = [
        "Big Mac + medium fries + Coke",
        "Thai green curry with jasmine rice",
        "chicken caesar salad with croutons",
    ]

    for order in test_orders:
        print(f"🍽️  Order: {order}")
        result = estimate_meal_price(order)
        print(f"💰 Result:\n{result}")
        print("=" * 60)
