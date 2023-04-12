import datetime

class operation():
    """Класс содержит информацию по операции"""

    def __init__(self, date: datetime, description: str, from_acc: str, to_acc: str, amount: str, name_cur: str):
        self.date = date
        self.description = description
        self.from_acc = from_acc
        self.to_acc = to_acc
        self.amount = amount
        self.name_cur = name_cur


    def format_from(self, from_acc: str) -> str:
        """
        Форматирование строки "откуда" для вывода на экран
        :param from_acc: исходная строка откуда
        :return: отформтаированная для вывода строка
        """
        return from_acc[:-16] + from_acc[-16: -12] + " " + from_acc[-12: -10] + "** **** " + from_acc[-4:]



# oper = operation(date="2019-08-26T10:50:58.294041", description="Перевод организации",\
#                  from_acc="Maestro 1596837868705199", to_acc="Счет 64686473678894779589",\
#                  amount="8221.37", name_cur="руб.")
#
# print(oper.format_from("Maestro 1596837868705199"))

