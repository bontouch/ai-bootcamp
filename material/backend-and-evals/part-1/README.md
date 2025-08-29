# Part 1: Basic FastAPI Foundation

## Learning Objectives
- Understand FastAPI application structure and setup
- Master Pydantic models for request/response validation
- Leverage FastAPI's automatic OpenAPI documentation

## API Endpoints

### Health Check
- `GET /health` - Returns system status and uptime

### User Management
- `POST /api/v1/users` - Create a new user
- `GET /api/v1/users` - List all users (with pagination)
- `GET /api/v1/users/{user_id}` - Get specific user by ID
- `PUT /api/v1/users/{user_id}` - Update existing user
- `DELETE /api/v1/users/{user_id}` - Delete user

## Running the Application

```bash
# From the part-1 directory
cd material/backend-and-evals/part-1

# Install dependencies (if not already installed)
uv sync

# Run with uvicorn
uvicorn app.api.main:app --reload --host localhost --port 8000
```

The API will be available at:
- **API Base**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **OpenAPI Schema**: http://localhost:8000/openapi.json

## Example Usage
Take a look in the `test_api.ipynb` notebook to test the API.

## Architecture Highlights

### Project Structure
```
app/
├── api/
│   ├── main.py              # FastAPI application setup
│   └── api_v1/
│       ├── endpoints/
│       │   └── users.py     # User management endpoints
│       └── models/
│           └── responses.py # Pydantic response models
└── core/
    └── config.py            # Application configuration
```

### Key Concepts Demonstrated

**1. Pydantic Models**
- Type validation and serialization
- Automatic request/response documentation
- Built-in data validation with helpful error messages

**2. FastAPI Routers**
- Clean separation of endpoint logic
- Automatic route registration
- Consistent URL patterns
