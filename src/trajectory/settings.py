"""trajectory Settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for trajectory."""

    model_config = SettingsConfigDict(
        env_prefix="TRAJECTORY",
        env_file=".env-trajectory",
    )
    debug: bool = False
