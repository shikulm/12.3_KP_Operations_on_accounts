from src.main import *
from src.operation import *
input_data = [
    { "id": 441945886, "state": "EXECUTED", "date": "2019-07-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"} },
        "description": "Перевод организации", "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"  },
    {"id": 41428829,"state": "EXECUTED", "date": "2019-08-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD" } },
        "description": "Перевод организации", "from": "MasterCard 7158300734726758", "to": "Счет 35383033474447895560" },
    { "id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD" } },
        "description": "Перевод организации",  "from": "Счет 75106830613657916952",  "to": "Счет 11776614605963066702" },
    { "id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689",
        "operationAmount": { "amount": "67314.70",  "currency": {"name": "руб.", "code": "RUB" } },
        "description": "Перевод организации",  "from": "Visa Platinum 1246377376343588",  "to": "Счет 14211924144426031657"}
]

output_data = [operation("2019-08-03T18:35:29.512364", "Перевод организации", \
                         "MasterCard 7158300734726758", "Счет 35383033474447895560",  "8221.37", "USD"),
                operation("2019-07-26T10:50:58.294041", "Перевод организации", \
                         "Maestro 1596837868705199", "Счет 64686473678894779589",  "31957.58", "руб.")
]

def test_select_executed_operations():
    # assert [str(el) for el in select_executed_operations(input_data)] == [str(el) for el in output_data]
    assert str(select_executed_operations(input_data, 2)[0]) == str(output_data[0])
    assert str(select_executed_operations(input_data, 2)[1]) == str(output_data[1])
    assert len(select_executed_operations(input_data, 2)) == 2
    assert len(select_executed_operations(input_data, 3)) == 3
    assert len(select_executed_operations(input_data, 5)) == 3
