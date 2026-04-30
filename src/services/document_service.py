import io
import logging

from pypdf import PdfReader
from pypdf.errors import PdfReadError

from src.core.exceptions import PDFProcessingError

logger = logging.getLogger(__name__)


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
