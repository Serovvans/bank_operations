import os
import json

from typing import List, Dict


def load_operations() -> List[Dict]:
    """
    Загружает данные об операциях из файла operations.json
    :return: список словарей с информацией об операциях
    """
    file = os.path.join("data", "operations.json")
    with open(file) as f:
        operations = json.load(f)

    return operations


def fill_omissions(operations: List[Dict]) -> List[Dict]:
    """
    Если отправитель оперции пропещен, в словарь добавляется вместо него пустая строка
    :param operations: список словарей с описанием операций
    :return: список словарей с описанием операций, в которых заполнили пропуск отправителя
    """
    result = operations.copy()
    for item in result:
        if "from" not in item:
            item["from"] = ""

    return result
# Строковые представления номера счёта и карты
# Изменение формата даты
# Строковое представлене суммы операции