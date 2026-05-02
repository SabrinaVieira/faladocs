"""Módulo de configuração para carregar variáveis de ambiente."""

import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# --- INÍCIO DO BLOCO DE DEBUG ---
print("--- [DEBUG] Iniciando o carregamento do módulo config.py ---")

# 1. Constrói o caminho absoluto para o arquivo .env na raiz do projeto.
project_root = Path(__file__).parent.parent.parent
dotenv_path = project_root / ".env"
print(f"--- [DEBUG] Caminho do arquivo .env: {dotenv_path}")
print(f"--- [DEBUG] O arquivo .env existe? {dotenv_path.exists()}")

# 2. Força o carregamento das variáveis do .env para o ambiente do sistema (os.environ).
#    Isso acontece ANTES da classe AppSettings ser definida, eliminando a condição de corrida.
was_loaded = load_dotenv(dotenv_path=dotenv_path, override=True)
print(f"--- [DEBUG] O arquivo .env foi carregado por dotenv? {was_loaded}")

# 3. Imprime as variáveis de ambiente relevantes para verificação.
print(f"--- [DEBUG] Valor de GOOGLE_API_KEY em os.environ: {os.getenv('GOOGLE_API_KEY')}")
print(f"--- [DEBUG] Valor de SUPABASE_URL em os.environ: {os.getenv('SUPABASE_URL')}")
print(f"--- [DEBUG] Valor de SUPABASE_KEY em os.environ: {os.getenv('SUPABASE_KEY')}")
# --- FIM DO BLOCO DE DEBUG ---


class AppSettings(BaseSettings):
    """
    Define e valida as variáveis de ambiente da aplicação, lendo-as
    diretamente do ambiente do processo, que já foi populado pelo `load_dotenv`.
    """
    GOOGLE_API_KEY: str
    SUPABASE_URL: str
    SUPABASE_KEY: str


# @lru_cache  # <-- REMOVIDO TEMPORARIAMENTE PARA DEBUG
def get_settings() -> AppSettings:
    """Retorna uma instância das configurações da aplicação."""
    print("--- [DEBUG] Função get_settings() foi chamada. Criando nova instância de AppSettings. ---")
    try:
        settings = AppSettings()
        print("--- [DEBUG] Instância de AppSettings criada com sucesso. ---")
        return settings
    except Exception as e:
        print(f"--- [DEBUG] ERRO ao criar instância de AppSettings: {e}")
        raise