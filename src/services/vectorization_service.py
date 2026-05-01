"""
Serviço responsável pela vetorização de texto e armazenamento no Supabase.
"""

import logging
from typing import List

from langchain_community.vectorstores import SupabaseVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from src.core import config
from src.core.exceptions import EmbeddingError, VectorStorageError
from src.infrastructure.database.supabase_client import get_supabase_client

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
        logger.info("Iniciando o processo de embedding e armazenamento de chunks.")
        supabase_client = get_supabase_client()

        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001", google_api_key=config.get_settings().google_api_key
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
        logger.error(f"Falha ao gerar embeddings ou armazenar vetores: {type(e).__name__}")
        raise EmbeddingError("Falha ao gerar embeddings ou armazenar vetores.") from e