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
    chunk_text,
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


# region: Testes para rt04_chunk_text

# Texto longo para forçar a divisão em múltiplos chunks.
# Assumindo chunk_size=1000 e chunk_overlap=200 na implementação.
LONG_TEXT = "Este é um texto muito longo " * 200

# Texto curto, menor que o chunk_size padrão.
SHORT_TEXT = "Este é um texto curto."


def test_chunk_text_Given_long_text_When_chunk_text_is_called_Then_returns_list_of_chunks():
    """
    Given: Um texto longo que excede o tamanho do chunk.
    When: A função chunk_text é chamada.
    Then: Retorna uma lista de strings (chunks) com mais de um elemento.
    """
    # When
    chunks = chunk_text(LONG_TEXT)

    # Then
    assert isinstance(chunks, list)
    assert len(chunks) > 1
    assert all(isinstance(chunk, str) for chunk in chunks)


def test_chunk_text_Given_short_text_When_chunk_text_is_called_Then_returns_list_with_single_chunk():
    """
    Given: Um texto curto que não excede o tamanho do chunk.
    When: A função chunk_text é chamada.
    Then: Retorna uma lista contendo um único item, que é o texto original.
    """
    # When
    chunks = chunk_text(SHORT_TEXT)

    # Then
    assert isinstance(chunks, list)
    assert len(chunks) == 1
    assert chunks[0] == SHORT_TEXT


def test_chunk_text_Given_empty_string_When_chunk_text_is_called_Then_returns_empty_list():
    """
    Given: Uma string vazia.
    When: A função chunk_text é chamada.
    Then: Retorna uma lista vazia.
    """
    # When
    chunks = chunk_text("")

    # Then
    assert isinstance(chunks, list)
    assert len(chunks) == 0


def test_chunk_text_Given_non_string_input_When_chunk_text_is_called_Then_raises_TypeError():
    """
    Given: Uma entrada que não é uma string (ex: None ou int).
    When: A função chunk_text é chamada com essa entrada.
    Then: Um TypeError deve ser levantado.
    """
    with pytest.raises(TypeError):
        chunk_text(None)

    with pytest.raises(TypeError):
        chunk_text(12345)


# endregion