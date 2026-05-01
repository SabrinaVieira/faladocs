"""Módulo para exceções customizadas da aplicação."""


class PDFProcessingError(Exception):
    """Exceção levantada para erros durante o processamento de um arquivo PDF."""

    pass


class SupabaseConnectionError(Exception):
    """Exceção levantada para erros ao conectar ou interagir com o Supabase."""

    pass
