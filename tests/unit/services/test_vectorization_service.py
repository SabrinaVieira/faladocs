"""
Testes unitários para o serviço de vetorização e armazenamento.
"""

import pytest
from unittest.mock import MagicMock, patch

from src.core.exceptions import EmbeddingError, VectorStorageError

# Módulo e função a serem testados
from src.services.vectorization_service import embed_and_store_chunks


@pytest.fixture
def mock_dependencies(mocker):
    """Fixture para mockar as dependências de infraestrutura e bibliotecas."""
    mock_get_supabase_client = mocker.patch(
        "src.services.vectorization_service.get_supabase_client"
    )
    mock_google_embeddings = mocker.patch(
        "src.services.vectorization_service.GoogleGenerativeAIEmbeddings"
    )
    mock_supabase_vector_store = mocker.patch(
        "src.services.vectorization_service.SupabaseVectorStore"
    )
    return {
        "get_supabase_client": mock_get_supabase_client,
        "google_embeddings": mock_google_embeddings,
        "supabase_vector_store": mock_supabase_vector_store,
    }


def test_embed_and_store_chunks_given_valid_chunks_when_called_then_succeeds(
    mock_dependencies,
):
    """
    Given: Uma lista de chunks de texto.
    When: A função embed_and_store_chunks é chamada.
    Then: Deve instanciar os embeddings, o cliente Supabase e chamar o
          método from_texts sem levantar exceções.
    """
    # Arrange
    chunks = ["primeiro chunk", "segundo chunk"]

    # Act
    embed_and_store_chunks(chunks)

    # Assert
    mock_dependencies["get_supabase_client"].assert_called_once()
    mock_dependencies["google_embeddings"].assert_called_once()
    mock_dependencies["supabase_vector_store"].from_texts.assert_called_once()


def test_embed_and_store_chunks_given_embedding_fails_when_called_then_raises_embedding_error(
    mock_dependencies,
):
    """
    Given: Uma falha na API de embeddings.
    When: A função embed_and_store_chunks é chamada.
    Then: Deve levantar a exceção customizada EmbeddingError.
    """
    # Arrange
    chunks = ["chunk que vai falhar"]
    mock_dependencies["supabase_vector_store"].from_texts.side_effect = Exception(
        "Google API Error"
    )

    # Act & Assert
    with pytest.raises(EmbeddingError, match="Falha ao gerar embeddings ou armazenar vetores."):
        embed_and_store_chunks(chunks)


# Nota: O teste para VectorStorageError é similar ao de EmbeddingError.
# A biblioteca LangChain usa `from_texts` para ambas as operações,
# tornando a distinção da causa raiz (embedding vs. storage) difícil
# sem inspecionar a exceção interna. Para este teste, focamos em
# garantir que *qualquer* falha no processo levante uma exceção esperada.