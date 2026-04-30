from pathlib import Path

# Define o diretório raiz do projeto com base na localização deste arquivo de teste.
# Path(__file__) -> /home/sabrina/Documentos/faladocs/tests/test_project_structure.py
# .parent -> /home/sabrina/Documentos/faladocs/tests
# .parent -> /home/sabrina/Documentos/faladocs
PROJECT_ROOT = Path(__file__).parent.parent


def test_project_core_directories_exist():
    """
    Garante que os diretórios principais do projeto (src, docs, tests) existem,
    conforme a especificação rt01_setup_project_structure.md.
    """
    required_dirs = ["src", "docs", "tests"]
    for dir_name in required_dirs:
        dir_path = PROJECT_ROOT / dir_name
        assert dir_path.exists(), f"O diretório '{dir_name}' não foi encontrado na raiz do projeto."
        assert dir_path.is_dir(), f"O caminho '{dir_name}' existe, mas não é um diretório."


def test_critical_project_files_exist():
    """
    Garante que arquivos críticos para a configuração e execução do projeto existem.
    """
    required_files = ["pyproject.toml", "requirements.txt", ".gitignore"]
    for file_name in required_files:
        file_path = PROJECT_ROOT / file_name
        assert file_path.exists(), f"O arquivo de configuração essencial '{file_name}' não foi encontrado."
        assert file_path.is_file(), f"O caminho '{file_name}' existe, mas não é um arquivo."