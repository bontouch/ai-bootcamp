from typing import Optional
from openai import OpenAI
# TODO: Import your models here:
# from models import DocumentType, Receipt, ExtractionResult


"""
DocumentExtractor - Core class for structured document processing using OpenAI API
Handles receipt extraction with validation, error handling, and expense categorization

TODO: Implement the receipt extraction logic with structured outputs
"""


class DocumentExtractor:
    def __init__(self, openai_api_key: Optional[str] = None):
        # TODO: Initialize OpenAI client and set model
        self.client = OpenAI(api_key=openai_api_key)
        self.model = "gpt-4.1"

    def extract_document(self, text: str):
        # TODO: Implement document extraction following this pattern:

        # Step 1: Validate input using _is_valid_input()
        # if not self._is_valid_input(text):
        #     return ExtractionResult(success=False, error_message="Input failed validation")

        # Step 2: Get system prompt for receipt extraction
        # system_prompt = self._get_receipt_prompt()

        # Step 3: Make OpenAI API call using structured outputs
        # response = self.client.responses.parse(
        #     model=self.model,
        #     input=[
        #         {"role": "system", "content": system_prompt},
        #         {"role": "user", "content": text}
        #     ],
        #     text_format=Receipt,  # Direct use of Receipt class
        #     temperature=0
        # )

        # Step 4: Extract parsed document and create successful result
        # document = response.output_parsed
        # return ExtractionResult(
        #     success=True,
        #     document=document,
        #     tokens_used=response.usage.total_tokens if response.usage else None,
        #     confidence_score=getattr(document, "extraction_confidence", 0.0),
        #     fields_extracted=self._count_extracted_fields(document)
        # )

        # Step 5: Handle exceptions with try/except
        # except Exception as e:
        #     return ExtractionResult(
        #         success=False,
        #         error_message=str(e)
        #     )
        pass

    def _is_valid_input(self, text: str) -> bool:
        # TODO: Implement input validation:
        # - Check if text exists and length > 10
        # - Check for suspicious words like ["hack", "password", "login", "admin", "root"]
        # - Return False if text is too short or contains suspicious content
        pass

    def _get_receipt_prompt(self) -> str:
        # TODO: Write a system prompt for receipt extraction
        pass

    def _count_extracted_fields(self, document) -> int:
        # TODO: Count non-null fields in the document:
        # - Use document.model_dump() to get all fields as dict
        # - Count values that are not None
        # - Return the count
        pass
