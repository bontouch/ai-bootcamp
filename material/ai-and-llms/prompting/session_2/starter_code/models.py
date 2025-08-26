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

TODO: Define your Pydantic models for structured OpenAI API responses
"""


class ExpenseCategory(BaseModel):
    # TODO: Add these fields:
    # category: str - name of expense category (Food & Beverage, Health & Wellness, etc.)
    # total_amount: Decimal - total cost for this category (Field with ge=0 constraint)
    # item_count: int - number of items in category (Field with ge=1 constraint)
    # items: List[str] - list of item descriptions in this category
    pass


class LineItem(BaseModel):
    # TODO: Add these fields:
    # description: str - item description from receipt
    # quantity: int - quantity purchased (Field with ge=1 constraint)
    # unit_price: Decimal - price per unit (Field with ge=0 constraint)
    # total_price: Decimal - total line price (Field with ge=0 constraint)

    # TODO: Add @field_validator("total_price") that checks:
    # - If quantity and unit_price are available, verify total_price = quantity × unit_price
    # - Use Decimal("0.01") tolerance for floating point comparison
    # - Raise ValueError if calculation doesn't match
    pass


class Receipt(BaseModel):
    # TODO: Add basic document fields:
    # receipt_number: Optional[str] = None
    # transaction_date: date (required)
    # transaction_time: Optional[str] = None

    # TODO: Add merchant information:
    # merchant_name: str (required)
    # merchant_location: Optional[str] = None

    # TODO: Add financial fields:
    # line_items: List[LineItem] (required list of items)
    # subtotal: Decimal (Field with ge=0 constraint)
    # tax_rate: Optional[float] = None
    # tax_amount: Decimal (Field with ge=0 constraint)
    # total_amount: Decimal (Field with ge=0 constraint)
    # currency: str = Field(default="USD")

    # TODO: Add payment details:
    # payment_method: Optional[Literal["cash", "card", "digital", "other"]] = None
    # card_last_four: Optional[str] = Field(pattern=r"^\d{4}$")

    # TODO: Add categorization:
    # expense_categories: List[ExpenseCategory] = Field(default_factory=list)
    # extraction_confidence: float = Field(ge=0.0, le=1.0, default=0.0)

    # TODO: Add @field_validator("total_amount") that checks:
    # - If subtotal and tax_amount exist, verify total_amount = subtotal + tax_amount
    # - Use Decimal("0.01") tolerance for comparison
    pass


class ExtractionResult(BaseModel):
    # TODO: Add result tracking fields:
    # success: bool - whether extraction succeeded
    # document: Optional[Receipt] = None - the extracted document if successful
    # error_message: Optional[str] = None - error description if failed
    # tokens_used: Optional[int] = None - OpenAI tokens consumed
    # confidence_score: float = Field(ge=0.0, le=1.0, default=0.0) - extraction confidence
    # fields_extracted: int = Field(ge=0, default=0) - count of non-null fields
    # validation_errors: List[str] = Field(default_factory=list) - any validation issues

    # TODO: Add helper method:
    # def was_successful(self) -> bool:
    #     return self.success and self.document is not None
    pass


# TODO: Create type alias for document types:
# DocumentType = Receipt
