# Documento de Escopo: MVP do Projeto FalaDocs

**Versão:** 1.0
**Data:** 2026-04-28

## 1. Objetivo

O objetivo deste MVP (Minimum Viable Product) é desenvolver e validar o núcleo funcional da aplicação "FalaDocs", um assistente conversacional (chatbot) baseado em arquitetura RAG (*Retrieval-Augmented Generation*). O MVP tem como objetivo permitir que usuários façam o upload de um documento PDF, extraiam seu conteúdo e interajam com ele via perguntas em linguagem natural.

A aplicação será construída com alto rigor técnico para garantir escalabilidade e manutenibilidade, utilizando Python, Streamlit (Frontend), LangChain (Orquestração), Google Gemini flash 2.5 (LLM) e Supabase (Vector DB e Banco Relacional para histórico e feedbacks). O foco central é entregar um fluxo confiável de extração, vetorização, recuperação de contexto e geração de respostas estritamente baseadas no documento fornecido, mitigando alucinações.

## 2. Requisitos Funcionais (RF)

- **RF01:** O sistema deve permitir o upload de documentos em formato PDF (`.pdf`) através da interface web.
- **RF02:** O sistema deve processar o conteúdo dos documentos submetidos, dividindo-os em segmentos de texto gerenciáveis (chunks).
- **RF03:** O sistema deve gerar embeddings vetoriais para cada chunk de texto e armazená-los no Vector DB do Supabase.
- **RF04:** O sistema deve prover uma interface gráfica (via Streamlit) para que o usuário possa inserir uma pergunta.
- **RF05:** O sistema deve realizar uma busca de similaridade no banco de dados vetorial para encontrar os chunks de texto mais relevantes para a pergunta do usuário.
- **RF06:** O sistema deve submeter a pergunta do usuário e os chunks de texto relevantes a um serviço de LLM para gerar uma resposta.
- **RF07:** O sistema deve exibir a resposta gerada pelo LLM ao usuário na interface do Streamlit.

## 3. Requisitos Não Funcionais (RNF)

### RNF01: Arquitetura e Organização Modular
- **Clean Architecture:** O projeto seguirá os princípios da Clean Architecture para garantir a separação de responsabilidades e o baixo acoplamento entre os módulos. A estrutura será dividida em camadas:
    - **Domain:** Contém as entidades e regras de negócio puras (ex: `Documento`, `Chunk`).
    - **Application:** Orquestra os fluxos de trabalho (casos de uso), como `ProcessarDocumento` e `RealizarPergunta`.
    - **Adapters/Interfaces:** Conectores para o mundo externo, como a UI (Streamlit), clientes de banco de dados e o cliente do LLM.
    - **Frameworks & Drivers:** Implementações concretas e tecnologias externas (ex: `Streamlit`, `Supabase`, `cliente Google Gemini`).
- **Separação de Serviços:** A lógica será modularizada em serviços com responsabilidades únicas:
    - **Serviço de Documentos:** Responsável pelo parsing, chunking e pré-processamento do texto.
    - **Serviço de Vetorização:** Responsável pela comunicação com o banco de dados vetorial (criação e busca de embeddings).
    - **Serviço de LLM:** Encapsula a lógica de comunicação com a API do LLM, incluindo a formatação de prompts e o tratamento de respostas.

### RNF02: Padrão de Código e Qualidade
- **PEP8:** Todo o código Python deve aderir estritamente ao guia de estilo PEP8.
- **Formatação Automática:** O projeto utilizará `Black` e `Ruff` para garantir a formatação consistente e a detecção de erros de linting.
- **Clean Code:** Serão aplicados princípios de código limpo, como nomes de variáveis e funções significativos, funções pequenas e com responsabilidade única (SRP), e a redução de complexidade ciclomática.

### RNF03: Estratégia de Testabilidade
- **Framework de Testes:** `Pytest` será o framework padrão para todos os testes automatizados.
- **Testes Unitários:**
    - Cobrirão toda a lógica de negócio na camada de `Application` e `Domain`.
    - Funções de processamento de texto (ex: `chunk_text`) e validações de dados serão testadas de forma isolada.
    - Dependências externas (I/O, chamadas de rede para LLMs, acesso ao DB) serão mockadas para garantir que os testes sejam rápidos e determinísticos.
- **Testes de Integração:**
    - Validarão a interação entre os serviços principais: o fluxo desde o recebimento da pergunta na interface, passando pela busca no banco vetorial e a chamada ao serviço do LLM.
    - Testarão a conexão e a comunicação real com o banco de dados vetorial em um ambiente de teste.
- **Cobertura de Código:** A meta de cobertura de testes para os módulos de lógica de negócio críticos é de, no mínimo, 80%.

### RNF04: Segurança
- **Gerenciamento de Segredos:** Chaves de API e outras credenciais sensíveis não devem ser versionadas no código. Elas serão gerenciadas através de variáveis de ambiente e carregadas via `python-dotenv` em ambiente de desenvolvimento.
- **Logs:** Logs de erro não devem expor stack traces completos ou dados sensíveis em ambientes produtivos. As mensagens de erro para o usuário final serão genéricas.

### RNF05: Ambiente e Dependências
- **Ambiente Virtual:** O desenvolvimento será realizado exclusivamente dentro de um ambiente virtual Python (`venv`), criado e gerenciado conforme o `requirements.txt`.
- **Proibição de Docker:** Para este MVP, não serão utilizadas soluções baseadas em Docker, conforme as regras globais do projeto.

### RNF06: Versionamento e Documentação
- **Conventional Commits:** Todos os commits no repositório Git seguirão o padrão Conventional Commits (ex: `feat:`, `fix:`, `docs:`).
- **Tratamento de Erros e Logging:** Funções críticas devem incluir blocos `try...except` para tratamento de exceções e registrar logs informativos (para fluxos bem-sucedidos) e de erro (para falhas), permitindo rastreabilidade e depuração.

## 4. Fora de Escopo do MVP

- Autenticação e múltiplos usuários.
- Persistência de histórico de conversas entre sessões.
- Gerenciamento de documentos (ex: listar, deletar ou atualizar documentos já processados).
- Suporte a outros formatos de arquivo além de `.pdf` (como `.txt`, `.md`, `.docx`).
- Otimizações de performance para processamento em larga escala.
- Pipeline de deploy automatizado para ambiente de produção.

## 5. Critérios de Aceite

O MVP será considerado concluído quando todos os seguintes critérios forem atendidos:

1.  **Funcionalidade Principal:** Todos os Requisitos Funcionais (RF01 a RF07) estão implementados e operacionais através da interface com Streamlit.
2.  **Qualidade de Código:** O código-fonte está em conformidade com os padrões de código (RNF02) e arquitetura (RNF01) definidos.
3.  **Testes:** A suíte de testes automatizados (unitários e de integração) existe, cobre os fluxos críticos com no mínimo 80% de cobertura e todos os testes passam com sucesso.
4.  **Segurança e Ambiente:** Os requisitos de segurança (RNF04) e ambiente (RNF05) são cumpridos.
5.  **Documentação:** O `README.md` do projeto contém instruções claras sobre como configurar o ambiente virtual, instalar as dependências e executar a aplicação e os testes.
6.  **Revisão:** O código foi submetido a um processo de code review e aprovado pela equipe de desenvolvimento.

---