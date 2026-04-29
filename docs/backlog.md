# Backlog de Desenvolvimento - Projeto FalaDocs

Este documento detalha as tarefas de desenvolvimento, organizadas em releases progressivas, para a construção do MVP do FalaDocs.

---

## Release 1: Core (Foco no pipeline RAG: Upload, Extração, Vetorização e Chat básico)

*O objetivo desta release é construir o fluxo ponta-a-ponta da aplicação, garantindo que um usuário possa subir um documento e fazer uma pergunta, recebendo uma resposta baseada no conteúdo.*

- [ ] **ID:** RT01
  - **Descrição:** Configurar a estrutura inicial do projeto seguindo os princípios da Clean Architecture. Inclui a criação dos diretórios (`src`, `tests`, `docs`), ambiente virtual (`venv`) e instalação das dependências do `requirements.txt`.
  - **AC:** A estrutura de pastas está criada e as dependências estão instaladas em um ambiente virtual funcional.

- [ ] **ID:** RT02
  - **Descrição:** Implementar o gerenciamento de segredos para as chaves de API (Google Gemini, Supabase) utilizando `python-dotenv`.
  - **AC:** As chaves são carregadas a partir de um arquivo `.env` e não estão hard-coded no código-fonte.

- [ ] **ID:** RF01
  - **Descrição:** Desenvolver a interface de upload de arquivos na UI com Streamlit, permitindo que o usuário selecione e envie um documento PDF.
  - **AC:** A interface exibe um componente `st.file_uploader` que aceita apenas arquivos `.pdf`.

- [ ] **ID:** RT03
  - **Descrição:** Criar um serviço de processamento de documentos para extrair o texto de um arquivo PDF enviado.
  - **AC:** Uma função recebe o arquivo PDF e retorna seu conteúdo textual completo como uma string.

- [ ] **ID:** RT04
  - **Descrição:** Implementar a lógica de "chunking" para dividir o texto extraído em segmentos menores e sobrepostos, utilizando `langchain.text_splitter`.
  - **AC:** Uma função recebe uma string de texto longa e a retorna como uma lista de strings (chunks) de tamanho definido.

- [ ] **ID:** RT05
  - **Descrição:** Configurar o cliente de conexão com o Supabase e criar um serviço para interagir com o Vector Store.
  - **AC:** O sistema consegue se conectar com sucesso à instância do Supabase.

- [ ] **ID:** RT06
  - **Descrição:** Implementar o fluxo de geração de embeddings (via `langchain-google-genai`) e armazenamento dos vetores no Supabase.
  - **AC:** Após o chunking, os segmentos de texto são vetorizados e persistidos na tabela de vetores do Supabase.

- [ ] **ID:** RF02
  - **Descrição:** Desenvolver a interface de chat básica no Streamlit, com um campo de entrada de texto para a pergunta do usuário e um botão de envio.
  - **AC:** O usuário pode digitar uma pergunta e submetê-la.

- [ ] **ID:** RT07
  - **Descrição:** Implementar a lógica de busca de similaridade (retrieval) que, dada uma pergunta, consulta o Supabase e retorna os chunks mais relevantes.
  - **AC:** A função de busca retorna uma lista de chunks contextualmente relacionados à pergunta.

- [ ] **ID:** RT08
  - **Descrição:** Criar um serviço para orquestrar a chamada ao LLM (Google Gemini) via LangChain, formatando o prompt com o contexto recuperado (chunks) e a pergunta do usuário.
  - **AC:** O serviço monta o prompt final e realiza uma chamada bem-sucedida à API do Gemini.

- [ ] **ID:** RF03
  - **Descrição:** Exibir a resposta gerada pelo LLM na interface do Streamlit.
  - **AC:** A resposta do chatbot aparece na tela após o usuário fazer uma pergunta.

---

## Release 2: Qualidade (Foco em Testabilidade, Padrões de Código e Validações)

*O objetivo desta release é robustecer o código-fonte, garantir a qualidade através de testes automatizados e melhorar o tratamento de erros.*

- [ ] **ID:** RT09
  - **Descrição:** Configurar as ferramentas de qualidade de código `Black` e `Ruff` no projeto e integrá-las a um hook de pre-commit.
  - **AC:** O código é automaticamente formatado e verificado contra erros de linting antes de cada commit.

- [ ] **ID:** RT10
  - **Descrição:** Desenvolver testes unitários com Pytest para os serviços de lógica pura (extração de texto, chunking, formatação de prompt).
  - **AC:** As funções são testadas de forma isolada, com dependências externas (I/O, rede) mockadas. A cobertura de testes para estes módulos atinge 80%.

