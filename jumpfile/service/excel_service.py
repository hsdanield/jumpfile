from pathlib import Path
import pandas as pd
import datetime

from jumpfile.repository.file_repository import FileRepository


def exist_path(path):
    return Path(path).exists()


def create_path_if_not_exist(full_path):
    try:
        if not exist_path(full_path):
            Path(full_path).mkdir()
            print(f"{full_path} criado com sucesso...")

            return True
    except Exception as e:
        print(f"Erro ao criar diretorio {full_path} ... Erro: {e}")

    return False


def create_paths(paths):
    [create_path_if_not_exist(path) for path in paths]


def save_excel(name):
    data = []

    file_repository = FileRepository(name=name)
    path_files = file_repository.get_path_files()
    path_destiny = file_repository.get_path_destiny()
    filters = file_repository.get_filters()
    root_path = file_repository.get_path()

    # Criando Diretorios caso não existir
    create_paths(path_destiny)

    for path in path_files:
        for key, values in filters.items():
            for value in values:
                path_file = map_destiny(value, path.name, root_path)
                df_book = pd.read_excel(path)
                df_new_book = df_book.loc[df_book[key] == value]
                df_new_book.to_excel(path_file, index=None)


def map_destiny(value, name, root_path):
    file_name = f"{value}-{name}"
    new_path = f"{root_path}\\{value}\\{file_name}"
    return new_path
