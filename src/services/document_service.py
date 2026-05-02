import io
import logging
from typing import List

from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader
from pypdf.errors import PdfReadError

from core.exceptions import PDFProcessingError

logger = logging.getLogger(__name__)

# Constantes para a lógica de "chunking", facilitando a manutenção e o ajuste fino.
# O tamanho do chunk (CHUNK_SIZE) define o comprimento máximo de cada segmento de texto.
# A sobreposição (CHUNK_OVERLAP) garante que o contexto seja mantido entre os chunks.

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


def extract_text_from_pdf(pdf_bytes: io.BytesIO) -> str:
    """
    Extrai o texto de um objeto de bytes de um arquivo PDF.

    Args:
        pdf_bytes: Um objeto file-like (BytesIO) contendo os dados do PDF.

    Returns:
        Uma string única contendo o texto concatenado de todas as páginas do PDF.
        Retorna uma string vazia se o PDF não tiver páginas.

    Raises:
        PDFProcessingError: Se o arquivo PDF estiver corrompido ou não puder ser lido.
    """
    try:
        pdf_reader = PdfReader(pdf_bytes)
        if not pdf_reader.pages:
            return ""

        text_parts = [page.extract_text() for page in pdf_reader.pages]
        return "".join(text_parts)

    except PdfReadError as e:
        error_msg = f"Falha ao ler o conteúdo do PDF. Erro da biblioteca: {type(e).__name__}"
        logger.error(error_msg)
        raise PDFProcessingError("Falha ao processar o arquivo PDF.") from e


def chunk_text(text: str) -> List[str]:
    """
    Divide um texto longo em segmentos (chunks) menores e sobrepostos.

    Args:
        text: A string de texto a ser dividida.

    Returns:
        Uma lista de strings, onde cada string é um chunk do texto original.
        Retorna uma lista vazia se o texto de entrada for vazio ou contiver apenas espaços.

    Raises:
        TypeError: Se a entrada fornecida não for uma string.
    """
    if not isinstance(text, str):
        raise TypeError("A entrada para a função chunk_text deve ser uma string.")

    if not text.strip():
        return []

    # Utiliza o RecursiveCharacterTextSplitter do LangChain, que tenta dividir
    # o texto em separadores comuns (como quebras de linha e espaços) para
    # manter a coesão semântica dos chunks.
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        add_start_index=True,  # Adiciona metadados sobre a posição do chunk
    )

    # O método create_documents retorna uma lista de objetos Document.
    # Precisamos extrair o conteúdo de texto (page_content) de cada um.
    documents = text_splitter.create_documents([text])
    return [doc.page_content for doc in documents]
