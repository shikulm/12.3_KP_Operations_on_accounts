import os
import json

FILE_OPERATIONS = "operations.json"

def load_operation(file_name: str = FILE_OPERATIONS) -> list:
    """
    Загрузка списка операций из файла
    :param file_name: Название входного файла
    :return: Словарь с импортироваными данными
    """
    full_file_name = os.path.join(os.path.dirname(__file__), "InputFiles", file_name)

    return json.load(open(full_file_name, "r", encoding="utf8"))


op = load_operation(FILE_OPERATIONS)
print(op)

# op2 =load_operation("empty_file.json")
# print(op2)


