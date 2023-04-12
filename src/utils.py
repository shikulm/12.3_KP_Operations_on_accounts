import os
import json
from datetime import datetime

FILE_OPERATIONS = "operations.json"

def load_operation(file_name: str = FILE_OPERATIONS) -> list:
    """
    Загрузка списка операций из файла
    :param file_name: Название входного файла
    :return: Словарь с импортироваными данными
    """
    full_file_name = os.path.join(os.path.dirname(__file__), "InputFiles", file_name)

    return json.load(open(full_file_name, "r", encoding="utf8"))

def format_date(date: datetime) -> str:
    """
    Преобразование даты в формат MM.DD.YYYY
    :param date: исходная дата, которую трбуется отформатировать
    :return: отформатированная дата
    """
    dt = datetime.strptime(date[:10], "%Y-%m-%d")

    return datetime.strftime(dt, "%d.%m.%Y")





