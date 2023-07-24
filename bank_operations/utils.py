import os
import json

from typing import List, Dict


def load_operations(file_name: str) -> List[Dict]:
    """
    Загружает данные об операциях из файла operations.json
    file_name: имя файла для загрузки
    :return: список словарей с информацией об операциях
    """
    file = os.path.join("data", file_name)
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


def card_number_to_string(card_number: str) -> str:
    """
    Переводит номер карты в шаблонное строковое представление
    :param card_number: номер карты отправителя
    :return: Строковое представление номера карты по шаблону XXXX XX** **** XXXX
    """
    if not card_number:
        return ""

    return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]


def bank_account_to_string(bank_account: str) -> str:
    """
    Переводит номер счета получателя в шаблонное строковое представление
    :param bank_account: номер счета получателя
    :return: Номер счета в формате **XXXX
    """
    if not bank_account:
        return ""

    return "**" + bank_account[-4:]
# Строковые представления номера счёта и карты
# Изменение формата даты
# Строковое представлене суммы операции
# Получение последних 5 выполненных операций