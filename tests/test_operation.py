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

def test_format_from_to(operat_1):
    oper = operation(*operat_1)
    assert oper.format_from_to("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert oper.format_from_to("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert oper.format_from_to("Счет 75106830613657916952") == "Счет **6952"
    assert oper.format_from_to("57916") == "?????"
    assert oper.format_from_to("57916yf") == "???????"
    assert oper.format_from_to(25) == "???????"


def test_format_from_to_TypeError(operat_1):
    oper = operation(*operat_1)
    with pytest.raises(TypeError):
        oper.format_from_to(25)


def test_str(operat_1):
    oper = operation(*operat_1)
    assert str(oper) == "26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n8221.37 руб."