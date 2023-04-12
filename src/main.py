from src.operation import *
from src.utils import *
def select_executed_operations(lst_operations_in: list, cnt_select: int = 5) -> list:
    """
    Функция формирует список объектов класса operation
    из списка словарей с выполненными операциями
    :param lst_operations_in: список операций, загруженный из файла json
    :param cnt_select: количество выбираемых элементов
    :return: список объектов класса operation
    """

    # ёСписок с результирующим набором данных
    lst_operations_out = []

    # Выбираем из списка данные, которые могут быть занесены в результирующий набор

    opers = [(el.get('date'), el.get('description'), el.get('from'), el.get('to'), el.get('operationAmount').get('amount'), \
            el.get('operationAmount').get('currency').get('name')) \
             for el in lst_operations_in if el.get('state') == 'EXECUTED']
    # Сортируем список по первой колонке с датой
    opers.sort(reverse=True)

    # Определяем сколько элменетов надо выбрать из cписка
    if cnt_select > len(opers):
        cnt_select = len(opers)

    for i in range(cnt_select):
        # print(opers[i])
        lst_operations_out.append(operation(*opers[i]))

    return lst_operations_out


if __name__ == '__main__':
    op_in = load_operation()
    [print(f"{el}\n") for el in select_executed_operations(op_in)]
