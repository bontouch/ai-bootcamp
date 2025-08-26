import os
import json
from typing import Dict
from dotenv import load_dotenv
from extractor import DocumentExtractor
from models import ExtractionResult

load_dotenv()


"""
Receipt Processing Demo - CLI interface for structured receipt extraction
Demonstrates OpenAI API structured outputs with Pydantic validation
Supports sample data processing and interactive receipt entry
"""


class ReceiptProcessingDemo:
    def __init__(self):
        self.extractor = DocumentExtractor()

    def run_demo(self):
        sample_documents = self._get_sample_documents()
        if not sample_documents:
            return

        for doc_name, doc_text in sample_documents.items():
            result = self.extractor.extract_document(doc_text)
            self._display_result(doc_name, result)

    def _get_sample_documents(self) -> Dict[str, str]:
        file_path = "../sample_receipt.txt"
        try:
            with open(file_path, "r") as f:
                receipt_text = f.read().strip()
            return {"Sample Receipt": receipt_text}
        except FileNotFoundError:
            print(f"Error: {file_path} not found")
            return {}

    def _display_result(self, doc_name: str, result: ExtractionResult):
        if result.was_successful():
            doc = result.document
            print(f"{doc_name}: SUCCESS")
            print(f"Total: {doc.currency} {doc.total_amount}")
            print(f"Items: {len(doc.line_items)}")

            if doc.expense_categories:
                print(f"Categories ({len(doc.expense_categories)}):")
                for category in doc.expense_categories:
                    print(
                        f"  • {category.category}: {doc.currency} {category.total_amount}"
                    )
                    for item in category.items:
                        print(f"    - {item}")
        else:
            print(f"{doc_name}: FAILED - {result.error_message}")

    def interactive_mode(self):
        print("Enter receipt text (type 'END' to finish):")

        lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)

        if not lines:
            return

        text = "\n".join(lines)
        result = self.extractor.extract_document(text)
        self._display_result("Custom", result)

        if result.was_successful():
            show_json = input("Show JSON? (y/n): ").strip().lower()
            if show_json == "y":
                print(json.dumps(result.document.model_dump(), indent=2, default=str))


def main():
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: Set OPENAI_API_KEY environment variable")
        return

    demo = ReceiptProcessingDemo()

    while True:
        print("\n1. Sample receipt")
        print("2. Interactive mode")
        print("3. Exit")

        choice = input("Choose (1-3): ").strip()

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
