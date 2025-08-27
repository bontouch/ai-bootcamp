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
    - "Thai green curry with rice" → ["jasmine rice portion", "coconut milk", "Thai basil", "chicken breast"]
    - "chicken caesar salad with croutons" → ["grilled chicken breast", "caesar salad lettuce", "parmesan cheese", "caesar dressing", "bread croutons"]
    - "large pizza margherita extra cheese" → ["large pizza dough", "tomato sauce", "mozzarella cheese", "extra mozzarella cheese", "fresh basil"]
    - "spaghetti carbonara" → ["spaghetti pasta", "bacon bits", "eggs", "parmesan cheese", "black pepper", "olive oil"]
    - "chicken burrito bowl" → ["grilled chicken", "cilantro lime rice", "black beans", "corn salsa", "cheese", "sour cream", "guacamole"]
    - "veggie burger with fries" → ["veggie patty", "burger bun", "lettuce", "tomato", "pickles", "french fries", "ketchup"]
    - "Greek salad" → ["mixed greens", "feta cheese", "olives", "cucumber", "tomatoes", "red onion", "olive oil dressing"]

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
