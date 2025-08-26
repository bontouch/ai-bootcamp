"""
Main Price Calculator Agent - Orchestrates food parsing, web search, and calculations
"""

from agents import Agent, WebSearchTool, Runner
from parser_agent import create_food_parser_agent
from tools import calculate_meal_price


def create_price_agent() -> Agent:
    """
    Create the main price calculator agent with all tools.
    
    Returns:
        Agent configured with WebSearch, calculator tools, and parser agent
        
    TODO: Implement the main price agent
    """
    
    # TODO: Create the food parser agent  
    parser_agent = create_food_parser_agent()
    
    # TODO: Define instructions for the main agent
    instructions = """
    TODO: Write instructions for the price calculator agent
    
    You are a meal price calculator that helps users understand the cost of their food orders.
    
    Your workflow:
    1. Use the food_parser tool to break complex orders into individual items
    2. Use web_search to find price information for each food item  
    3. Use calculate_meal_price to sum totals and get budget category
    4. Provide helpful budget context about the meal cost
    
    Always search for current, accurate pricing data and provide realistic budget advice.
    """
    
    # TODO: Create and configure the main agent with tools
    price_agent = Agent(
        name="price_calculator",
        instructions=instructions,
        tools=[
            # TODO: Add the parser agent as a tool
            # parser_agent.as_tool(...),
            
            # TODO: Add WebSearchTool for price lookups
            # WebSearchTool(),
            
            # TODO: Add calculator function
            # calculate_meal_price,
        ]
    )
    
    return price_agent


def estimate_meal_price(food_order: str) -> str:
    """
    Main function to estimate price for a food order.
    
    Args:
        food_order: Complex food order string
        
    Returns:
        Formatted price summary
        
    TODO: Implement the price estimation workflow
    """
    
    # TODO: Create the price agent
    agent = create_price_agent()
    
    # TODO: Process the food order through the agent
    # This should trigger the full workflow:
    # 1. Parse food order
    # 2. Search for pricing data
    # 3. Calculate totals
    # 4. Format results
    
    try:
        # TODO: Run the agent with the food order using Runner.run_sync()
        # result = Runner.run_sync(agent, food_order)
        # return result.final_output
        response = "TODO: Implement agent execution"
        return response
        
    except Exception as e:
        return f"❌ Error processing food order: {str(e)}"


# Test the price agent
if __name__ == "__main__":
    test_orders = [
        "Big Mac + medium fries + Coke",
        "Thai green curry with jasmine rice",
        "chicken caesar salad"
    ]
    
    for order in test_orders:
        print(f"🍽️  Order: {order}")
        result = estimate_meal_price(order)
        print(f"💰 Result: {result}")
        print("-" * 50)