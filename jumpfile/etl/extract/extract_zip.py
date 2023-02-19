from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List
from zipfile import ZipFile
from extract_http import get_request

from jumpfile.repository.file_repository import FileRepository


@dataclass
class ZipResponse:
    zip_name: Optional[str]
    files_name: Optional[List]


def download_zip(path, destiny, file_name):
    response = get_request(path, )
    local_path = f"{destiny}{file_name}"

    if response:

        exist = Path(local_path).exists()

        if not exist:
            with open(local_path, "wb") as f:
                f.write(response.content)
                return True

    return False


def read_name_files(path, zip_name, fil_names):
    full_path = path + zip_name
    with ZipFile(full_path, mode="r") as f:
        temp_file = f.namelist()
        if fil_names:
            files_name = [f.extract(file) for file in temp_file if file in fil_names]
        else:
            files_name = [f.extract(file) for file in temp_file]

    return ZipResponse(zip_name=zip_name, files_name=files_name)


def filter_files(files, fil_names):
    return [file for file in files if file in fil_names]


def teste():
    path = "https://assets.datacamp.com/production/repositories/5899/datasets/19d6cf619d6a771314f0eb489262a31f89c424c2/ppr-all.zip"
    file_repository = FileRepository("apontamentos")
    zip_name = "ppr-all.zip"

    download = download_zip(path=path, destiny=file_repository.get_path(), file_name=zip_name)

    file_names = read_name_files(path=file_repository.get_path(), zip_name=zip_name,
                                 fil_names=["teste.txt", "ppr-all.csv"])

    print(download)
    print(file_names)


teste()
