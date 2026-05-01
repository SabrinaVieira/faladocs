"""Módulo de configuração para carregar variáveis de ambiente."""

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """
    Define e valida as variáveis de ambiente da aplicação.
    Carrega as variáveis de um arquivo .env.
    """

    GOOGLE_API_KEY: str
    SUPABASE_URL: str
    SUPABASE_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


@lru_cache
def get_settings() -> AppSettings:
    """Retorna uma instância cacheada das configurações da aplicação."""
    return AppSettings()