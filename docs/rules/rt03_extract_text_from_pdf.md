[METADADOS]
Arquivo de Destino: `src/services/document_service.py`
Linguagem/Ambiente: Python, rodando estritamente em ambiente virtual (venv). Não assuma conteinerização ou Docker sob nenhuma hipótese.

[ASSINATURA E INTERFACE]
Entradas: Uma função `extract_text_from_pdf` que recebe um objeto `io.BytesIO` (conteúdo binário do arquivo PDF).
Saídas: Uma única string (`str`) contendo todo o texto extraído do documento.
Tipagem: Exige Type Hints rigorosos em todas as assinaturas. `def extract_text_from_pdf(pdf_stream: io.BytesIO) -> str:`.

[REGRAS DE NEGÓCIO E COMPORTAMENTO]
1. A função deve utilizar uma biblioteca robusta para leitura de PDF (ex: `pypdf`).
2. O texto de todas as páginas do documento PDF deve ser extraído e concatenado em uma única string.
3. Caracteres de quebra de linha (`\n`) devem ser mantidos para preservar a estrutura básica dos parágrafos.

[TRATAMENTO DE ERROS E SEGURANÇA]
- A função deve ser encapsulada em um bloco `try...except`.
- Em caso de falha na leitura do arquivo (ex: PDF corrompido, protegido por senha), uma exceção customizada `PDFProcessingError` deve ser lançada.
- O log de erro deve registrar o tipo da exceção original e uma mensagem genérica, ex: `logging.error(f"Falha ao processar PDF: {type(e).__name__}")`. Não vazar o stack trace completo para o usuário ou logs de produção.

[RESTRIÇÕES ARQUITETURAIS]
- Este serviço é agnóstico à fonte do arquivo. Ele não deve ter conhecimento de Streamlit ou de qualquer outra camada de UI. Sua única responsabilidade é a extração de texto de um fluxo de bytes.