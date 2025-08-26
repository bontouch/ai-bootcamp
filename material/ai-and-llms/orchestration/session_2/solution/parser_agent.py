"""
Food Parser Agent - Complete Implementation
"""

from agents import Agent, Runner


def create_food_parser_agent() -> Agent:
    """
    Create a food parser agent that breaks down complex food orders.

    Returns:
        Agent configured to parse food orders into individual items
    """

    instructions = """
    You are a food parsing specialist. Your job is to break down complex food orders
    into individual, searchable food items.

    Guidelines:
    - Break complex orders like "Big Mac meal" into individual components
    - Be specific about restaurant chains when mentioned (e.g., "McDonald's Big Mac")
    - Include portion sizes when specified (e.g., "medium fries", "large pizza")
    - Return a simple list of items that can be searched for pricing data
    - Don't add items that weren't mentioned

    Examples:
    - "Big Mac meal" → ["Big Mac", "McDonald's medium fries", "medium Coca-Cola"]
    - "Thai green curry with rice" → ["Thai green curry", "jasmine rice portion"]
    - "chicken caesar salad with croutons" → ["chicken caesar salad", "croutons"]
    - "large pizza margherita extra cheese" → ["large margherita pizza with extra
    cheese"]

    Always return just the list of food items, one per line, without bullets or numbers.
    """

    parser_agent = Agent(
        name="food_parser",
        instructions=instructions,
    )

    return parser_agent


# Test the parser agent
if __name__ == "__main__":
    parser = create_food_parser_agent()

    test_orders = [
        "Big Mac meal",
        "Thai green curry with rice",
        "chicken caesar salad with croutons",
        "large pizza margherita extra cheese",
    ]

    for order in test_orders:
        print(f"Order: {order}")
        result = Runner.run_sync(parser, f"Parse this food order: {order}")
        print("Parsed items:")
        print(result.final_output)
        print("-" * 40)
