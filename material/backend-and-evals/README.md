# Backend & Evals Workshop

## Overview
This 3-part progressive workshop teaches modern FastAPI backend development with AI integration, designed for digital product agency engineers transitioning to AI roles.

## Learning Objectives
- Master FastAPI development patterns and async programming
- Understand dependency injection and service layer architecture  
- Implement repository pattern with SQLAlchemy and database migrations
- Integrate OpenAI APIs into production backend systems
- Build scalable, maintainable backend architectures

## Workshop Structure

### Part 1: Basic FastAPI Foundation (45-60 minutes)
**Focus**: Core FastAPI concepts with working endpoints

**Key Concepts**:
- FastAPI application setup and configuration
- Pydantic models for request/response validation
- RESTful API design patterns
- Async/await programming model
- Automatic OpenAPI documentation

**What You'll Build**: A user management API with complete CRUD operations, health checks, and proper error handling.

### Part 2: AI Service Integration (60-75 minutes)  
**Focus**: FastAPI dependency injection with AI service layer

**Key Concepts**:
- Dependency injection patterns in FastAPI
- Service layer architecture
- OpenAI API integration
- External configuration management
- Error handling for external APIs
- Response caching strategies

**What You'll Build**: A text analysis API that performs sentiment analysis using OpenAI, demonstrating clean separation of concerns and proper dependency management.

### Part 3: Full Architecture with Repository Pattern (75-90 minutes)
**Focus**: Complete database integration with repository pattern

**Key Concepts**:
- Repository pattern implementation
- SQLAlchemy 2.0 with async operations
- Database migrations with Alembic
- Data persistence strategies
- Database dependency injection
- Seed data management

**What You'll Build**: A complete AI analysis platform with database persistence, allowing users to store and retrieve analysis history with full CRUD operations.

## Technical Requirements

### Dependencies
```toml
fastapi = "^0.104.0"      # Modern web framework
uvicorn = "^0.24.0"       # ASGI server
sqlalchemy = "^2.0.0"     # ORM with async support
alembic = "^1.12.0"       # Database migrations
python-multipart = "^0.0.6" # Form data support
aiosqlite = "^0.19.0"     # Async SQLite driver
openai = "^1.100.1"       # OpenAI API client
pydantic = "^2.11.7"      # Data validation
python-dotenv = "^1.1.1"  # Environment management
```

### Environment Setup
```bash
# Install dependencies
uv sync

# Set up environment variables
export OPENAI_API_KEY="your-api-key-here"

# Run any part
cd material/backend-and-evals/part-1
python run.py
```

## Progressive Architecture

### Part 1 Architecture
```
app/
├── api/
│   ├── main.py              # FastAPI application
│   └── api_v1/
│       ├── endpoints/
│       │   └── users.py     # User management endpoints
│       └── models/
│           └── responses.py # Pydantic response models
└── core/
    └── config.py            # Application settings
```

### Part 2 Architecture (extends Part 1)
```
app/
├── ai/
│   ├── models/
│   │   └── requests.py      # AI request/response models
│   └── service/
│       └── analyzer.py      # AI business logic service
├── api/
│   ├── deps.py              # Dependency injection
│   ├── main.py
│   └── api_v1/
│       └── endpoints/
│           ├── users.py     # (from Part 1)
│           └── analyze.py   # AI analysis endpoints
└── core/
    └── config.py            # Extended configuration
```

### Part 3 Architecture (extends Part 2)  
```
app/
├── ai/ (from Part 2)
├── api/
│   ├── deps.py              # Database dependencies added
│   ├── main.py
│   └── api_v1/
│       └── endpoints/
│           ├── users.py     # (from Part 1)
│           ├── analyze.py   # Enhanced with persistence
│           └── history.py   # Analysis history endpoints
├── core/
│   ├── config.py            # Database configuration added
│   └── database.py          # SQLAlchemy setup
└── db/
    ├── repository/
    │   └── analysis.py      # Repository pattern
    └── schemas/
        └── analysis.py      # SQLAlchemy models
```

## Key Patterns Demonstrated

### 1. Dependency Injection
FastAPI's powerful dependency system for clean, testable code:
```python
async def get_ai_service() -> AIAnalyzer:
    return AIAnalyzer()

@router.post("/analyze")
async def analyze_text(
    request: AnalysisRequest,
    ai_service: AIAnalyzer = Depends(get_ai_service)
):
    return await ai_service.analyze(request.text)
```

### 2. Service Layer Pattern
Separating business logic from API concerns:
```python
class AIAnalyzer:
    async def analyze(self, text: str) -> AnalysisResult:
        # Business logic here
        pass
```

### 3. Repository Pattern
Abstracting data access for maintainability:
```python
class AnalysisRepository:
    async def create(self, analysis: Analysis) -> Analysis:
        # Database operations here
        pass
```

## Best Practices Highlighted
- **Type Safety**: Comprehensive type hints throughout
- **Async Operations**: Proper async/await usage for I/O operations
- **Error Handling**: Structured error responses and logging
- **Configuration**: Environment-based settings management
- **Documentation**: Automatic OpenAPI schema generation
- **Testing**: Dependency injection enables easy testing
- **Security**: Input validation and sanitization

## Common Pitfalls Addressed
- Blocking I/O operations in async contexts
- Missing type hints affecting IDE support
- Poor error handling leading to unclear failures
- Tight coupling between layers
- Missing input validation
- Hardcoded configuration values

## Workshop Flow
1. **Part 1**: Build foundation understanding with working API
2. **Part 2**: Add complexity with external service integration  
3. **Part 3**: Complete the architecture with data persistence

Each part builds upon the previous, demonstrating how to evolve a simple API into a production-ready application with proper architectural patterns.