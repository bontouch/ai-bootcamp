import time
from typing import Optional, Type
from openai import OpenAI
from models import DocumentType, Receipt, ExtractionResult


class DocumentExtractor:
    def __init__(self, openai_api_key: Optional[str] = None):
        self.client = OpenAI(api_key=openai_api_key)
        self.model = "gpt-4.1"

    def extract_document(self, text: str, document_type: str) -> ExtractionResult:
        start_time = time.time()

        try:
            if not self._is_valid_input(text):
                return ExtractionResult(
                    success=False,
                    error_message="Input failed validation",
                    processing_time=time.time() - start_time,
                )

            model_class = self._get_model_class(document_type)
            if not model_class:
                return ExtractionResult(
                    success=False,
                    error_message=f"Unsupported document type: {document_type}",
                    processing_time=time.time() - start_time,
                )

            system_prompt = self._get_system_prompt(document_type)
            response = self.client.beta.chat.completions.parse(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": text},
                ],
                response_format=model_class,
                temperature=0,
            )

            document = response.choices[0].message.parsed
            processing_time = time.time() - start_time

            return ExtractionResult(
                success=True,
                document=document,
                processing_time=processing_time,
                tokens_used=response.usage.total_tokens if response.usage else None,
                confidence_score=getattr(document, "extraction_confidence", 0.0),
                fields_extracted=self._count_extracted_fields(document),
            )

        except Exception as e:
            return ExtractionResult(
                success=False,
                error_message=str(e),
                processing_time=time.time() - start_time,
            )

    def _is_valid_input(self, text: str) -> bool:
        if not text or len(text.strip()) < 10:
            return False
        suspicious = ["hack", "password", "login", "admin", "root"]
        return not any(word in text.lower() for word in suspicious)

    def _get_model_class(self, document_type: str) -> Optional[Type[DocumentType]]:
        if document_type.lower() == "receipt":
            return Receipt
        return None

    def _get_system_prompt(self, document_type: str) -> str:
        prompts = {
            "receipt": self._get_receipt_prompt(),
        }
        return prompts.get(document_type.lower(), "Extract document information.")

    def _get_receipt_prompt(self) -> str:
        return """Extract receipt information including items, payment details,
        merchant info.

IMPORTANT: Categorize all purchases into these specific expense categories:
- Food & Beverage
- Health & Wellness
- Household & Utilities
- Leisure & Entertainment
"""

    def _count_extracted_fields(self, document: DocumentType) -> int:
        return sum(1 for v in document.model_dump().values() if v is not None)
