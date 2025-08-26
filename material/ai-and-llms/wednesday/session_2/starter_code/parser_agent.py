"""
Food Parser Agent - Breaks complex food orders into searchable items
"""

from agents import Agent, Runner


def create_food_parser_agent() -> Agent:
    """
    Create a food parser agent that breaks down complex food orders.

    Returns:
        Agent configured to parse food orders into individual items

    TODO: Implement the food parser agent
    """

    # TODO: Define clear instructions for the agent
    instructions = """
    TODO: Write instructions for the food parser agent
    
    The agent should:
    - Take complex food orders like "Big Mac meal" or "Thai curry with rice"
    - Break them down into individual, searchable food items
    - Be specific about portions and restaurant chains when possible
    - Return a simple list of food items that can be searched for pricing data
    
    Examples:
    - "Big Mac meal" → ["Big Mac", "McDonald's medium fries", "medium Coca-Cola"]
    - "Thai curry with rice" → ["Thai green curry", "jasmine rice portion"]
    """

    # TODO: Create and return the Agent
    parser_agent = Agent(
        name="food_parser",
        instructions=instructions,
    )

    return parser_agent


# Test the parser agent
if __name__ == "__main__":
    parser = create_food_parser_agent()

    test_orders = ["Big Mac meal", "Thai green curry with rice", "chicken caesar salad"]

    for order in test_orders:
        print(f"Order: {order}")
        # TODO: Test the parser agent with sample orders
        # result = Runner.run_sync(parser, f"Parse this food order: {order}")
        # print(f"Parsed: {result.final_output}")
        print()
