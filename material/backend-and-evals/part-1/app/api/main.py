from fastapi import FastAPI
from .api_v1.endpoints import users, health
from ..core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="A comprehensive user management API built with FastAPI",
    version=settings.app_version,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.include_router(health.router)
app.include_router(users.router, prefix=settings.api_v1_prefix, tags=["users"])


@app.get("/", tags=["root"])
async def root() -> dict:
    """Root endpoint with basic application information."""
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": settings.app_version,
        "docs_url": "/docs",
        "health_check": "/health",
    }
