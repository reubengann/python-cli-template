from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    setting1: Optional[str]
    setting2: Optional[str]

    class Config:
        env_file = ".env"


settings = Settings.parse_obj({})
