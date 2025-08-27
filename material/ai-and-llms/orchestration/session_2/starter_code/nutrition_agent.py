from agents import Agent, WebSearchTool, Runner
from parser_agent import create_food_parser_agent
from tools import calculate_calories


def create_nutrition_agent() -> Agent:
    """
    Create the main nutrition estimator agent with all tools.

    Returns:
        Agent configured with WebSearch, calculator tools, and parser agent
    """
    # TODO: Create the food parser agent
    parser_agent = create_food_parser_agent()

    # TODO: Write instructions for the nutrition estimator agent
    # Hints for writing effective agent instructions:
    # - Define the agent's role (nutrition estimator)
    # - Outline a clear 4-5 step workflow
    # - Specify search strategy (what to search for, which sources to trust)
    # - Include guidance on data extraction (calories per serving, portion sizes)
    # - Emphasize accuracy and double-checking results

    instructions = """
    TODO: Write comprehensive instructions for the nutrition agent

    Consider including:
    - Agent role and purpose
    - Step-by-step workflow using available tools
    - Search strategy for finding nutrition data
    - Data extraction guidelines
    - Quality and accuracy requirements
    """

    # TODO: Create and configure the nutrition agent with tools
    nutrition_agent = Agent(
        name="nutrition_estimator",
        instructions=instructions,
        tools=[
            # TODO: Add the parser agent as a tool
            # This tool breaks complex orders into individual searchable items
            # Hint: Use parser_agent.as_tool(tool_name="food_parser", tool_description="...")
            # TODO: Add WebSearchTool for nutrition lookups
            # This tool searches the web for nutrition information
            # Hint: Import and instantiate WebSearchTool()
            # TODO: Add calculator function for calorie totaling
            # This tool sums calories and provides health categorization
            # Hint: Use the calculate_calories function imported from tools
        ],
    )

    return nutrition_agent


def estimate_nutrition(food_order: str) -> str:
    # TODO: Instantiate the nutrition agent

    try:
        # TODO: Create simple prompt and run the agent
        # Hint: The agent instructions contain the full workflow,
        # so just ask for the calorie calculation
        # Use: Runner.run_sync(agent, prompt)

        return "TODO: Implement agent execution"

    except Exception as e:
        return f"❌ Error processing food order: {str(e)}"
