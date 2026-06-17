from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf-8")
    database_url: str = "postgresql://devlucas:teste123@localhost:5432/api_bancaria"
    environment: str = "production"

settings = Settings()    