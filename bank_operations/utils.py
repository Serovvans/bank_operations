import os
import json

from typing import List, Dict


def load_operations() -> List[Dict]:
    """
    Загружает данные об операциях из файла operations.json
    :return: список словарей с информацией об операциях
    """
    file = os.path.join("data", "operations.json")
    operations = json.loads(file)

    return operations


def fill_omissions(operations: List[Dict]) -> List[Dict]:
    result = operations.copy()
    for item in result:
        if "from" not in item:
            item["from"] = ""

    return result
# Строковые представления номера счёта и карты
# Изменение формата даты
# Строковое представлене суммы операции