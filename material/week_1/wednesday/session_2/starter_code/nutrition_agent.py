"""
Main Nutrition Agent - Orchestrates food parsing, web search, and calculations
"""

from agents import Agent, WebSearchTool
from parser_agent import create_food_parser_agent
from tools import calculate_calories, format_nutrition_summary


def create_nutrition_agent() -> Agent:
    """
    Create the main nutrition agent with all tools.

    Returns:
        Agent configured with WebSearch, calculator tools, and parser agent

    TODO: Implement the main nutrition agent
    """

    # TODO: Create the food parser agent
    parser_agent = create_food_parser_agent()

    # TODO: Define instructions for the main agent
    instructions = """
    TODO: Write instructions for the nutrition agent
    
    You are a nutrition estimator that helps users understand the calorie content of their food.
    
    Your workflow:
    1. Use the food_parser tool to break complex orders into individual items
    2. Use web_search to find calorie information for each food item  
    3. Use calculate_calories to sum totals and get daily percentage
    4. Provide helpful health context about the calorie amount
    
    Always be accurate with nutrition data and provide realistic health advice.
    """

    # TODO: Create and configure the main agent with tools
    nutrition_agent = Agent(
        name="nutrition_estimator",
        instructions=instructions,
        tools=[
            # TODO: Add the parser agent as a tool
            # parser_agent.as_tool(...),
            # TODO: Add WebSearchTool for nutrition lookups
            # WebSearchTool(),
            # TODO: Add calculator function
            # calculate_calories,
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

    TODO: Implement the nutrition estimation workflow
    """

    # TODO: Create the nutrition agent
    agent = create_nutrition_agent()

    # TODO: Process the food order through the agent
    # This should trigger the full workflow:
    # 1. Parse food order
    # 2. Search for nutrition data
    # 3. Calculate totals
    # 4. Format results

    try:
        # TODO: Run the agent with the food order
        response = "TODO: Implement agent execution"
        return response

    except Exception as e:
        return f"❌ Error processing food order: {str(e)}"


# Test the nutrition agent
if __name__ == "__main__":
    test_orders = [
        "Big Mac + medium fries + Coke",
        "Thai green curry with jasmine rice",
        "chicken caesar salad",
    ]

    for order in test_orders:
        print(f"🍽️  Order: {order}")
        result = estimate_nutrition(order)
        print(f"📊 Result: {result}")
        print("-" * 50)
