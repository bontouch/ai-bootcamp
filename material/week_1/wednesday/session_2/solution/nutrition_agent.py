"""
Main Nutrition Agent - Complete Implementation
"""

from agents import Agent, WebSearchTool
from parser_agent import create_food_parser_agent
from tools import calculate_calories


def create_nutrition_agent() -> Agent:
    """
    Create the main nutrition agent with all tools.

    Returns:
        Agent configured with WebSearch, calculator tools, and parser agent
    """

    parser_agent = create_food_parser_agent()

    instructions = """
    You are a nutrition estimator that helps users understand the calorie content of
    their food orders.

    Your workflow:
    1. Use the food_parser tool to break complex orders into individual searchable items
    2. Use web_search to find accurate calorie information for each food item
    3. Extract calorie numbers from search results carefully
    4. Use calculate_calories to sum totals and get health advice
    5. Format results in a clear, helpful summary

    Search Strategy:
    - Search for "{food item} calories nutrition facts"
    - Look for reputable sources (USDA, restaurant nutrition info, health sites)
    - Extract calorie numbers carefully - look for "calories per serving" or similar
    - If multiple values found, use the most reasonable/average one
    - For restaurant items, prefer official restaurant nutrition data

    Be accurate with nutrition data and provide realistic health advice.
    Always double-check your calorie extractions before calculating totals.
    """

    nutrition_agent = Agent(
        name="nutrition_estimator",
        instructions=instructions,
        tools=[
            parser_agent.as_tool(
                tool_name="food_parser",
                tool_description=(
                    "Break complex food orders into individual searchable items"
                ),
            ),
            WebSearchTool(),
            calculate_calories,
        ],
    )

    return nutrition_agent


def estimate_nutrition(food_order: str) -> str:
    """
    Main function to estimate nutrition for a food order.

    Args:
        food_order: Complex food order string

    Returns:
        Formatted nutrition summary
    """

    agent = create_nutrition_agent()

    try:
        # Run the agent with a comprehensive prompt
        prompt = f"""
        Estimate the total calories for this food order: "{food_order}"

        Follow this process:
        1. Parse the order into individual food items
        2. Search for calorie information for each item
        3. Calculate the total calories and daily percentage
        4. Provide a formatted summary with health advice

        Be thorough in your searches and accurate with calorie extraction.
        """

        response = agent.run(prompt)
        return response

    except Exception as e:
        return f"❌ Error processing food order: {str(e)}"


# Test the nutrition agent
if __name__ == "__main__":
    test_orders = [
        "Big Mac + medium fries + Coke",
        "Thai green curry with jasmine rice",
        "chicken caesar salad with croutons",
    ]

    for order in test_orders:
        print(f"🍽️  Order: {order}")
        result = estimate_nutrition(order)
        print(f"📊 Result:\n{result}")
        print("=" * 60)
