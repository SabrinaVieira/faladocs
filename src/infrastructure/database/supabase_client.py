import logging
import os

from supabase import Client, create_client

from src.core.exceptions import SupabaseConnectionError

logger = logging.getLogger(__name__)


def get_supabase_client() -> Client:
    """
    Cria e retorna um cliente de conexão com o Supabase.

    A função busca as credenciais (URL e Key) a partir das variáveis de ambiente
    'SUPABASE_URL' e 'SUPABASE_KEY'.

    Returns:
        Um objeto de cliente do Supabase pronto para uso.

    Raises:
        SupabaseConnectionError: Se as variáveis de ambiente não estiverem
                                 definidas ou se a conexão falhar.
    """
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")

    if not supabase_url:
        raise SupabaseConnectionError(
            "A variável de ambiente SUPABASE_URL não foi definida."
        )
    if not supabase_key:
        raise SupabaseConnectionError(
            "A variável de ambiente SUPABASE_KEY não foi definida."
        )

    try:
        client: Client = create_client(supabase_url, supabase_key)
        return client
    except Exception as e:
        error_msg = f"Falha ao conectar com o Supabase. Erro: {type(e).__name__}"
        logger.error(error_msg)
        raise SupabaseConnectionError(error_msg) from e