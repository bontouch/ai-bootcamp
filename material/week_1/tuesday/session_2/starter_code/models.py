"""
Data Models for Receipt Processing
Week 1 - Tuesday - Session 2 Lab

TODO: Define your Pydantic models here
"""

from typing import List, Optional, Literal
from pydantic import BaseModel, Field, field_validator
from datetime import date
from decimal import Decimal


class ExpenseCategory(BaseModel):
    """Categorized expense information"""

    # TODO: Define fields for category name, total amount, item count, and item list
    pass


class LineItem(BaseModel):
    """Individual line item on receipt"""

    # TODO: Define fields for description, quantity, unit_price, total_price
    # TODO: Add validator to ensure quantity × unit_price = total_price
    pass


class Receipt(BaseModel):
    """Receipt document structure"""

    # TODO: Define all receipt fields including:
    # - Basic info (date, merchant, etc.)
    # - Financial details (subtotal, tax, total)
    # - Line items
    # - Expense categories
    # TODO: Add validator to ensure subtotal + tax = total_amount
    pass


class ExtractionResult(BaseModel):
    """Wrapper for extraction results with metadata"""

    # TODO: Define fields for success status, document, error handling
    pass
