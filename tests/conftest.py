"""
Arquivo de configuração global para a suíte de testes do Pytest.
"""
import pytest
from unittest.mock import MagicMock


@pytest.fixture(autouse=True)
def override_get_settings(mocker):
    """
    Sobrescreve (patches) a função `get_settings` para toda a sessão de testes.

    Esta abordagem é mais direta e robusta contra problemas de timing de importação
    e cache do que usar monkeypatch. Ela garante que qualquer chamada a
    `config.get_settings()` retorne um objeto de configuração mockado e funcional,
    isolando completamente os testes do mecanismo de carregamento de variáveis.
    """
    # 1. Cria um objeto de mock que se parece com o objeto AppSettings real.
    mock_settings = MagicMock()
    mock_settings.google_api_key = "fake-api-key"
    mock_settings.supabase_url = "http://fake-url.com"
    mock_settings.supabase_key = "fake-key"

    # 2. Faz o patch da função no local onde ela é DEFINIDA.
    mock_get_settings = mocker.patch("src.core.config.get_settings")

    # 3. Configura o mock para retornar nosso objeto falso.
    mock_get_settings.return_value = mock_settings