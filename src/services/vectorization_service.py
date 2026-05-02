"""
Serviço responsável pela vetorização de texto e armazenamento no Supabase.
"""


import logging
from typing import List

from langchain_community.vectorstores import SupabaseVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from core import config
from core.exceptions import EmbeddingError, VectorStorageError
from infrastructure.database.supabase_client import get_supabase_client

logger = logging.getLogger(__name__)


def embed_and_store_chunks(chunks: List[str]) -> None:
    """
    Gera embeddings para uma lista de chunks de texto e os armazena no Supabase.

    Args:
        chunks: Uma lista de strings, onde cada string é um chunk de texto.

    Raises:
        EmbeddingError: Se ocorrer uma falha durante a geração dos embeddings
                        ou no armazenamento dos vetores.
    """
    try:
        logger.info(
            f"Iniciando o processo de embedding e armazenamento de {len(chunks)} chunks."
        )
        supabase_client = get_supabase_client()


        embeddings = GoogleGenerativeAIEmbeddings(
            # O modelo "models/embedding-001" está obsoleto.
            # Usamos o "text-embedding-004", que é um modelo mais recente e recomendado
            # para tarefas de embedding e que também gera vetores de 768 dimensões.
            model="models/gemini-embedding-2", google_api_key=config.get_settings().GOOGLE_API_KEY
        )

        SupabaseVectorStore.from_texts(
            texts=chunks,
            embedding=embeddings,
            client=supabase_client,
            table_name="documents",
            query_name="match_documents",
        )
        logger.info(f"{len(chunks)} chunks foram vetorizados e armazenados com sucesso.")
    except Exception as e:
        # Usar logger.exception para capturar o traceback completo do erro original.
        # Isso é crucial para o debug, pois revela a causa raiz do problema.
        logger.exception(
            "Uma exceção não tratada ocorreu durante a vetorização e armazenamento."
        )
        raise EmbeddingError("Falha ao gerar embeddings ou armazenar vetores.") from e
    




