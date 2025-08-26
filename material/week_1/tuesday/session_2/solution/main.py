"""Receipt Processing Demo"""

import os
import json
from typing import Dict
from dotenv import load_dotenv
from extractor import DocumentExtractor
from models import ExtractionResult

# Load environment variables
load_dotenv()


class ReceiptProcessingDemo:
    def __init__(self):
        self.extractor = DocumentExtractor()

    def run_demo(self):
        print("Receipt Expense Categorization Demo")
        print("=" * 40)

        sample_documents = self._get_sample_documents()

        if not sample_documents:
            return

        for doc_name, (doc_text, doc_type) in sample_documents.items():
            print(f"\nProcessing: {doc_name}")
            result = self.extractor.extract_document(doc_text, doc_type)
            self._display_result(doc_name, result)

    def _get_sample_documents(self) -> Dict[str, tuple[str, str]]:
        try:
            with open("material/week_1/tuesday/session_2/sample_receipt.txt", "r") as f:
                receipt_text = f.read().strip()
            return {
                "Sample Receipt": (receipt_text, "receipt"),
            }
        except FileNotFoundError:
            print("Error: sample_receipt.txt not found. Please ensure the file exists.")
            return {}

    def _display_result(self, doc_name: str, result: ExtractionResult):
        if result.was_successful():
            print(f"{doc_name}: SUCCESS - Confidence: {result.confidence_score:.2f}")
            doc = result.document
            if hasattr(doc, "total_amount"):
                print(f"Total: {doc.currency} {doc.total_amount}")
            if hasattr(doc, "line_items") and doc.line_items:
                print(f"Items: {len(doc.line_items)}")

            # Display expense categories
            if hasattr(doc, "expense_categories") and doc.expense_categories:
                print(f"Expense Categories ({len(doc.expense_categories)}):")
                for category in doc.expense_categories:
                    print(
                        f"  • {category.category}: {doc.currency} {category.total_amount} ({category.item_count} items)"
                    )
                    for item in category.items:
                        print(f"    - {item}")
        else:
            print(f"{doc_name}: FAILED - {result.error_message}")

    def interactive_mode(self):
        print("\nInteractive Mode - Receipt Processing")
        print("Enter receipt text (type 'END' to finish):")
        doc_type = "receipt"

        lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)

        if not lines:
            return

        text = "\n".join(lines)
        result = self.extractor.extract_document(text, doc_type)

        self._display_result("Custom", result)

        if result.was_successful():
            show_json = input("\nShow JSON? (y/n): ").strip().lower()
            if show_json == "y":
                print(json.dumps(result.document.model_dump(), indent=2, default=str))


def main():
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: Set OPENAI_API_KEY environment variable")
        return

    demo = ReceiptProcessingDemo()

    while True:
        print("\nReceipt Expense Categorization Demo")
        print("1. Sample receipt")
        print("2. Interactive mode (enter your own receipt)")
        print("3. Exit")

        choice = input("\nChoose (1-3): ").strip()

        try:
            if choice == "1":
                demo.run_demo()
            elif choice == "2":
                demo.interactive_mode()
            elif choice == "3":
                break
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
