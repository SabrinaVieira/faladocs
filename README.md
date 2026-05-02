# FalaDocs

O "FalaDocs" é um assistente conversacional (chatbot) que utiliza a arquitetura RAG (*Retrieval-Augmented Generation*) para permitir que usuários conversem com seus documentos PDF.

## 🎯 Objetivo do MVP

O objetivo deste MVP (Minimum Viable Product) é validar o fluxo principal da aplicação, permitindo que um usuário realize o upload de um documento PDF, faça perguntas em linguagem natural e receba respostas inteligentes e contextuais baseadas estritamente no conteúdo do documento.

## ✨ Funcionalidades (Release 1)

-   **Upload de PDF:** Interface para o usuário enviar um documento no formato `.pdf`.
-   **Processamento de Texto:** Extração automática do conteúdo textual, que é então segmentado em *chunks* gerenciáveis.
-   **Vetorização e Armazenamento:** Geração de embeddings vetoriais para cada *chunk* de texto e armazenamento em um banco de dados vetorial (Supabase).
-   **Chat Interativo:** Interface de chat para o usuário fazer perguntas e receber respostas geradas por um LLM (Google Gemini).

## ⚠️ Limitações da Release 1

Esta primeira versão foca em validar a arquitetura e o fluxo principal. É importante notar as seguintes limitações:

-   **Integração UI-Backend Incompleta:** Embora os serviços de backend para processamento de documentos e vetorização (`document_service`, `vectorization_service`) estejam implementados, a interface do usuário (`app.py`) ainda não está totalmente conectada a eles. Atualmente, o upload do arquivo não dispara o salvamento no banco de dados.
-   **Respostas Simuladas:** A interação no chat ainda não consulta o LLM com o contexto do documento. As respostas são simuladas para validar a interface.
-   **Sem Persistência de Histórico:** A conversa não é salva. Cada atualização da página reinicia o estado do chat.
-   **Usuário Único:** Não há sistema de autenticação ou separação de dados por usuário.

## 🚀 Próximos Passos

A evolução do projeto seguirá o `backlog.md`, com os seguintes objetivos:

1.  **Conectar o Pipeline RAG:** O próximo passo crucial é integrar a interface do Streamlit com os serviços de backend. Isso fará com que o upload de um PDF dispare a extração, o chunking e a vetorização, salvando os dados no Supabase.
2.  **Habilitar Respostas Reais:** Implementar a lógica de busca por similaridade (RT07) e a chamada ao LLM (RT08) para que as perguntas dos usuários sejam respondidas com base no conteúdo real do documento.
3.  **Qualidade e Robustez (Release 2):** Introduzir ferramentas de qualidade de código (`Black`, `Ruff`), expandir a cobertura de testes unitários e de integração, e melhorar o tratamento de erros.
4.  **Funcionalidades Avançadas (Release 3):** Implementar a persistência do histórico de conversas e um sistema de feedback (👍/👎) para as respostas geradas.

## 🛠️ Stack de Tecnologias

-   **Linguagem:** Python 3.11+
-   **Interface (UI):** Streamlit
-   **Orquestração RAG:** LangChain
-   **LLM & Embeddings:** Google Gemini
-   **Banco de Dados Vetorial:** Supabase (com `pgvector`)
-   **Testes:** Pytest

## ⚠️ Pré-requisitos Essenciais

Para que o projeto funcione corretamente, é **obrigatório** possuir e configurar uma chave de API do Google.

-   **Google API Key:** Você precisa de uma chave de API válida, gerada através do Google AI Studio. A API "Generative Language" deve estar ativada para sua chave.
-   **Modelo de Embedding:** O projeto está configurado para utilizar o modelo de embedding `models/gemini-embedding-2`. O uso de um modelo diferente ou a falta de uma chave de API válida resultará em falha no processo de vetorização.

> **Importante:** Sem uma chave de API válida e configurada, o processo de vetorização dos documentos falhará. Consequentemente, nenhum dado será salvo no banco de dados e a aplicação será incapaz de gerar respostas, pois não encontrará contexto para as perguntas.

## ⚙️ Configuração do Ambiente

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd faladocs
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    Crie um arquivo chamado `.env` na raiz do projeto com o conteúdo abaixo.

    ```env
    # /home/sabrina/Documentos/faladocs/.env

    # Chave de API do Google (obrigatória)
    GOOGLE_API_KEY="sua_chave_de_api_aqui"

    # Credenciais do Supabase (obrigatórias)
    SUPABASE_URL="url_do_seu_projeto_supabase"
    SUPABASE_KEY="sua_chave_service_role_do_supabase"
    ```
    Substitua os valores pelas suas credenciais reais.

## 🗄️ Configuração do Banco de Dados (Supabase)

Antes de executar a aplicação, você precisa preparar seu banco de dados no Supabase.

1.  Acesse o **SQL Editor** no painel do seu projeto Supabase.
2.  Copie e execute o conteúdo do script `docs/supabase-scripts.md`. Isso irá habilitar a extensão `pgvector`, criar a tabela `documents` e a função `match_documents`.

## 🚀 Executando a Aplicação

Com o ambiente e o banco de dados configurados, execute o seguinte comando para iniciar a interface do Streamlit:

```bash
streamlit run src/app.py
```

## 🧪 Executando os Testes

Para garantir a qualidade e a integridade do código, execute a suíte de testes com Pytest:

```bash
pytest
```