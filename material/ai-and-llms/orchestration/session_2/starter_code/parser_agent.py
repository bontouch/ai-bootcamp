from agents import Agent, Runner


def create_food_parser_agent() -> Agent:
    """
    Create a food parser agent that breaks down complex food orders.

    Returns:
        Agent configured to parse food orders into individual items
    """

    # TODO: Write instructions for the food parsing specialist agent
    # Hints for effective parsing instructions:
    # - Define the agent's role (food parsing specialist)
    # - Specify the goal (break complex orders into individual searchable items)
    # - Include parsing guidelines:
    #   * Break complex orders into components
    #   * Be specific about restaurant chains when mentioned
    #   * Include portion sizes when specified
    #   * Return simple list format
    #   * Don't add items that weren't mentioned
    # - Provide concrete examples showing input → output transformations
    # - Specify the exact output format (list of items, one per line)

    instructions = """
    TODO: Write comprehensive instructions for the food parser agent

    Consider including:
    - Agent role and purpose
    - Parsing guidelines and rules
    - Specific examples with different food types:
      * Fast food meals
      * International cuisine
      * Salads and complex dishes
      * Pizza with toppings
      * Pasta dishes
      * Burrito bowls
      * Burgers with sides
      * Greek/Mediterranean dishes
    - Output format specification
    """

    parser_agent = Agent(
        name="food_parser",
        instructions=instructions,
    )

    return parser_agent
