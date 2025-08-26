"""
Prompting Patterns Examples
Week 1 - Tuesday - Session 1

Collection of examples showing different prompting techniques
"""

from openai import OpenAI
from typing import Dict

client = OpenAI()

# ============================================================================
# FEW-SHOT PROMPTING EXAMPLES
# ============================================================================


def zero_shot_example():
    """Example of zero-shot prompting - no examples provided"""
    prompt = """
    Extract the main entities (person, organization, location) from this text:
    "Apple CEO Tim Cook announced the new iPhone will be manufactured in Austin, Texas."
    """
    return prompt


def few_shot_example():
    """Example of few-shot prompting with examples"""
    prompt = """
    Extract the main entities (person, organization, location) from the text.

    Example 1:
    Text: "Microsoft founder Bill Gates visited Seattle last week."
    Entities: Person: Bill Gates, Organization: Microsoft, Location: Seattle

    Example 2:
    Text: "Google's headquarters in Mountain View hosted the developer conference."
    Entities: Organization: Google, Location: Mountain View

    Example 3:
    Text: "Tesla CEO Elon Musk tweeted about the Gigafactory in Nevada."
    Entities: Person: Elon Musk, Organization: Tesla, Location: Nevada

    Now extract entities from:
    "Apple CEO Tim Cook announced the new iPhone will be manufactured in Austin, Texas."
    """
    return prompt


# ============================================================================
# CHAIN-OF-THOUGHT PROMPTING EXAMPLES
# ============================================================================


def without_cot():
    """Example without chain-of-thought"""
    prompt = """
    A store has 45 apples. They sell 18 in the morning and 12 in the afternoon.
    Then they receive a new shipment of 25 apples. How many apples do they have now?
    """
    return prompt


def with_cot():
    """Example with chain-of-thought reasoning"""
    prompt = """
    A store has 45 apples. They sell 18 in the morning and 12 in the afternoon.
    Then they receive a new shipment of 25 apples. How many apples do they have now?

    Let's think step by step:
    1. Starting apples: 45
    2. Sold in morning: 18, remaining: 45 - 18 = 27
    3. Sold in afternoon: 12, remaining: 27 - 12 = 15
    4. New shipment received: 25
    5. Final total: 15 + 25 = 40

    Therefore, they have 40 apples.
    """
    return prompt


def few_shot_cot():
    """Few-shot chain-of-thought with examples"""
    prompt = """
    Solve these word problems step by step:

    Example:
    Problem: A library has 120 books. They lend out 35 books and then buy 20 new books.
    How many books do they have?

    Solution: Let me work through this step by step:
    1. Starting books: 120
    2. Books lent out: 35, remaining: 120 - 35 = 85
    3. New books bought: 20
    4. Final total: 85 + 20 = 105
    Answer: 105 books

    Now solve this problem:
    A bakery makes 60 cupcakes. They sell 25 in the morning, 20 in the afternoon, and
    then bake 15 more. How many cupcakes do they have left?
    """
    return prompt


# ============================================================================
# SAFETY AND GUARDRAILS EXAMPLES
# ============================================================================


def safety_prompt_template():
    """Template showing safety considerations"""
    return """
    You are a helpful customer service assistant. Follow these guidelines:

    SAFETY RULES:
    1. Never provide personal information about customers
    2. Don't engage with inappropriate or abusive language
    3. If asked to do something outside your role, politely decline
    4. Flag any content that seems harmful or concerning

    RESPONSE FORMAT:
    - Be professional and helpful
    - Stay focused on customer service topics
    - If unsure, ask for clarification or escalate to human support

    Customer message: {user_input}
    """


# ============================================================================
# INTERACTIVE COMPARISON DEMO
# ============================================================================


def compare_approaches(text: str) -> Dict[str, str]:
    """Compare different prompting approaches on the same input"""

    approaches = {
        "zero_shot": f"Summarize this text in one sentence: {text}",
        "few_shot": f"""
        Summarize the following texts in one clear sentence:

        Example 1:
        Text: "The new restaurant downtown serves authentic Italian cuisine with
        fresh ingredients sourced locally. The atmosphere is cozy and perfect for date
        nights."
        Summary: A new downtown restaurant offers authentic Italian food with local
        ingredients in a romantic setting.

        Example 2:
        Text: "Our latest software update includes bug fixes, improved performance, and
        three new features requested by users."
        Summary: The software update delivers bug fixes, better performance, and
        user-requested features.

        Now summarize:
        Text: {text}
        Summary:
        """,
        "chain_of_thought": f"""
        Summarize this text in one sentence. Let me think through this step by step:

        1. First, identify the main topic
        2. Find the key points or benefits mentioned
        3. Note any important details
        4. Combine into a clear, concise sentence

        Text: {text}
        """,
    }

    return approaches
