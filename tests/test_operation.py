import pytest
from src.operation import *

@pytest.fixture
def operat_1():
    return ["2019-08-26T10:50:58.294041", "Перевод организации", "Maestro 1596837868705199", "Счет 64686473678894779589", "8221.37", "руб."]

def test_init_operation(operat_1):
    """Проверка __init__() для класса operation"""
    # oper = operation(date="2019-08-26T10:50:58.294041", description="Перевод организации",\
    #                  from_acc="Maestro 1596837868705199", to_acc="Счет 64686473678894779589",\
    #                  amount="8221.37", name_cur="руб.")

    oper = operation(*operat_1)
    assert oper.date == "2019-08-26T10:50:58.294041"
    assert oper.description == "Перевод организации"
    assert oper.from_acc == "Maestro 1596837868705199"
    assert oper.to_acc == "Счет 64686473678894779589"
    assert oper.amount == "8221.37"
    assert oper.name_cur == "руб."

