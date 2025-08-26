"""
Calculator tools for meal price agent - Complete Implementation
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
    """
    total_price = sum(price_list)
    budget_category = categorize_meal_budget(total_price)

    # Generate budget advice based on price amount
    if total_price < 30:
        budget_advice = "Very budget-friendly - great value for money!"
    elif total_price < 50:
        budget_advice = "Budget meal - good option for everyday dining."
    elif total_price < 100:
        budget_advice = "Moderate price - typical for casual dining."
    elif total_price < 200:
        budget_advice = "Higher-end meal - good for special occasions."
    else:
        budget_advice = "Premium dining experience - quite expensive."

    return MealPriceResult(
        total_price=total_price,
        budget_category=budget_category,
        budget_advice=budget_advice,
    )


@function_tool
def categorize_meal_budget(price: float) -> str:
    """
    Categorize meal cost into budget ranges.

    Args:
        price: Total meal price in SEK

    Returns:
        Budget category string
    """
    if price < 50:
        return "budget"
    elif price < 150:
        return "moderate"
    else:
        return "expensive"


# Note: Removed format_price_summary function to avoid Pydantic schema issues
# The agent will handle formatting in its instructions instead
