import io
import logging
from unittest.mock import MagicMock, patch

import pytest

# A especificação rt03 aponta para um serviço, então os testes assumem
# que a implementação estará em `src/services/document_service.py`
# e as exceções customizadas em `src/core/exceptions.py`.
# O código-fonte real será importado de 'src', não de 'tests'.
from src.services.document_service import (
    PDFProcessingError,
    extract_text_from_pdf,
)


def test_Given_ValidPdfBytes_When_extract_text_from_pdf_Then_ReturnsConcatenatedText():
    """
    Given: Um stream de bytes de um PDF válido com múltiplas páginas.
    When: A função extract_text_from_pdf é chamada.
    Then: Ela deve retornar uma única string com o texto de todas as páginas concatenado.
    """
    # Arrange (Dado)
    fake_pdf_bytes = io.BytesIO(b"%PDF-fake-content")
    mock_page1 = MagicMock()
    mock_page1.extract_text.return_value = "Texto da página 1. "
    mock_page2 = MagicMock()
    mock_page2.extract_text.return_value = "Texto da página 2."

    mock_pdf_reader = MagicMock()
    mock_pdf_reader.pages = [mock_page1, mock_page2]

    with patch(
        "src.services.document_service.PdfReader", return_value=mock_pdf_reader
    ) as mock_pdf_reader_class:
        # Act (Quando)
        extracted_text = extract_text_from_pdf(fake_pdf_bytes)

        # Assert (Então)
        mock_pdf_reader_class.assert_called_once_with(fake_pdf_bytes)
        assert extracted_text == "Texto da página 1. Texto da página 2."
        mock_page1.extract_text.assert_called_once()
        mock_page2.extract_text.assert_called_once()


def test_Given_PdfWithNoPages_When_extract_text_from_pdf_Then_ReturnsEmptyString():
    """
    Given: Um stream de bytes de um PDF que não contém páginas.
    When: A função extract_text_from_pdf é chamada.
    Then: Ela deve retornar uma string vazia.
    """
    # Arrange
    fake_pdf_bytes = io.BytesIO(b"%PDF-fake-empty")
    mock_pdf_reader = MagicMock()
    mock_pdf_reader.pages = []  # Sem páginas

    with patch(
        "src.services.document_service.PdfReader", return_value=mock_pdf_reader
    ):
        # Act
        extracted_text = extract_text_from_pdf(fake_pdf_bytes)

        # Assert
        assert extracted_text == ""


def test_Given_CorruptedPdfBytes_When_extract_text_from_pdf_Then_RaisesPDFProcessingError(
    caplog,
):
    """
    Given: Um stream de bytes de um arquivo PDF inválido ou corrompido.
    When: A função extract_text_from_pdf é chamada.
    Then: Ela deve capturar o erro da biblioteca, logar e levantar uma PDFProcessingError.
    """
    # Arrange
    # Import da biblioteca de erro aqui para evitar import global desnecessário
    from pypdf.errors import PdfReadError

    caplog.set_level(logging.ERROR)
    corrupted_pdf_bytes = io.BytesIO(b"isto nao e um pdf")

    with patch(
        "src.services.document_service.PdfReader", side_effect=PdfReadError("Erro de leitura")
    ) as mock_pdf_reader_class:
        # Act & Assert
        with pytest.raises(PDFProcessingError) as exc_info:
            extract_text_from_pdf(corrupted_pdf_bytes)

        assert "Falha ao processar o arquivo PDF." in str(exc_info.value)
        assert "Falha ao ler o conteúdo do PDF" in caplog.text
        assert "PdfReadError" in caplog.text

        mock_pdf_reader_class.assert_called_once_with(corrupted_pdf_bytes)