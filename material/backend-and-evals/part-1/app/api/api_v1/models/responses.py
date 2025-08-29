from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    """Base user model with common fields."""
    name: str = Field(..., min_length=1, max_length=100, description="User's full name")
    email: EmailStr = Field(..., description="User's email address")
    age: Optional[int] = Field(None, ge=0, le=150, description="User's age")


class UserCreate(UserBase):
    """Model for creating a new user."""
    pass


class UserUpdate(BaseModel):
    """Model for updating an existing user."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, ge=0, le=150)


class User(UserBase):
    """Complete user model with ID and timestamps."""
    id: int = Field(..., description="Unique user identifier")
    created_at: datetime = Field(..., description="User creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")

    class Config:
        from_attributes = True


class UserList(BaseModel):
    """Response model for user list with pagination info."""
    users: List[User] = Field(..., description="List of users")
    total: int = Field(..., description="Total number of users")
    page: int = Field(..., description="Current page number")
    size: int = Field(..., description="Number of users per page")
    has_next: bool = Field(..., description="Whether there are more pages")


class HealthCheck(BaseModel):
    """Health check response model."""
    status: str = Field(..., description="Application status")
    timestamp: datetime = Field(..., description="Check timestamp")
    version: str = Field(..., description="Application version")
    uptime_seconds: float = Field(..., description="Application uptime in seconds")


class ErrorResponse(BaseModel):
    """Standard error response model."""
    error: str = Field(..., description="Error type")
    message: str = Field(..., description="Error message")
    details: Optional[dict] = Field(None, description="Additional error details")