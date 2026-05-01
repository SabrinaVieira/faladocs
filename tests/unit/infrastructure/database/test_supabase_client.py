import logging
from unittest.mock import MagicMock, patch

import pytest

from src.core.exceptions import SupabaseConnectionError
from src.infrastructure.database.supabase_client import (
    get_supabase_client,
)


def test_get_supabase_client_Given_valid_credentials_When_called_Then_returns_client(
    monkeypatch,
):
    """
    Given: As variáveis de ambiente SUPABASE_URL e SUPABASE_KEY estão definidas.
    When: A função get_supabase_client é chamada.
    Then: Ela deve chamar supabase.create_client com as credenciais corretas e retornar o cliente.
    """
    # Arrange
    monkeypatch.setenv("SUPABASE_URL", "http://fake-url.com")
    monkeypatch.setenv("SUPABASE_KEY", "fake-key")
    mock_client = MagicMock()

    with patch(
        "src.infrastructure.database.supabase_client.create_client",
        return_value=mock_client,
    ) as mock_create_client:
        # Act
        client = get_supabase_client()

        # Assert
        mock_create_client.assert_called_once_with(
            "http://fake-url.com", "fake-key"
        )
        assert client == mock_client


@pytest.mark.parametrize(
    "missing_env_var", ["SUPABASE_URL", "SUPABASE_KEY"]
)
def test_get_supabase_client_Given_missing_credentials_When_called_Then_raises_error(
    monkeypatch, missing_env_var
):
    """
    Given: Uma das variáveis de ambiente (SUPABASE_URL ou SUPABASE_KEY) não está definida.
    When: A função get_supabase_client é chamada.
    Then: Ela deve levantar uma SupabaseConnectionError.
    """
    # Arrange
    monkeypatch.setenv("SUPABASE_URL", "http://fake-url.com")
    monkeypatch.setenv("SUPABASE_KEY", "fake-key")
    monkeypatch.delenv(missing_env_var)

    # Act & Assert
    with pytest.raises(SupabaseConnectionError) as exc_info:
        get_supabase_client()

    assert f"A variável de ambiente {missing_env_var} não foi definida." in str(
        exc_info.value
    )


def test_get_supabase_client_Given_connection_fails_When_called_Then_logs_and_raises_error(
    monkeypatch, caplog
):
    """
    Given: As credenciais estão definidas, mas a criação do cliente falha.
    When: A função get_supabase_client é chamada.
    Then: Ela deve logar o erro e levantar uma SupabaseConnectionError.
    """
    # Arrange
    monkeypatch.setenv("SUPABASE_URL", "http://fake-url.com")
    monkeypatch.setenv("SUPABASE_KEY", "fake-key")
    caplog.set_level(logging.ERROR)

    with patch(
        "src.infrastructure.database.supabase_client.create_client",
        side_effect=Exception("Connection timed out"),
    ):
        # Act & Assert
        with pytest.raises(SupabaseConnectionError):
            get_supabase_client()

        assert "Falha ao conectar com o Supabase" in caplog.text