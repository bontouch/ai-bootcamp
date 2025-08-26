"""
CLI interface for the Meal Price Calculator Agent
"""

import os
from price_agent import estimate_meal_price


def load_sample_queries(filename: str = "../meal_queries.txt") -> list:
    """
    Load sample meal queries from file.
    
    Returns:
        List of meal query strings
        
    TODO: Implement file loading
    """
    try:
        # TODO: Load meal queries from the file
        # Handle file not found gracefully
        return []
        
    except FileNotFoundError:
        print(f"⚠️  Sample file {filename} not found")
        return []


def interactive_mode():
    """
    Interactive CLI for testing meal price estimation.
    
    TODO: Implement interactive mode
    """
    print("💰 Meal Price Calculator Agent")
    print("=" * 40)
    print("Enter food orders to get price estimates.")
    print("Type 'quit' to exit, 'samples' to see sample queries.")
    print()
    
    while True:
        # TODO: Implement interactive loop
        user_input = input("Enter food order: ").strip()
        
        if user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'samples':
            # TODO: Show sample queries
            pass
        elif user_input:
            # TODO: Process the user's food order
            print("TODO: Process food order")
        else:
            print("Please enter a food order or 'quit' to exit.")


def batch_mode():
    """
    Process all sample queries in batch mode.
    
    TODO: Implement batch processing
    """
    print("💰 Meal Price Calculator - Batch Mode")
    print("=" * 40)
    
    # TODO: Load sample queries
    queries = load_sample_queries()
    
    if not queries:
        print("No sample queries found.")
        return
    
    # TODO: Process each query and display results
    for i, query in enumerate(queries, 1):
        print(f"\n[{i}/{len(queries)}] {query}")
        # TODO: Estimate meal price and display result


def main():
    """
    Main CLI entry point.
    
    TODO: Implement main function with mode selection
    """
    
    # TODO: Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("Please set your OpenAI API key:")
        print("export OPENAI_API_KEY='your-key-here'")
        return
    
    print("Choose mode:")
    print("1. Interactive mode - Enter food orders manually")
    print("2. Batch mode - Process all sample queries")
    
    # TODO: Implement mode selection and execution
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    if choice == "1":
        interactive_mode()
    elif choice == "2":
        batch_mode()
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()