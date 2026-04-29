### 📄 Prompt 1 prompts-gemini-code-assitant-default (2.5-flash)
Context (Contexto): Estou desenvolvendo o MVP do "FalaDocs" Objective (Objetivo): Com base nos arquivos fornecidos (@Escopo_FalaDocs_v3.txt), gere o documento de escopo-mvp.md consolidado Você deve identificar lacunas no documento original e complementar o novo documento com requisitos de qualidade de software, incluindo organização modular, padrões de código consistentes (Clean Code), e estratégia de testabilidade (testes automatizados com Pytest, cobertura de fluxo crítico e validações)

Style (Estilo): Utilize uma linguagem técnica, profissional e direta Tone (Tom): Analítico, O tom deve ser de um Arquiteto de Software ou Lead Developer focado em viabilidade técnica e qualidade Audience (Público): Desenvolvedores de software, engenheiros de QA Response (Resposta): Forneça o conteúdo completo formatado em Markdown no diretorio docs/. O documento deve seguir a estrutura:

Objetivo Requisitos Funcionais (RF) Requisitos Não Funcionais (RNF) - Incluindo os novos requisitos de qualidade e testes solicitados Fora de Escopo Criterios de aceite

Ao elaborar a seção de Requisitos Não Funcionais, detalhe como a testabilidade será garantida (ex: unitários para processamento de chunks, integração para chamadas de LLM). Certifique-se de que a organização modular especifique a separação de responsabilidades (serviços de LLM, processamento de documentos, banco de dados e interface) Em "Criterios de aceite" definição de quando a aplicação esta pronta no geral

### 📄 Prompt 2
Context (Contexto): O projeto "FalaDocs" deve ser entregue em 3 releases progressivas: Core (funcionalidades com testes de unidade), Qualidade (refinamento e testes de integração) e Entrega Final (polimento e persistência)
Objective (Objetivo):
Com base nos documentos @escopo-mvp.md e @requirements.txt, crie o backlog mínimo de desenvolvimento. Você deve desmembrar as funcionalidades em requisitos técnicos e funcionais, atribuindo IDs únicos (ex: RF01, RT01). O foco deve ser em garantir a organização modular e a testabilidade automatizada (Pytest) desde o início. Se identificar lacunas técnicas necessárias para o funcionamento do RAG que não estão nos docs originais, identifiaque-as e as complemente. Ao final do processo liste se há necessidade de revisão e alteração do documento de @escopo-mvp_md

Style (Estilo): Formato de checklist em Markdown, organizado por Releases. Linguagem técnica, clara e concisa
Tone (Tom): Profissional, focado em engenharia de software e orientado a resultados
Audience (Público): Desenvolvedores e Analistas de Sistemas
Response (Resposta):
Forneça exclusivamente o conteúdo para o arquivo docs/backlog.md. Estruture a resposta da seguinte forma:
Release 1: Core (Foco no pipeline RAG: Upload, Extração, Vetorização e Chat básico)
Release 2: Qualidade (Foco em Requisitos Técnicos de Testabilidade, Padrões de Código, Validações e Cobertura de Testes Automatizados).
Release 3: Entrega Final (Foco em Persistência de Histórico, Sistema de Feedback e Refinamento de UI)

Para cada item, inclua:
ID (RF para Funcional e RT para Técnico)
Descrição direta
Critérios de Aceite (AC) claros

### 📄 Prompt 3
Revise o documento @escopo-mvp.md, pois este deve  seguir as tecnologias descritas em @requirements.txt

### 📄 Prompt 4
Objetivo: Com base no porjeto, gere o diagrama mermaid de componentes e fluxo de dados
Estilo: simples, legivel e versonável
Resposta: apenas bloco mermaid

### 📄 Prompt 5
Para garantir a qualidade do código gerado por IA, utilizamos a abordagem Spec-Driven Development (SDD). Precisamos traduzir o Backlog da Release 1 em contratos SDD individuais

Objetivo: Criar um arquivo de Contrato SDD para cada um dos requisitos que compõem a Release 1 do FalaDocs

Expectativas:
1. Gere um arquivo distinto para cada requisito.
2. Utilize a nomenclatura estrita: rtXX_<nome>.md para requisitos técnicos, e rnfXX_<nome>.md para requisitos não funcionais e rfXX_<nome>.md para requisitos funcionais (onde XX é o ID do backlog).
3. Cada arquivo deve OBRIGATORIAMENTE seguir o template exato abaixo:

"[METADADOS]
Arquivo de Destino: [Caminho do arquivo]
Linguagem/Ambiente: Python, rodando estritamente em ambiente virtual (venv). Não assuma conteinerização ou Docker sob nenhuma hipótese.

[ASSINATURA E INTERFACE]
Entradas: [Definir]
Saídas: [Definir]
Tipagem: Exige Type Hints rigorosos em todas as assinaturas.

[REGRAS DE NEGÓCIO E COMPORTAMENTO]
1. [Regra 1]
2. [Regra 2]

[TRATAMENTO DE ERROS E SEGURANÇA]
- [Definir exceções customizadas e regras de log limitando vazamento de dados sensíveis e stack trace genérico, ex: type(e).__name__]

[RESTRIÇÕES ARQUITETURAIS]
- [Definir os limites de isolamento, garantindo separação entre UI (Streamlit), RAG (LangChain) e Database (Supabase)]"

Escopo: Limite a geração dos itens da Release 1

Tom/Target: Arquiteto de Software Sênior criando especificações inquebráveis para desenvolvedores ou assistentes de IA.

Assets: Considere os documentos escopo-mvp.md e backlog.md previamente fornecidos no contexto.

Resposta: Retorne o conteúdo em markdown de cada um dos arquivos gerados, separados por blocos de código, prontos para serem salvos na pasta docs/rules/ do projeto.

### 📄 Prompt 6
crie o arquivos no diretorio

### 📄 Prompt 7
Objetivo: Criar um arquivo de Contrato SDD para cada um dos requisitos que compõem a Release 2 do FalaDocs
Expectativas:
1. Gere um arquivo distinto para cada requisito.
2. Utilize a nomenclatura estrita: rtXX_<nome>.md para requisitos técnicos, e rnfXX_<nome>.md para requisitos não funcionais e rfXX_<nome>.md para requisitos funcionais (onde XX é o ID do backlog).
3. Cada arquivo deve OBRIGATORIAMENTE seguir o template exato abaixo:

"[METADADOS]
Arquivo de Destino: [Caminho do arquivo]
Linguagem/Ambiente: Python, rodando estritamente em ambiente virtual (venv). Não assuma conteinerização ou Docker sob nenhuma hipótese.
[ASSINATURA E INTERFACE]
Entradas: [Definir]
Saídas: [Definir]
Tipagem: Exige Type Hints rigorosos em todas as assinaturas.
[REGRAS DE NEGÓCIO E COMPORTAMENTO]
1. [Regra 1]
2. [Regra 2]
[TRATAMENTO DE ERROS E SEGURANÇA]
[RESTRIÇÕES ARQUITETURAIS]

Escopo: Limite a geração dos itens da Release 2
Tom/Target: Arquiteto de Software Sênior criando especificações inquebráveis para desenvolvedores ou assistentes de IA.
Assets: Considere os documentos escopo-mvp.md e backlog.md previamente fornecidos no contexto.
Resposta: Retorne o conteúdo em markdown de cada um dos arquivos gerados, separados por blocos de código, prontos para serem salvos na pasta docs/rules/ do projeto.

### 📄 Prompt 8

### 📄 Prompt 9

### 📄 Prompt 10
