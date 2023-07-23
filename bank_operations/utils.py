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

# Строковые представления номера счёта и карты
# Изменение формата даты
# Строковое представлене суммы операции