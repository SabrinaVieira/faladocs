import logging

from supabase import Client, create_client

from core import config
from core.exceptions import SupabaseConnectionError, EmbeddingError

logger = logging.getLogger(__name__)


def get_supabase_client() -> Client:
    """
    Cria e retorna um cliente de conexão com o Supabase.

    A função busca as credenciais (URL e Key) a partir do módulo de
    configuração central da aplicação.

    Returns:
        Um objeto de cliente do Supabase pronto para uso.

    Raises:
        SupabaseConnectionError: Se as credenciais não estiverem configuradas
                                 ou se a conexão falhar.
    """
    # Busca as configurações da fonte única de verdade.
    # A validação da existência das chaves já é feita pela Pydantic na inicialização.
    settings = config.get_settings()
    supabase_url = settings.SUPABASE_URL
    supabase_key = settings.SUPABASE_KEY

    try:
        client: Client = create_client(supabase_url, supabase_key)
        logger.info("Cliente Supabase criado com sucesso.")
        return client
    except Exception as e:
        error_msg = f"Falha ao criar o cliente Supabase. Erro: {type(e).__name__}"
        logger.exception(error_msg)  # Usar exception para logar o traceback completo
        raise SupabaseConnectionError(error_msg) from e