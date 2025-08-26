from typing import Optional
from openai import OpenAI
from models import DocumentType, Receipt, ExtractionResult


"""
DocumentExtractor - Core class for structured document processing using OpenAI API
Handles receipt extraction with validation, error handling, and expense categorization
"""


class DocumentExtractor:
    def __init__(self, openai_api_key: Optional[str] = None):
        self.client = OpenAI(api_key=openai_api_key)
        self.model = "gpt-4.1"

    def extract_document(self, text: str) -> ExtractionResult:
        try:
            if not self._is_valid_input(text):
                return ExtractionResult(
                    success=False,
                    error_message="Input failed validation",
                )

            system_prompt = self._get_receipt_prompt()
            response = self.client.responses.parse(
                model=self.model,
                input=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": text},
                ],
                text_format=Receipt,
                temperature=0,
            )

            document = response.output_parsed

            return ExtractionResult(
                success=True,
                document=document,
                tokens_used=response.usage.total_tokens if response.usage else None,
                confidence_score=getattr(document, "extraction_confidence", 0.0),
                fields_extracted=self._count_extracted_fields(document),
            )

        except Exception as e:
            return ExtractionResult(
                success=False,
                error_message=str(e),
            )

    def _is_valid_input(self, text: str) -> bool:
        if not text or len(text.strip()) < 10:
            return False
        suspicious = ["hack", "password", "login", "admin", "root"]
        return not any(word in text.lower() for word in suspicious)

    def _get_receipt_prompt(self) -> str:
        return """Extract receipt information including items, payment details, merchant info.

IMPORTANT: Categorize all purchases into these specific expense categories:
- Food & Beverage
- Health & Wellness
- Household & Utilities
- Leisure & Entertainment
"""

    def _count_extracted_fields(self, document: DocumentType) -> int:
        return sum(1 for v in document.model_dump().values() if v is not None)
