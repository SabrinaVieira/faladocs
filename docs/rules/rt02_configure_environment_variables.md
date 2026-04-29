[METADADOS]
Arquivo de Destino: `src/core/config.py`
Linguagem/Ambiente: Python, rodando estritamente em ambiente virtual (venv). Não assuma conteinerização ou Docker sob nenhuma hipótese.

[ASSINATURA E INTERFACE]
Entradas: Um arquivo `.env` na raiz do projeto contendo as variáveis `GOOGLE_API_KEY`, `SUPABASE_URL`, e `SUPABASE_KEY`.
Saídas: Uma função ou objeto que fornece acesso seguro às variáveis de ambiente carregadas.
Tipagem: Exige Type Hints rigorosos em todas as assinaturas. Exemplo: `def get_settings() -> AppSettings:`.

[REGRAS DE NEGÓCIO E COMPORTAMENTO]
1. O módulo deve utilizar a biblioteca `python-dotenv` para carregar variáveis de um arquivo `.env`.
2. As chaves de API e credenciais NUNCA devem ser codificadas diretamente no código-fonte.
3. Deve ser implementada uma classe de configuração (ex: usando `pydantic_settings.BaseSettings`) para validar e prover acesso tipado às variáveis.

[TRATAMENTO DE ERROS E SEGURANÇA]
- Se uma variável de ambiente essencial não for encontrada durante a inicialização, o sistema deve lançar uma exceção `KeyError` ou `ValueError` com uma mensagem clara, como "Erro: A variável de ambiente 'SUPABASE_URL' não foi definida.", interrompendo a execução.
- O arquivo `.env` deve ser incluído no `.gitignore` para prevenir o versionamento de segredos.

[RESTRIÇÕES ARQUITETURAIS]
- Este módulo é a única fonte de verdade para configurações e segredos. Nenhum outro módulo deve tentar ler arquivos `.env` ou variáveis de ambiente diretamente.