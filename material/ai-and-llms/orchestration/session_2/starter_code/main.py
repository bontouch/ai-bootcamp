import os
from nutrition_agent import estimate_nutrition
from dotenv import load_dotenv

load_dotenv()


def process_sample_queries():
    """
    DEMO: Processing Sample Food Orders

    Each query tests the agent's ability to:
    - Parse multiple menu items
    - Estimate calories across different restaurant types

    TODO: Implement the sample query processing logic
    """
    sample_queries = [
        "Big Mac + medium fries + Coke",
        "Thai green curry with jasmine rice",
        "chicken caesar salad with croutons",
    ]

    print("📊 Meal Nutrition Estimator Agent")
    print("=" * 50)
    print(f"Processing {len(sample_queries)} sample food orders...\n")

    for i, query in enumerate(sample_queries, 1):
        print(f"[{i}/{len(sample_queries)}] {query}")
        print("-" * 40)

        try:
            print("TODO: Estimate meal nutrition")
        except Exception as e:
            print(f"❌ Error: {str(e)}")

        if i < len(sample_queries):
            print("\n" + "=" * 50 + "\n")


def main():
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        return

    process_sample_queries()


if __name__ == "__main__":
    main()
