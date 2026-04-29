[METADADOS]
Arquivo de Destino: `src/app.py`
Linguagem/Ambiente: Python, rodando estritamente em ambiente virtual (venv). Não assuma conteinerização ou Docker sob nenhuma hipótese.

[ASSINATURA E INTERFACE]
Entradas: Ação do usuário de selecionar um arquivo no navegador.
Saídas: Um objeto `streamlit.runtime.uploaded_file_manager.UploadedFile` que representa o arquivo enviado.
Tipagem: Exige Type Hints rigorosos em todas as assinaturas.

[REGRAS DE NEGÓCIO E COMPORTAMENTO]
1. A interface deve exibir um componente `streamlit.file_uploader`.
2. O componente deve ser configurado com o parâmetro `type=['pdf']` para restringir a seleção de arquivos apenas ao formato PDF.
3. Um label claro, como "Faça o upload de um documento PDF", deve ser associado ao componente.

[TRATAMENTO DE ERROS E SEGURANÇA]
- A lógica subsequente deve verificar se o objeto retornado pelo `file_uploader` não é `None` antes de tentar qualquer processamento.
- Nenhuma mensagem de erro customizada é necessária para seleção de tipo de arquivo inválido, pois o componente Streamlit já gerencia essa validação nativamente.

[RESTRIÇÕES ARQUITETURAIS]
- Toda a lógica de interface de usuário (UI) deve ser contida em arquivos que utilizam a biblioteca Streamlit.
- Este arquivo não deve conter lógica de extração de texto, chunking ou comunicação com banco de dados. Sua responsabilidade é apenas capturar a entrada do usuário e delegar o processamento.
