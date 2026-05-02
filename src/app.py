import io
import logging
import streamlit as st
from typing import Optional

from streamlit.runtime.uploaded_file_manager import UploadedFile

from core.exceptions import EmbeddingError, PDFProcessingError
from services.vectorization_service import embed_and_store_chunks
from services.document_service import chunk_text, extract_text_from_pdf

# Configuração básica de logging para exibir mensagens no console
# onde o Streamlit está rodando. Essencial para debug.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if "document_processed" not in st.session_state:
    st.session_state.document_processed = False


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


def main():
    """Função principal para orquestrar a aplicação Streamlit."""
    st.title("FalaDocs 💬")

    # O uploader de arquivo sempre será renderizado.
    # A lógica de processamento só ocorre se um novo arquivo for enviado.
    uploaded_file = render_file_uploader()

    if uploaded_file:
        # Processa o arquivo apenas uma vez, quando ele é carregado.
        if not st.session_state.document_processed:
            with st.spinner(f"Processando '{uploaded_file.name}'..."):
                try:
                    # Lê o arquivo em memória
                    pdf_bytes = io.BytesIO(uploaded_file.getvalue())

                    # RT03: Extrai o texto do PDF
                    text = extract_text_from_pdf(pdf_bytes)
                    st.info("1/3 - Texto extraído do PDF com sucesso.")

                    # RT04: Divide o texto em chunks
                    chunks = chunk_text(text)
                    st.info(f"2/3 - Texto dividido em {len(chunks)} segmentos (chunks).")

                    # RT06: Vetoriza os chunks e armazena no Supabase
                    embed_and_store_chunks(chunks)
                    st.info("3/3 - Segmentos vetorizados e armazenados no banco de dados.")

                    # Armazena os chunks e o status no estado da sessão
                    st.session_state.chunks = chunks
                    st.session_state.document_processed = True
                    st.success(f"Documento processado! {len(chunks)} segmentos criados.")

                # Captura de erros específicos para dar feedback claro.
                except PDFProcessingError as e:
                    st.error(f"Erro ao processar o PDF: {e}")
                    st.session_state.document_processed = False
                except EmbeddingError as e:
                    st.error(f"Erro ao salvar o documento no banco de dados: {e}")
                    st.warning("Verifique o console onde o Streamlit está rodando para ver o erro detalhado.")
                    st.session_state.document_processed = False
                except Exception as e:
                    st.error("Ocorreu um erro inesperado. Verifique o console para detalhes.")
                    logging.exception("Erro inesperado no processamento do arquivo.")

    # Renderiza o campo de pergunta se o documento foi processado
    user_question = render_question_input(st.session_state.document_processed)

    if user_question:
        # Aqui entrará a lógica para buscar o contexto e gerar a resposta (RT07, RT08, RF03)
        st.write(f"Você perguntou: {user_question}")
        # Simula uma resposta
        with st.spinner("Pensando..."):
            st.info("Esta é uma resposta simulada. A integração com o LLM é o próximo passo.")


if __name__ == "__main__":
    main()