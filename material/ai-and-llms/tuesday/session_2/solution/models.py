"""
Data Models for Document Extraction
Week 1 - Tuesday - Session 2 Lab

Define your Pydantic models here for structured data extraction
"""

from typing import List, Optional, Literal
from pydantic import BaseModel, Field, field_validator
from datetime import date
from decimal import Decimal


class ExpenseCategory(BaseModel):
    """Categorized expense information"""

    category: str = Field(description="Category name for business expense reporting")
    total_amount: Decimal = Field(ge=0, description="Total amount for this category")
    item_count: int = Field(ge=1, description="Number of items in this category")
    items: List[str] = Field(description="List of item descriptions in this category")


class LineItem(BaseModel):
    """Individual line item on receipt"""

    description: str
    quantity: int = Field(ge=1, description="Quantity must be positive")
    unit_price: Decimal = Field(ge=0, description="Price must be non-negative")
    total_price: Decimal = Field(ge=0, description="Total must be non-negative")

    @field_validator("total_price")
    def validate_total(cls, v, info):
        data = info.data if hasattr(info, "data") else {}
        if "quantity" in data and "unit_price" in data:
            expected = data["quantity"] * data["unit_price"]
            if abs(v - expected) > Decimal("0.01"):
                raise ValueError(f"Total price {v} doesn't match quantity × unit_price")
        return v


class Receipt(BaseModel):
    """Receipt document structure"""

    document_type: Literal["receipt"] = "receipt"
    receipt_number: Optional[str] = None
    transaction_date: date
    transaction_time: Optional[str] = None

    # Merchant info
    merchant_name: str
    merchant_location: Optional[str] = None

    # Items and payment
    line_items: List[LineItem]
    subtotal: Decimal = Field(ge=0)
    tax_rate: Optional[float] = None
    tax_amount: Decimal = Field(ge=0)
    total_amount: Decimal = Field(ge=0)
    currency: str = Field(default="USD")

    # Payment details
    payment_method: Optional[Literal["cash", "card", "digital", "other"]] = None
    card_last_four: Optional[str] = Field(
        pattern=r"^\d{4}$", description="Last 4 digits of card"
    )

    # Expense categorization
    expense_categories: List[ExpenseCategory] = Field(
        default_factory=list,
        description="Purchases grouped by category (Food, Beverages, Office Supplies, etc.)",
    )

    extraction_confidence: float = Field(ge=0.0, le=1.0, default=0.0)

    @field_validator("total_amount")
    def validate_total_amount(cls, v, info):
        data = info.data if hasattr(info, "data") else {}
        if "subtotal" in data and "tax_amount" in data:
            expected = data["subtotal"] + data["tax_amount"]
            if abs(v - expected) > Decimal("0.01"):
                raise ValueError(f"Total {v} doesn't match subtotal + tax")
        return v


class ExtractionResult(BaseModel):
    """Wrapper for extraction results with metadata"""

    success: bool
    document: Optional[Receipt] = None
    error_message: Optional[str] = None
    processing_time: Optional[float] = None
    tokens_used: Optional[int] = None

    # Quality indicators
    confidence_score: float = Field(ge=0.0, le=1.0, default=0.0)
    fields_extracted: int = Field(ge=0, default=0)
    validation_errors: List[str] = Field(default_factory=list)

    def was_successful(self) -> bool:
        return self.success and self.document is not None


# Helper type for document type
DocumentType = Receipt
