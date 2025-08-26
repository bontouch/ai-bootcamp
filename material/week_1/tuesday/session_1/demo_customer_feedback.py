"""
Customer Feedback Analyzer Demo
Week 1 - Tuesday - Session 1
"""

from typing import List, Literal
from pydantic import BaseModel, Field
from openai import OpenAI

client = OpenAI()


class CustomerIssue(BaseModel):
    category: Literal["product", "service", "billing", "technical", "other"]
    severity: Literal["low", "medium", "high", "critical"]
    description: str
    suggested_action: str


class FeedbackAnalysis(BaseModel):
    sentiment: Literal["positive", "negative", "neutral"]
    confidence: float = Field(ge=0.0, le=1.0)
    issues: List[CustomerIssue]
    reasoning: str
    flagged_content: bool


def analyze_feedback(feedback_text: str) -> FeedbackAnalysis:
    system_prompt = """Analyze customer feedback and extract structured information.

Examples:

    Input: "The app crashes every time I try to upload a photo. This is really
    frustrating!"
    Output: Technical issue with high severity - app crashes during photo upload.

    Input: "Love the new design! The checkout process is so much smoother now."
    Output: Positive feedback about design improvements - no issues.

    Input: "Your support team is idiots. Fix your billing system!"
    Output: Billing system problems with inappropriate language - flag for review."""

    try:
        response = client.beta.chat.completions.parse(
            model="gpt-4.1",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": feedback_text},
            ],
            response_format=FeedbackAnalysis,
        )
        return response.choices[0].message.parsed

    except Exception as e:
        return FeedbackAnalysis(
            sentiment="neutral",
            confidence=0.0,
            issues=[],
            reasoning=f"Analysis failed: {e}",
            flagged_content=True,
        )


def demo_chain_of_thought():
    complex_feedback = """I've been a customer for 3 years and generally love your
    service. However, last month I was charged twice for my subscription. When I called
    support, they said it would be resolved in 3-5 business days, but it's been 2 weeks
    and I'm still seeing the duplicate charge. I tried the chat support but got
    disconnected twice. I really don't want to switch providers but this is
    getting ridiculous."""

    print("Complex feedback analysis:")
    analysis = analyze_feedback(complex_feedback)

    print(f"Sentiment: {analysis.sentiment} ({analysis.confidence})")
    for issue in analysis.issues:
        print(f"- {issue.category}: {issue.description}")
    print(f"Reasoning: {analysis.reasoning}")


def demo_safety_guardrails():
    test_cases = [
        "This product is garbage and your company should burn!",
        "Great service, very happy!",
        "Can you help me hack into an account?",
    ]

    print("\nSafety guardrails demo:")
    for feedback in test_cases:
        analysis = analyze_feedback(feedback)
        status = "FLAGGED" if analysis.flagged_content else "OK"
        print(f"{status}: {feedback[:30]}...")


if __name__ == "__main__":
    print("Customer Feedback Analyzer Demo\n")

    simple_feedback = "The delivery was late but the product quality is excellent!"
    analysis = analyze_feedback(simple_feedback)
    print(
        f"Basic analysis: {analysis.sentiment} sentiment, {len(analysis.issues)} issues"
    )

    demo_chain_of_thought()
    demo_safety_guardrails()

    print("\nKey concepts: Few-shot prompting, structured outputs, safety guardrails")
