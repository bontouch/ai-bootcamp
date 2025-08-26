"""
Receipt Extractor with OpenAI Integration
Week 1 - Tuesday - Session 2 Lab

TODO: Implement the receipt extraction logic with few-shot prompting
"""

import time
from typing import Optional
from openai import OpenAI
# TODO: Import your models here


class ReceiptExtractor:
    def __init__(self, openai_api_key: Optional[str] = None):
        # TODO: Initialize OpenAI client
        # TODO: Set model to "gpt-4.1"
        pass

    def extract_receipt(self, receipt_text: str):
        # TODO: Implement receipt extraction using:
        # 1. Input validation
        # 2. Few-shot prompting with examples
        # 3. OpenAI structured outputs (client.beta.chat.completions.parse)
        # 4. Error handling
        pass

    def _get_receipt_prompt(self) -> str:
        # TODO: Create few-shot prompt with examples showing how to categorize items into:
        # - Food & Beverage
        # - Health & Wellness
        # - Household & Utilities
        # - Leisure & Entertainment
        #
        # Include concrete examples like:
        # "Energy Drinks" → Food & Beverage
        # "Essential Oils" → Health & Wellness
        # "Hand Sanitizer" → Household & Utilities
        # "Board Games" → Leisure & Entertainment
        pass
