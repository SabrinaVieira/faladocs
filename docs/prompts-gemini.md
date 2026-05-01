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
utilize conventional commites para o que fizemos desde o ultimo commit

### 📄 Prompt 26
me explique como juntar tudo desenvolvido na atual branch na master sem apagar ela

### 📄 Prompt 27
como criar uma branch para rt04_chunk_text.md
git checkout -b feat/RT04-chunk-text-service

### 📄 Prompt 28
Com base no **rt04_chunk_text.md**, escreva os testes unitários (pytest) que garantirão que o contrato seja cumprido. Utilize mocks para isolar chamadas de rede se necessario. E explique os passos do seu raciocinio
Sempre consulte o  **rules/global_rules.md** antes de sugerir algo, e matenha as boas práticas conforme **rt01_setup_project_structure.md** e clean Architecture
Se necessario separe por  responsabilidades. Os testes automatizados devem residir exclusivamente dentro do diretório tests/, tests/units e assim por diante

### 📄 Prompt 29
o arquivo recem criado para atender **rt04_chunk_text.md**, possui o memso nome de arquivo de teste que deveria criado para atender rt03_extract_text_from_pdf.md
e ambos deveriam ser salvos em ser salvo em tests/unit/services/test_document_service.py

### 📄 Prompt 30
como rdar este teste com salvamento do resultado em um arquivo de log na pasta logs
se eu rodar este teste agora irá dar erro, sim ou não

pytest > logs/test_results_$(date +%Y%m%d_%H%M%S).log 2>&1


### 📄 Prompt 31
utilize conventional commites, e escreva um commit resumido para o que fizemos desde o ultimo commit nesta branch


### 📄 Prompt 32
Agora, escreva a implementação em **rt04_chunk_text.md**, para fazer esses testes passarem. E explique os passos do seu raciocinio
Sempre consulte o  **rules/global_rules.md** antes de sugerir algo, e matenha as boas práticas conforme **rt01_setup_project_structure.md** e clean Architecture

### 📄 Prompt 33
1 - utilize conventional commites, e escreva um commit curto para o que fizemos desde o ultimo commit nesta branch, a mensagem não deve ultrapassar 50 caracteres
2 me explique como juntar tudo desenvolvido na atual branch na master sem apagar ela

test(services): add unit tests for rt04 text chunking




### 📄 Prompt 34
Contexto e Objetivo: Estamos no desenvolvimento do MVP do FalaDocs. Sua tarefa é garantir a integridade do contrato **rt05_setup_supabase_client** através de testes unitários robustos.
DIRETRIZES CRÍTICAS DE ARQUITETURA (Prioridade Máxima):
Leitura Obrigatória: Antes de qualquer linha de código, você deve processar o arquivo **rules/global_rules.md** e o **rt01_setup_project_structure.md**. Suas sugestões devem ser 100% complacentes com esses documentos.

Localização 
Estrita: Você está proibido de sugerir a criação de arquivos fora da estrutura definida. Testes unitários devem residir exclusivamente em **tests/unit/**[contexto_especifico]/. 
Verifique a estrutura de pastas atual antes de propor o caminho.
Padrão de Projeto: Siga rigorosamente os princípios de Clean Architecture.
Separe os testes por contexto e responsabilidade (ex: domain, application, infrastructure).
Requisitos Técnicos:
Ferramental: Utilize pytest.Isolamento: Implemente mocks para todas as chamadas de rede ou dependências externas para garantir que o teste seja puramente unitário.

Entrega Esperada:
Raciocínio: Explique os passos lógicos e como a estrutura escolhida respeita a Clean Architecture.Caminho do Arquivo: Indique explicitamente o caminho completo (ex: tests/unit/services/test_validador.py) antes do bloco de código.
Código: Implementação dos testes seguindo as boas práticas de legibilidade e padrões do projeto.

### 📄 Prompt 35
o arquivo foi criado no diretório incorreto

### 📄 Prompt 36
como rdar este teste com salvamento do resultado em um arquivo de log na pasta logs
pytest > logs/test_results_test_supabase_client_$(date +%Y%m%d_%H%M%S).log 2>&1


### 📄 Prompt
Analise o **test_results_test_supabase_client_20260501_111418.log**, me explique porque o erro "ImportError: cannot import name 'SupabaseConnectionError' from 'src.core.exceptions' (/home/sabrina/Documentos/faladocs/src/core/exceptions.py)" ocorre

### 📄 Prompt
Analise o **test_results_test_supabase_client_20260501_111647.log** me explique porque o erro 'ModuleNotFoundError: No module named 'src.infrastructure' ocorre

### 📄 Prompt
Analise o test_results_test_supabase_client_20260501_112445.log me explique porque o erro 'ImportError: cannot import name 'get_supabase_client' from 'src.infrastructure.database' ocorre

### 📄 Prompt
(como rdar este teste com salvamento do resultado em um arquivo de log na pasta logs)
se eu rodar este teste agora irá dar erro, sim ou não

### 📄 Prompt
Utilize conventional commites, e escreva um commit curto  (com no máx 60 caracteres) para o que fizemos desde o ultimo commit nesta branch
test(infra): add unit tests for supabase client setup


### 📄 Prompt
Objetivo: Implementar o cliente Supabase no arquivo **rt05_setup_supabase_client** para garantir que os testes unitários recém-criados passem com sucesso

REGRAS DE OURO DE ARQUITETURA (Prioridade Absoluta):
Consulta Obrigatória: Antes de gerar qualquer código, processe os arquivos **rules/global_rules.md**, **rt01_setup_project_structure.md** e o escopo do projeto FalaDocs.
Clean Architecture: O cliente deve ser implementado como uma camada de Infrastructure ou External Service Adapter. Garanta a inversão de dependência se o contrato exigir.
Localização Precisa: Verifique a estrutura de diretórios do projeto. Você deve indicar o caminho completo onde o arquivo será criado/editado (ex: src/infrastructure/database/supabase_client.py) antes de exibir o código.
Padronização: Utilize as bibliotecas já definidas no projeto (Python, LangChain, Streamlit) conforme o setup do MVP.

Requisitos da Implementação:
A configuração deve ser resiliente e buscar credenciais via variáveis de ambiente (conforme boas práticas de segurança).
O código deve ser modular e fácil de ser "mockado" em futuros testes de integração.

Entrega Esperada:
Caminho do Arquivo: Informe o diretório exato seguindo o padrão rt01.
Raciocínio Técnico: Explique como a implementação satisfaz os requisitos do contrato e mantém a estrutura modular do FalaDocs.
Código-Fonte: Implementação completa, limpa e comentada em Python.


### 📄 Prompt
o arquivo foi criado no diretório incorreto

### 📄 Prompt
Utilize conventional commites, e escreva um commit curto  (com no máx 60 caracteres) para o que fizemos desde o ultimo commit nesta branch

### 📄 Prompt


### 📄 Prompt


### 📄 Prompt


### 📄 Prompt


### 📄 Prompt


### 📄 Prompt