import time
from datetime import datetime
from fastapi import APIRouter
from ..models.responses import HealthCheck
from ....core.config import settings

router = APIRouter()

# Record application start time (module level)
app_start_time = time.time()


@router.get("/health", response_model=HealthCheck, tags=["health"])
async def health_check() -> HealthCheck:
    """Check application health and status."""
    current_time = time.time()
    uptime = current_time - app_start_time

    return HealthCheck(
        status="healthy",
        timestamp=datetime.now(),
        version=settings.app_version,
        uptime_seconds=uptime,
    )
