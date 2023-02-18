from pathlib import Path

from jumpfile.configs.config import settings


class FileRepository:

    def __init__(self, name):
        self.__name = settings.pathfiles.excel[name]["name"]
        self.__path = settings.pathfiles.excel[name]["path"]
        self.__description = settings.pathfiles.excel[name]["description"]
        self.__prefix = settings.pathfiles.excel[name]["prefix"]
        self.__filters = settings.pathfiles.excel[name]["filters"]

    def validation_exist_path(self):
        return Path(self.__path).exists()

    def get_path(self):
        return self.__path

    def get_path_files(self):
        files_prefix = Path(self.__path).rglob(f"*{self.__prefix}")
        path_files = [path for path in files_prefix]
        return path_files

    def get_filters(self):
        return self.__filters

    def get_path_destiny(self):
        path_destiny = []
        for key, values in self.__filters.items():
            path_destiny = [f"{self.__path}{value}" for value in values]
        return path_destiny
