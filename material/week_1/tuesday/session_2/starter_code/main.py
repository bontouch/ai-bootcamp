"""
Receipt Processing Demo
Week 1 - Tuesday - Session 2 Lab

TODO: Create a CLI application that processes receipts and displays categorized results
"""

import os
from dotenv import load_dotenv
# TODO: Import your classes here

# Load environment variables
load_dotenv()


def load_sample_receipt():
    """Load the sample receipt from file"""
    # TODO: Read sample_receipt.txt and return the content
    pass


def display_results(result):
    """Display extraction results with categorized items"""
    # TODO: Show success/failure status
    # TODO: Display total amount and item count
    # TODO: Show expense categories with items listed under each
    pass


def interactive_mode():
    """Allow user to input custom receipt text"""
    # TODO: Prompt user to enter receipt text
    # TODO: Process the input and display results
    pass


def main():
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: Set OPENAI_API_KEY environment variable")
        return

    # TODO: Initialize your ReceiptExtractor

    while True:
        print("\nReceipt Expense Categorization Demo")
        print("1. Process sample receipt")
        print("2. Interactive mode (enter your own receipt)")
        print("3. Exit")

        choice = input("\nChoose (1-3): ").strip()

        # TODO: Implement menu options
        # 1. Load and process sample_receipt.txt
        # 2. Allow custom receipt input
        # 3. Exit


if __name__ == "__main__":
    main()
