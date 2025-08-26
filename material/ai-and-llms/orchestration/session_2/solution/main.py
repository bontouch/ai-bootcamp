"""
CLI interface for the Meal Price Calculator Agent - Complete Implementation
"""

import os
from price_agent import estimate_meal_price


def load_sample_queries(filename: str = "../meal_queries.txt") -> list:
    """
    Load sample meal queries from file.

    Returns:
        List of meal query strings
    """
    try:
        with open(filename, "r") as file:
            queries = [line.strip() for line in file if line.strip()]
        return queries

    except FileNotFoundError:
        print(f"⚠️  Sample file {filename} not found")
        return []


def interactive_mode():
    """
    Interactive CLI for testing meal price estimation.
    """
    print("💰 Meal Price Calculator Agent")
    print("=" * 40)
    print("Enter food orders to get price estimates.")
    print("Type 'quit' to exit, 'samples' to see sample queries.")
    print()

    while True:
        user_input = input("Enter food order: ").strip()

        if user_input.lower() == "quit":
            print("👋 Goodbye!")
            break
        elif user_input.lower() == "samples":
            show_sample_queries()
        elif user_input:
            print(f"\n🔍 Processing: {user_input}")
            print("-" * 40)
            result = estimate_meal_price(user_input)
            print(result)
            print("-" * 40)
        else:
            print("Please enter a food order or 'quit' to exit.")


def show_sample_queries():
    """
    Display sample queries for users to try.
    """
    samples = [
        "Big Mac + medium fries + Coke",
        "Thai green curry with jasmine rice",
        "chicken caesar salad with croutons",
        "Starbucks venti caramel macchiato",
        "avocado toast with poached egg",
    ]

    print("\n📋 Sample food orders to try:")
    for i, sample in enumerate(samples, 1):
        print(f"  {i}. {sample}")
    print()


def batch_mode():
    """
    Process all sample queries in batch mode.
    """
    print("💰 Meal Price Calculator - Batch Mode")
    print("=" * 40)

    queries = load_sample_queries()

    if not queries:
        print("No sample queries found.")
        return

    print(f"Processing {len(queries)} sample queries...\n")

    for i, query in enumerate(queries, 1):
        print(f"[{i}/{len(queries)}] {query}")
        print("-" * 40)

        try:
            result = estimate_meal_price(query)
            print(result)
        except Exception as e:
            print(f"❌ Error: {str(e)}")

        print("=" * 60)

        # Pause between requests to avoid rate limits
        if i < len(queries):
            input("\nPress Enter to continue to next query...")


def main():
    """
    Main CLI entry point.
    """

    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("Please set your OpenAI API key:")
        print("export OPENAI_API_KEY='your-key-here'")
        return

    print("Choose mode:")
    print("1. Interactive mode - Enter food orders manually")
    print("2. Batch mode - Process all sample queries")

    choice = input("\nEnter choice (1 or 2): ").strip()

    if choice == "1":
        interactive_mode()
    elif choice == "2":
        batch_mode()
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
