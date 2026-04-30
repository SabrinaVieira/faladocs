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
existem muitos difffs e muitas camadas da aplicação ainda sem commites, utilize conventional commites para cada uma da camadas em separado e faça os commites para mim

### 📄 Prompt 9
Sempre consulte o diretório /rules/global_rules.md antes de para garantir acertividade. Se a implementação divergir da spec, priorize a spec ou peça clarificação"
Com base na  especificação rf01_upload_pdf_document.md, escreva PRIMEIRO os testes unitários (pytest) que garantirão que este contrato seja cumprido. Utilize mocks para isolar chamadas de rede.


### 📄 Prompt 10
como rdar o teste e enviar para um arquivo de testo do diretorio logs 
pytest > logs/test_results$(date +%Y%m%d_%H%M%S).log


### 📄 Prompt 11
Sempre consulte o diretório /rules/global_rules.md antes de para garantir acertividade. Se a implementação divergir da spec, priorize a spec ou peça clarificação. escreva a implementação real para fazer esses testes passarem, respeitando as restrições da especificação @rf01_upload_pdf_document.md

### 📄 Prompt 12
Sempre consulte o diretório /rules/global_rules.md antes 
Com base na  especificação rf02_submit_user_question.md, escreva PRIMEIRO os testes unitários (pytest) que garantirão que este contrato seja cumprido. Utilize mocks para isolar chamadas de rede.


### 📄 Prompt 13
Como rodar o teste, enviando o resultado do arquivo para o diretorio /logs - versionado com data e hora
pytest > logs/test_results_$(date +%Y%m%d_%H%M%S).log


### 📄 Prompt 14
escreva a implementação real para fazer esses testes passarem, respeitando as restrições da especificação rf02_submit_user_question.md. 
Sempre consulte o diretório /rules/global_rules.md antes


### 📄 Prompt 15
Sempre consulte o diretório /rules/global_rules.md antes 
Com base na  especificação rt01_setup_project_structure.md, escreva PRIMEIRO os testes unitários (pytest) que garantirão que este contrato seja cumprido. Utilize mocks para isolar chamadas de rede.


### 📄 Prompt 16
Como rodar o teste, enviando o resultado do arquivo para o diretorio /logs - versionado com data e hora
pytest > logs/test_results_$(date +%Y%m%d_%H%M%S).log 2>&1


### 📄 Prompt 17
escreva a implementação real para fazer esses testes passarem, respeitando as restrições da especificação rt01_setup_project_structure.md. 
Sempre consulte o diretório /rules/global_rules.md antes


### 📄 Prompt 18
Sempre consulte o diretório /rules/global_rules.md antes.
E com base na  especificação rt02_configure_environment_variables.md, escreva os testes unitários (pytest) que garantirão que este contrato seja cumprido. Utilize mocks para isolar chamadas de rede.


### 📄 Prompt 19
Escreva a implementação real para fazer esses testes passarem, respeitando as restrições da especificação rt02_configure_environment_variables.md 
Lembre-se sempre consulte o diretório /rules/global_rules.md antes


### 📄 Prompt 20
rodei os teste com ytest > logs/test_results_$(date +%Y%m%d_%H%M%S).log 2>&1, e o @test_results_20260429_190241.log foi retornado, avalie o e me diga o que esta sendo apontado de erro e como corrigir para que os teste passem

### 📄 Prompt 21
Sempre consulte o  **rules/global_rules.md** antes de sugerir algo,
matenha as boas práticas conforme **rt01_setup_project_structure.md** e clean Architecture
com base na  especificação **rt03_extract_text_from_pdf.md**, escreva os testes unitários (pytest) que garantirão que este contrato seja cumprido. Utilize mocks para isolar chamadas de rede se necessario.
se necessario Separe por  Responsabilidades:
Os testes automatizados devem residir exclusivamente dentro do diretório tests/, tests/units e assim por diante


### 📄 Prompt 22
como rdar este teste com salvamento do resultado em um arquivo de log na pasta logs
se eu rodar este teste agora irá dar erro, sim ou não


### 📄 Prompt 23
utilize conventional commites para o que fizemos ate agora

### 📄 Prompt 24
Agora, escreva a implementação em rt03_extract_text_from_pdf.md, para fazer esses testes passarem. Lembre-se sempre consulte rules/global_rules.md antes de implementar algo matenhas as boas práticas conforme **** e clean Architecture com base na especificação rt03_extract_text_from_pdf.md

### 📄 Prompt 25


### 📄 Prompt


### 📄 Prompt


### 📄 Prompt


### 📄 Prompt


### 📄 Prompt



### 📄 Prompt


### 📄 Prompt


### 📄 Prompt