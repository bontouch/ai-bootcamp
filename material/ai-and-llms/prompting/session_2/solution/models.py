from typing import List, Optional, Literal
from pydantic import BaseModel, Field, field_validator
from datetime import date
from decimal import Decimal


"""
Pydantic models for structured document extraction with validation
- ExpenseCategory: Groups receipt items by business expense category
- LineItem: Individual receipt line with quantity/price validation
- Receipt: Complete receipt structure with merchant, items, payment data
- ExtractionResult: API response wrapper with success/error metadata
"""


class ExpenseCategory(BaseModel):
    category: str
    total_amount: Decimal = Field(ge=0)
    item_count: int = Field(ge=1)
    items: List[str]


class LineItem(BaseModel):
    description: str
    quantity: int = Field(ge=1)
    unit_price: Decimal = Field(ge=0)
    total_price: Decimal = Field(ge=0)

    @field_validator("total_price")
    def validate_total(cls, v, info):
        data = info.data if hasattr(info, "data") else {}
        if "quantity" in data and "unit_price" in data:
            expected = data["quantity"] * data["unit_price"]
            if abs(v - expected) > Decimal("0.01"):
                raise ValueError(f"Total price {v} doesn't match quantity × unit_price")
        return v


class Receipt(BaseModel):
    receipt_number: Optional[str] = None
    transaction_date: date
    transaction_time: Optional[str] = None

    merchant_name: str
    merchant_location: Optional[str] = None

    line_items: List[LineItem]
    subtotal: Decimal = Field(ge=0)
    tax_rate: Optional[float] = None
    tax_amount: Decimal = Field(ge=0)
    total_amount: Decimal = Field(ge=0)
    currency: str = Field(default="USD")

    payment_method: Optional[Literal["cash", "card", "digital", "other"]] = None
    card_last_four: Optional[str] = Field(pattern=r"^\d{4}$")

    expense_categories: List[ExpenseCategory] = Field(default_factory=list)
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
    success: bool
    document: Optional[Receipt] = None
    error_message: Optional[str] = None
    tokens_used: Optional[int] = None
    confidence_score: float = Field(ge=0.0, le=1.0, default=0.0)
    fields_extracted: int = Field(ge=0, default=0)
    validation_errors: List[str] = Field(default_factory=list)

    def was_successful(self) -> bool:
        return self.success and self.document is not None


DocumentType = Receipt
