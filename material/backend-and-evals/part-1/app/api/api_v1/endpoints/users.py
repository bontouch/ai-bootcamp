from datetime import datetime
from typing import Dict
from fastapi import APIRouter, HTTPException, Query
from ..models.responses import User, UserCreate, UserUpdate, UserList

router = APIRouter()

# In-memory storage for demonstration
users_db: Dict[int, User] = {}
next_user_id: int = 1


def get_next_id() -> int:
    """Get the next available user ID."""
    global next_user_id
    current_id = next_user_id
    next_user_id += 1
    return current_id


@router.post("/users", response_model=User, status_code=201)
async def create_user(user_data: UserCreate) -> User:
    """Create a new user."""
    user_id = get_next_id()
    now = datetime.now()

    new_user = User(
        id=user_id,
        name=user_data.name,
        email=user_data.email,
        age=user_data.age,
        created_at=now,
        updated_at=now,
    )

    # Check for duplicate email
    for existing_user in users_db.values():
        if existing_user.email == user_data.email:
            raise HTTPException(
                status_code=400,
                detail=f"User with email {user_data.email} already exists",
            )

    users_db[user_id] = new_user
    return new_user


@router.get("/users", response_model=UserList)
async def list_users(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(10, ge=1, le=100, description="Page size"),
) -> UserList:
    """List all users with pagination."""
    all_users = list(users_db.values())
    total = len(all_users)

    # Calculate pagination
    start = (page - 1) * size
    end = start + size
    users_page = all_users[start:end]

    has_next = end < total

    return UserList(
        users=users_page, total=total, page=page, size=size, has_next=has_next
    )


@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int) -> User:
    """Get a specific user by ID."""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")

    return users_db[user_id]


@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user_update: UserUpdate) -> User:
    """Update an existing user."""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")

    existing_user = users_db[user_id]

    # Check for email conflicts (if email is being updated)
    if user_update.email and user_update.email != existing_user.email:
        for uid, user in users_db.items():
            if uid != user_id and user.email == user_update.email:
                raise HTTPException(
                    status_code=400,
                    detail=f"User with email {user_update.email} already exists",
                )

    # Update fields that were provided
    update_data = user_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(existing_user, field, value)

    existing_user.updated_at = datetime.now()
    users_db[user_id] = existing_user

    return existing_user


@router.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: int) -> None:
    """Delete a user."""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")

    del users_db[user_id]


@router.get("/users/{user_id}/exists")
async def user_exists(user_id: int) -> dict:
    """Check if a user exists."""
    exists = user_id in users_db
    return {"user_id": user_id, "exists": exists}
