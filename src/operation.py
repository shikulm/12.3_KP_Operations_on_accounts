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