- [ ] **ID:** RT11
  - **Descrição:** Desenvolver testes de integração para o pipeline RAG. O teste deve simular o upload, processamento, busca no Supabase (em ambiente de teste) e chamada ao LLM (mockado).
  - **AC:** O teste de integração valida o fluxo completo desde a pergunta até a geração da resposta, garantindo que os componentes se comunicam corretamente.

- [ ] **ID:** RT12
  - **Descrição:** Implementar validações e tratamento de erros na interface.
  - **AC:** O sistema exibe mensagens claras para o usuário em casos de falha (ex: "Falha ao processar o PDF", "Não foi possível conectar ao serviço", "Formato de arquivo inválido").

- [ ] **ID:** RT13
  - **Descrição:** Implementar um sistema de logging para registrar eventos importantes e erros em todo o fluxo da aplicação.
  - **AC:** Erros de processamento, falhas de API e outras exceções são registradas em um arquivo de log para facilitar a depuração.

---

## Release 3: Entrega Final (Foco em Persistência de Histórico e Refinamento)

*O objetivo desta release é adicionar funcionalidades de valor agregado, como histórico de conversas e feedback, além de polir a experiência do usuário.*

- [ ] **ID:** RT14
  - **Descrição:** Modelar e configurar as tabelas no banco de dados relacional do Supabase para armazenar o histórico de conversas e os feedbacks.
  - **AC:** As tabelas `chat_history` e `feedback` estão criadas e acessíveis via cliente Supabase.

- [ ] **ID:** RF04
  - **Descrição:** Implementar a persistência e exibição do histórico da conversa na sessão atual do Streamlit.
  - **AC:** O usuário pode ver suas perguntas anteriores e as respostas do bot na mesma tela, em ordem cronológica.

- [ ] **ID:** RF05
  - **Descrição:** Adicionar botões de feedback (ex: 👍/👎) a cada resposta gerada pelo bot.
  - **AC:** A interface exibe os botões de feedback abaixo de cada resposta.

- [ ] **ID:** RT15
  - **Descrição:** Implementar a lógica de backend para persistir o feedback do usuário no banco de dados Supabase.
  - **AC:** Ao clicar em um botão de feedback, um registro correspondente é criado na tabela `feedback`.

- [ ] **ID:** RT16
  - **Descrição:** Refinar a interface do usuário (UI/UX) com elementos como spinners de carregamento, mensagens de status e um layout mais organizado.
  - **AC:** A aplicação fornece feedback visual ao usuário enquanto o documento está sendo processado ou a resposta está sendo gerada.

- [ ] **ID:** RT17
  - **Descrição:** Criar e finalizar a documentação do projeto (`README.md`) com instruções claras de instalação, configuração e execução.
  - **AC:** Um novo desenvolvedor consegue configurar e rodar o projeto localmente seguindo apenas o `README.md`.

---

### ⚠️ Necessidade de Revisão do Documento de Escopo

**É altamente recomendável a revisão e alteração do arquivo `docs/escopo-mvp.md`.**

Foram identificadas inconsistências críticas entre a seção **"Objetivo"** e as seções **"Requisitos Funcionais (RF)"** e **"Fora de Escopo"**.

1.  **Tecnologia de Interface:** O objetivo cita **Streamlit (GUI)**, mas os RFs descrevem uma **CLI**.
2.  **Formato do Documento:** O objetivo foca em **PDF**, mas os RFs especificam `.txt`/`.md` e a seção "Fora de Escopo" exclui explicitamente o PDF.
3.  **Banco de Dados:** O objetivo e o `requirements.txt` apontam para **Supabase**, mas os RNFs mencionam **ChromaDB**.
4.  **LLM:** O objetivo cita **Google Gemini**, mas os RNFs mencionam um cliente **OpenAI**.

**Ação Sugerida:** Unificar o documento `escopo-mvp.md` para refletir a stack tecnológica definida no `requirements.txt` e no objetivo principal (Streamlit, PDF, Supabase, Gemini), ajustando os Requisitos Funcionais e a seção "Fora de Escopo" para alinhamento. Este backlog foi criado com base nesta interpretação.

<!--
[PROMPT_SUGGESTION]Com base no RT01 do backlog, gere a estrutura de diretórios e arquivos iniciais para o projeto "FalaDocs" seguindo a Clean Architecture.[/PROMPT_SUGGESTION]
[PROMPT_SUGGESTION]Crie o código inicial para o requisito RF01 (Upload de PDF com Streamlit) e RT03 (Extração de texto de PDF).[/PROMPT_SUGGESTION]
