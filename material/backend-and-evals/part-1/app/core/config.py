from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings and configuration."""

    app_name: str = "FastAPI User Management"
    app_version: str = "1.0.0"
    debug: bool = True
    host: str = "localhost"
    port: int = 8000

    # API Configuration
    api_v1_prefix: str = "/api/v1"

    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()
