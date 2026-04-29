
# Regras Globais do Projeto FalaDocs

1. **Ambiente:** O projeto utiliza estritamente um ambiente virtual Python (`venv`). Nunca sugira comandos, scripts ou arquiteturas baseadas em Docker.
2. **Padrão de Código:** Todo código Python deve estar conforme a PEP8 (usando Black/Ruff).
3. **Testes:** Todo novo código deve vir acompanhado de testes unitários usando `pytest` com dependências de I/O mockadas.
4. **Segurança:** Logs de erro nunca devem expor stack traces sensíveis ou chaves de API, expondo apenas tipagens genéricas.
5. **Clean Architecture:** Use Clean Architecture: separe lógica de negócio de frameworks.
6. **Commits:**  seguindo Conventional Commits (ex: feat:, fix:, docs:).
7. **Documentação:** Sempre inclua tratamento de erros (Try/Catch) e logs.
8. **Dependencias** Sempre verifique a existencia de pacotes no requirements.txt, caso ao pacote não exista, adicione os ao documento