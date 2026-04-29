[METADADOS]
Arquivo de Destino: `src/adapters/database/supabase_client.py`
Linguagem/Ambiente: Python, rodando estritamente em ambiente virtual (venv). Não assuma conteinerização ou Docker sob nenhuma hipótese.

[ASSINATURA E INTERFACE]
Entradas: Nenhuma (as credenciais são obtidas do módulo de configuração).
Saídas: Uma função `get_supabase_client` que retorna uma instância do cliente Supabase (`supabase.Client`).
Tipagem: Exige Type Hints rigorosos em todas as assinaturas. `from supabase import Client; def get_supabase_client() -> Client:`.

[REGRAS DE NEGÓCIO E COMPORTAMENTO]
1. A função deve importar as credenciais (`SUPABASE_URL`, `SUPABASE_KEY`) do módulo de configuração (`src/core/config.py`).
2. A função deve utilizar `supabase.create_client(url, key)` para instanciar e retornar o cliente.
3. Para otimização, a instância do cliente pode ser armazenada em cache (ex: usando `functools.lru_cache(maxsize=1)`) para evitar a recriação em chamadas subsequentes.

[TRATAMENTO DE ERROS E SEGURANÇA]
- A validação das credenciais é de responsabilidade do módulo de configuração (RT02).
- Falhas de conexão reais ocorrerão durante as operações (leitura/escrita) e devem ser tratadas nos serviços que utilizam este cliente, não na função de criação.

[RESTRIÇÕES ARQUITETURAIS]
- Este módulo atua como um Adaptador na Clean Architecture. Ele é o único ponto do sistema que deve ter conhecimento direto sobre a biblioteca `supabase`.
- Todos os outros serviços que precisam interagir com o Supabase devem fazê-lo obtendo a instância do cliente através desta função.