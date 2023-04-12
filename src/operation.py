import datetime
from src.utils import *

class operation():
    """Класс содержит информацию по операции"""

    def __init__(self, date: datetime, description: str, from_acc: str, to_acc: str, amount: str, name_cur: str):
        self.date = date
        self.description = description
        self.from_acc = from_acc
        self.to_acc = to_acc
        self.amount = amount
        self.name_cur = name_cur


    def format_from_to(self, from_to_acc: str) -> str:
        """
        Форматирование строк "откуда" и "куда" для вывода на экран
        :param from_acc: исходная строка откуда или куда
        :return: отформтаированная для вывода строка
        """
        if from_to_acc is None:
            return ""

        if len(from_to_acc) < 16:
             # Если строка содержит меньше 16 символов, то возвращаем строку с вопросами
            return "?" * len(from_to_acc)

        if from_to_acc[:4].lower() == "счет":
            # Для счета выводим толко последние 4 цифры
            return "Счет **" + from_to_acc[-4:]
        return from_to_acc[:-16] + from_to_acc[-16: -12] + " " + from_to_acc[-12: -10] + "** **** " + from_to_acc[-4:]


    def __str__(self):
        return f"{format_date(self.date)} {self.description}\n" +\
            f"{self.format_from_to(self.from_acc)} -> {self.format_from_to(self.to_acc)}\n" +\
            f"{self.amount} {self.name_cur}"




