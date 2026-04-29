[METADADOS]
Arquivo de Destino: `src/services/vectorization_service.py`
Linguagem/Ambiente: Python, rodando estritamente em ambiente virtual (venv). Não assuma conteinerização ou Docker sob nenhuma hipótese.

[ASSINATURA E INTERFACE]
Entradas: Uma função `embed_and_store_chunks` que recebe uma lista de chunks de texto (`List[str]`).
Saídas: Nenhuma (`None`). A função possui o efeito colateral de persistir os dados.
Tipagem: Exige Type Hints rigorosos em todas as assinaturas. `from typing import List; def embed_and_store_chunks(chunks: List[str]) -> None:`.

[REGRAS DE NEGÓCIO E COMPORTAMENTO]
1. A função deve instanciar o modelo de embeddings `GoogleGenerativeAIEmbeddings`, utilizando a API key do módulo de configuração.
2. A função deve obter a instância do cliente Supabase através do adaptador (`src/adapters/database/supabase_client.py`).
3. A função deve utilizar `SupabaseVectorStore.from_texts()` para orquestrar a geração dos embeddings e o armazenamento.
4. Os parâmetros para `from_texts` devem incluir os chunks, a instância de embeddings, o cliente Supabase, e o nome da tabela de destino no banco vetorial.

[TRATAMENTO DE ERROS E SEGURANÇA]
- A função deve tratar exceções relacionadas a chamadas de rede, tanto para a API do Google Gemini (embeddings) quanto para o Supabase (armazenamento).
- Exceções customizadas como `EmbeddingError` ou `VectorStorageError` devem ser lançadas para sinalizar a falha ao chamador.
- O log de erro deve registrar o tipo da exceção e uma mensagem genérica, sem expor dados sensíveis do chunk ou chaves de API.

[RESTRIÇÕES ARQUITETURAIS]
- Este serviço não deve ter conhecimento sobre a origem dos chunks (ex: PDF, UI). Ele apenas recebe uma lista de textos e a processa.
- A lógica está estritamente ligada ao ecossistema LangChain (`langchain-google-genai`, `langchain.vectorstores.supabase`).