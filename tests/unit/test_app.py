from unittest.mock import patch

# import pytest # Não é necessário se não houver fixtures ou parametrização

from src.app import render_file_uploader


def test_file_uploader_is_rendered_with_correct_parameters():
    """
    Garante que o st.file_uploader é chamado com os parâmetros corretos
    conforme a especificação em rf01_upload_pdf_document.md.
    """
    # Mocka a função st.file_uploader para isolar a UI
    with patch("streamlit.file_uploader") as mock_file_uploader:
        # Chama a função que deve renderizar o componente
        render_file_uploader()

        # Garante que a função da UI foi chamada exatamente uma vez
        mock_file_uploader.assert_called_once_with(
            label="Faça o upload de um documento PDF", type=["pdf"]
        )


def test_question_input_is_rendered_when_document_is_processed():
    """
    Garante que o st.chat_input é chamado com o label correto
    quando o documento foi processado.
    """
    with patch("streamlit.chat_input") as mock_chat_input:
        # Simula que o documento foi processado
        from src.app import render_question_input

        render_question_input(document_processed=True)

        # Verifica se o st.chat_input foi chamado uma vez com o label esperado
        mock_chat_input.assert_called_once_with(
            "Faça sua pergunta sobre o documento..."
        )


def test_question_input_is_not_rendered_when_document_is_not_processed():
    """
    Garante que o st.chat_input NÃO é chamado
    quando o documento NÃO foi processado.
    """
    with patch("streamlit.chat_input") as mock_chat_input:
        from src.app import render_question_input
        render_question_input(document_processed=False)
        mock_chat_input.assert_not_called()