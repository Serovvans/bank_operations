import os
import json

from typing import List
from src.operation import Operation


def load_operations(file_name: str) -> List[Operation]:
    """
    Загружает данные об операциях из файла operations.json
    file_name: имя файла для загрузки
    :return: список словарей с информацией об операциях
    """
    file = os.path.join("data", file_name)
    try:
        with open(file, encoding="utf8") as f:
            operations = json.load(f)
    except FileNotFoundError:
        print("Отсутствует файл с данными об операциях")
    except json.JSONDecodeError:
        print("Не удаётся декодировать файл")

    return [Operation(item.get("id"), item.get("date"),  item.get("description"), item.get("from", ""),
                      item.get("to"), item.get("operationAmount"), item.get("state")) for item in operations]


def get_last_five_executed_operations(operations: List[Operation]) -> List[Operation]:
    """
    Возвращает 5 последних выполненнх операций
    :param operations: все операции
    :return: 5 последних выполненных операций
    """
    executed_operations = [item for item in operations if item.state == "EXECUTED"]

    sorted_operations = list(sorted(executed_operations,
                                    key=lambda x: [x.get_date().year,
                                                   x.get_date().month,
                                                   x.get_date().day,
                                                   x.get_date().hour * 60 * 60 + x.get_date().minute * 60 +
                                                   x.get_date().second
                                                   ]
                                    )
                             )
    return (sorted_operations[-5:])[::-1]


def print_last_executed_operations(filename: str) -> None:
    """
    Выводит на экран информацию о 5 последних выполненных операциях
    :param filename:
    :return:
    """
    operations = load_operations(filename)

    print("\n\n".join(map(str, get_last_five_executed_operations(operations))))
