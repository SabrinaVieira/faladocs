from unittest.mock import patch

from src.app import render_file_uploader


def test_Given_Nothing_When_render_file_uploader_Then_CallsStreamlitUploaderWithCorrectParams():
    """
    Given: Nenhuma condição prévia.
    When: A função render_file_uploader é chamada.
    Then: O componente st.file_uploader é chamado com os parâmetros corretos.
    """
    # Arrange
    with patch("streamlit.file_uploader") as mock_file_uploader:
        # Act
        render_file_uploader()

        # Assert
        mock_file_uploader.assert_called_once_with(
            label="Faça o upload de um documento PDF", type=["pdf"]
        )


def test_Given_DocumentIsProcessed_When_render_question_input_Then_CallsStreamlitChatInput():
    """
    Given: Um documento foi processado com sucesso.
    When: A função render_question_input é chamada.
    Then: O componente st.chat_input é renderizado para o usuário.
    """
    # Arrange
    with patch("streamlit.chat_input") as mock_chat_input:
        from src.app import render_question_input

        # Act
        render_question_input(document_processed=True)

        # Assert
        mock_chat_input.assert_called_once_with(
            "Faça sua pergunta sobre o documento..."
        )


def test_Given_DocumentIsNotProcessed_When_render_question_input_Then_DoesNotCallStreamlitChatInput():
    """
    Given: Um documento ainda não foi processado.
    When: A função render_question_input é chamada.
    Then: O componente st.chat_input não deve ser renderizado.
    """
    # Arrange
    with patch("streamlit.chat_input") as mock_chat_input:
        from src.app import render_question_input

        # Act
        render_question_input(document_processed=False)

        # Assert
        mock_chat_input.assert_not_called()