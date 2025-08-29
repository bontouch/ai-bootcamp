from pydantic import BaseModel, Field
from typing import Union, Literal


class Number(BaseModel):
    type: Literal["number"]
    value: float


class BinaryOperation(BaseModel):
    type: Literal["binary_op"]
    op: Literal["+", "-", "*", "/"]
    left: "Expression"
    right: "Expression"


Expression = Union[Number, BinaryOperation]

BinaryOperation.model_rebuild()


class PaymentRequest(BaseModel):
    """Structured output for payment information extracted from multimodal input."""

    phone_number: str = Field(
        description="The phone number the user wants to send money to"
    )
    expression: Expression = Field(
        description="An arithmetic expression representing the amount to send"
    )
    message: str = Field(description="A fitting message to be sent with the payment")


class ProcessedPayment(BaseModel):
    """Final payment information with evaluated amount."""

    phone_number: str
    amount: float
    message: str


def evaluate_expression(expr: Expression) -> float:
    """
    Recursively evaluate arithmetic expressions.

    Args:
        expr: Expression object (Number or BinaryOperation)

    Returns:
        Evaluated numerical result
    """
    if expr.type == "number":
        return expr.value
    elif expr.type == "binary_op":
        left = evaluate_expression(expr.left)
        right = evaluate_expression(expr.right)
        match expr.op:
            case "+":
                return left + right
            case "-":
                return left - right
            case "*":
                return left * right
            case "/":
                return left / right
    raise ValueError(f"Unknown expression type: {expr.type}")
