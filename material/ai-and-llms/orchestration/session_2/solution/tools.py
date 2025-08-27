from typing import List
from pydantic import BaseModel
from agents import function_tool


class NutritionResult(BaseModel):
    total_calories: int
    health_category: str
    health_advice: str


@function_tool
def calculate_calories(calorie_list: List[int]) -> NutritionResult:
    total_calories = sum(calorie_list)
    health_category = categorize_meal_health(total_calories)

    # Generate health advice based on calorie amount
    if total_calories < 300:
        health_advice = "Light meal - great for snacks or weight management."
    elif total_calories < 600:
        health_advice = "Balanced meal - appropriate for most people."
    elif total_calories < 900:
        health_advice = "Hearty meal - good for active individuals or main meals."
    elif total_calories < 1200:
        health_advice = (
            "High-calorie meal - consider for post-workout or special occasions."
        )
    else:
        health_advice = "Very high calorie meal - should be consumed mindfully."

    return NutritionResult(
        total_calories=total_calories,
        health_category=health_category,
        health_advice=health_advice,
    )


def categorize_meal_health(calories: int) -> str:
    """
    Categorize meal calories into health ranges.
    """
    if calories < 400:
        return "light"
    elif calories < 800:
        return "moderate"
    else:
        return "heavy"
