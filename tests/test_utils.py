import pytest

from src.utils import *
def test_load_operation():
    assert load_operation("operations.json")[0] ==\
        {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',\
        'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},\
        'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}

    assert load_operation()[0] == \
           {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', \
            'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, \
            'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}


def test_load_operation_FileNotFound():
    with pytest.raises(FileNotFoundError):
        load_operation("opera.json")

def test_load_operation_TypeError():
    with pytest.raises(TypeError):
        load_operation(1)

def test_load_operation_JSONDecodeError():
    with pytest.raises(json.decoder.JSONDecodeError):
        load_operation("empty_file.json")

def test_format_date():
    assert format_date("2019-08-26T10:50:58.294041") == "26.08.2019"
    assert format_date("1956-11-13T10:50:58.294041") == "13.11.1956"


def test_format_date_ValueError():
    with pytest.raises(ValueError):
        format_date("2019-26-08T10:50:58.294041")

def test_format_date_TypeError():
    with pytest.raises(TypeError):
        format_date(25)
        format_date()