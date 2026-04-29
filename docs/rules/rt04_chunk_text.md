[METADADOS]
Arquivo de Destino: `src/services/document_service.py`
Linguagem/Ambiente: Python, rodando estritamente em ambiente virtual (venv). Não assuma conteinerização ou Docker sob nenhuma hipótese.

[ASSINATURA E INTERFACE]
Entradas: Uma função `split_text_into_chunks` que recebe uma string (`str`) de texto.
Saídas: Uma lista de strings (`List[str]`), onde cada item é um chunk de texto.
Tipagem: Exige Type Hints rigorosos em todas as assinaturas. `from typing import List; def split_text_into_chunks(text: str) -> List[str]:`.

[REGRAS DE NEGÓCIO E COMPORTAMENTO]
1. A função deve utilizar a classe `RecursiveCharacterTextSplitter` da biblioteca `langchain.text_splitter`.
2. Os parâmetros `chunk_size` e `chunk_overlap` devem ser definidos com valores configuráveis (ex: 1000 e 200, respectivamente), podendo ser carregados a partir do módulo de configuração.
3. Se a string de entrada for vazia ou `None`, a função deve retornar uma lista vazia.

[TRATAMENTO DE ERROS E SEGURANÇA]
- Dado o uso de uma biblioteca estável como LangChain, o tratamento de exceções para esta função específica é de baixa prioridade, mas a função deve ser robusta a entradas vazias.

[RESTRIÇÕES ARQUITETURAIS]
- Esta função deve ser parte do `document_service`, pois representa uma etapa do processamento de documentos.
- A implementação deve se ater ao uso da biblioteca LangChain para garantir consistência com o restante do pipeline RAG.