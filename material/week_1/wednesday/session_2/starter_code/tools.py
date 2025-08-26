"""
Calculator tools for meal price agent
"""

from typing import List
from pydantic import BaseModel
from agents import function_tool


class MealPriceResult(BaseModel):
    """Result from meal price calculation"""
    total_price: float
    budget_category: str
    budget_advice: str


@function_tool
def calculate_meal_price(price_list: List[float]) -> MealPriceResult:
    """
    Calculate total price and budget category.
    
    Args:
        price_list: List of price values for each food item
        
    Returns:
        MealPriceResult with total price, budget category, and budget advice
        
    TODO: Implement this function
    - Calculate total price
    - Determine budget category (budget/moderate/expensive)
    - Generate appropriate budget advice based on total
    """
    # TODO: Sum all prices in the list
    total_price = 0.0
    
    # TODO: Determine budget category using categorize_meal_budget()
    budget_category = ""
    
    # TODO: Generate budget advice based on price amount
    budget_advice = ""
    
    return MealPriceResult(
        total_price=total_price,
        budget_category=budget_category,
        budget_advice=budget_advice
    )


@function_tool
def categorize_meal_budget(price: float) -> str:
    """
    Categorize meal cost into budget ranges.
    
    Args:
        price: Total meal price in SEK
        
    Returns:
        Budget category string
        
    TODO: Implement price categorization
    - budget: < 50 SEK
    - moderate: 50-150 SEK  
    - expensive: > 150 SEK
    """
    # TODO: Implement categorization logic
    return "moderate"


# Note: Removed format_price_summary function to avoid Pydantic schema issues
# TODO: The agent should handle formatting in its instructions instead
# You can create helper functions without @function_tool if needed for internal use