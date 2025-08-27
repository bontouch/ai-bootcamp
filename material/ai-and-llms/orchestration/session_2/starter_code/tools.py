from typing import List
from pydantic import BaseModel
from agents import function_tool


class NutritionResult(BaseModel):
    total_calories: int
    health_category: str
    health_advice: str


@function_tool
def calculate_calories(calorie_list: List[int]) -> NutritionResult:
    # TODO: Sum all calories in the list
    total_calories = 0

    # TODO: Categorize the meal health based on total calories
    # Hint: Use the categorize_meal_health() helper function
    health_category = ""

    # TODO: Generate appropriate health advice based on calorie amount
    # Consider different ranges:
    # - < 300: Light meal advice
    # - 300-600: Balanced meal advice
    # - 600-900: Hearty meal advice
    # - 900-1200: High-calorie meal advice
    # - > 1200: Very high calorie meal advice
    health_advice = ""

    return NutritionResult(
        total_calories=total_calories,
        health_category=health_category,
        health_advice=health_advice,
    )


def categorize_meal_health(calories: int) -> str:
    """
    Categorize meal calories into health ranges.
    """
    # TODO: Return appropriate category based on calorie ranges
    # Suggested categories:
    # - "light": < 400 calories
    # - "moderate": 400-800 calories
    # - "heavy": > 800 calories
    return "moderate"
