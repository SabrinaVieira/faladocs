[METADADOS]
Arquivo de Destino: N/A (Estrutura do projeto)
Linguagem/Ambiente: Python, rodando estritamente em ambiente virtual (venv). Não assuma conteinerização ou Docker sob nenhuma hipótese.

[ASSINATURA E INTERFACE]
Entradas: Comandos do shell (`mkdir`, `python -m venv`, `pip install`).
Saídas: Uma estrutura de diretórios e um ambiente virtual ativado com as dependências instaladas.
Tipagem: N/A.

[REGRAS DE NEGÓCIO E COMPORTAMENTO]
1. Deve ser criada a seguinte estrutura de diretórios na raiz do projeto: `docs/`, `src/`, `tests/`.
2. Um ambiente virtual Python deve ser criado na pasta `.venv` na raiz do projeto.
3. Todas as dependências listadas no arquivo `requirements.txt` devem ser instaladas no ambiente virtual.

[TRATAMENTO DE ERROS E SEGURANÇA]
- A execução deve ser interrompida se o comando `pip install` falhar, indicando um problema com as dependências ou com o ambiente.

[RESTRIÇÕES ARQUITETURAIS]
- O código-fonte da aplicação deve residir exclusivamente dentro do diretório `src/`.
- Os testes automatizados devem residir exclusivamente dentro do diretório `tests/`.
- A documentação do projeto, incluindo estes contratos, deve residir em `docs/`.