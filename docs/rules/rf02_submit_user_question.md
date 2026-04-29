[METADADOS]
Arquivo de Destino: `src/app.py`
Linguagem/Ambiente: Python, rodando estritamente em ambiente virtual (venv). Não assuma conteinerização ou Docker sob nenhuma hipótese.

[ASSINATURA E INTERFACE]
Entradas: Texto (`str`) inserido pelo usuário em um campo de entrada.
Saídas: A string da pergunta do usuário, que será usada para iniciar o pipeline de RAG.
Tipagem: Exige Type Hints rigorosos em todas as assinaturas.

[REGRAS DE NEGÓCIO E COMPORTAMENTO]
1. A interface deve renderizar um componente `streamlit.text_input` para o usuário digitar a pergunta.
2. Um botão `streamlit.button` com o label "Enviar" deve ser exibido para submeter a pergunta.
3. A lógica deve ser contida em uma estrutura condicional (`if prompt := st.chat_input(...)` ou `if st.button(...)`) para garantir que o pipeline de resposta só seja acionado após a submissão do usuário.
4. O campo de entrada de texto e o botão só devem ser exibidos após o documento PDF ter sido processado com sucesso.

[TRATAMENTO DE ERROS E SEGURANÇA]
- A aplicação deve verificar se a string da pergunta não está vazia ou contém apenas espaços em branco antes de prosseguir com a busca de similaridade.

[RESTRIÇÕES ARQUITETURAIS]
- Este arquivo é responsável pela orquestração da UI e pela captura de eventos do usuário.
- Ao receber a pergunta, ele deve delegar a tarefa de busca e geração de resposta para os serviços apropriados da camada de aplicação, sem implementar essa lógica diretamente.