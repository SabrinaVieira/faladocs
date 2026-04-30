import streamlit as st
from typing import Optional
from streamlit.runtime.uploaded_file_manager import UploadedFile


def render_file_uploader() -> Optional[UploadedFile]:
    """
    Renderiza o componente de upload de arquivo na UI do Streamlit e retorna
    o arquivo enviado.

    Returns:
        Optional[UploadedFile]: O objeto do arquivo enviado pelo usuário ou None.
    """
    uploaded_file = st.file_uploader(
        label="Faça o upload de um documento PDF", type=["pdf"]
    )
    return uploaded_file


def render_question_input(document_processed: bool) -> Optional[str]:
    """
    Renderiza o campo de entrada de pergunta para o usuário.
    Só é exibido se o documento tiver sido processado com sucesso.

    Args:
        document_processed (bool): Indica se o documento foi processado.

    Returns:
        Optional[str]: A pergunta do usuário se submetida, caso contrário None.
    """
    if document_processed:
        user_question = st.chat_input("Faça sua pergunta sobre o documento...")
        return user_question
    return None