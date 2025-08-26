import os
import json
from typing import Dict
from dotenv import load_dotenv
# TODO: Import your DocumentExtractor and ExtractionResult classes:
# from extractor import DocumentExtractor
# from models import ExtractionResult

load_dotenv()


"""
Receipt Processing Demo - CLI interface for structured receipt extraction
Demonstrates OpenAI API structured outputs with Pydantic validation
Supports sample data processing and interactive receipt entry

TODO: Create a complete CLI application that processes receipts and displays categorized results
"""


class ReceiptProcessingDemo:
    def __init__(self):
        # TODO: Initialize your DocumentExtractor here:
        # self.extractor = DocumentExtractor()
        pass

    def run_demo(self):
        # TODO: Load sample documents using _get_sample_documents()
        # TODO: Loop through each document and call extractor.extract_document(doc_text)
        # TODO: Display results using _display_result()
        pass

    def _get_sample_documents(self) -> Dict[str, str]:
        # TODO: Read ../sample_receipt.txt file content
        # TODO: Return dictionary with format: {"Sample Receipt": text_content}
        # TODO: Return empty dict if file not found
        pass

    def _display_result(
        self, doc_name: str, result
    ):  # result should be ExtractionResult
        # TODO: Check if result.was_successful()
        # TODO: If successful:
        #   - Print doc_name + ": SUCCESS"
        #   - Print f"Total: {doc.currency} {doc.total_amount}"
        #   - Print f"Items: {len(doc.line_items)}"
        #   - If doc.expense_categories exists:
        #     - Print f"Categories ({len(doc.expense_categories)}):"
        #     - For each category: print f"  • {category.category}: {doc.currency} {category.total_amount}"
        #     - For each item in category: print f"    - {item}"
        # TODO: If failed:
        #   - Print f"{doc_name}: FAILED - {result.error_message}"
        pass

    def interactive_mode(self):
        # TODO: Print instruction "Enter receipt text (type 'END' to finish):"
        # TODO: Create empty lines list
        # TODO: Loop reading input() until user types "END"
        # TODO: Join lines with newlines to create text
        # TODO: Call extractor.extract_document(text)
        # TODO: Display results using _display_result("Custom", result)
        # TODO: If successful, ask "Show JSON? (y/n)" and print JSON if requested
        #   - Use: json.dumps(result.document.model_dump(), indent=2, default=str)
        pass


def main():
    # TODO: Check if OPENAI_API_KEY environment variable is set

    # TODO: Create ReceiptProcessingDemo instance

    while True:
        print("\n1. Sample receipt")
        print("2. Interactive mode")
        print("3. Exit")

        choice = input("Choose (1-3): ").strip()

        try:
            if choice == "1":
                # Run demo
                pass
            elif choice == "2":
                # Run interactive mode
                pass
            elif choice == "3":
                break
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
