import os
import json

FILE_OPERATIONS = "operations.json"

def load_operation(file_name: str) -> list:
    """
    Загрузка списка операций из файла
    :param file_name: Название входного файла
    :return: Словарь с импортироваными данными
    """
    full_file_name = os.path.join("InputFile", file_name)

    return json.load(open(full_file_name, "r", encoding="utf8"))


op = load_operation(FILE_OPERATIONS)
print(op)


