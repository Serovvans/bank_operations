from src.operation import Operation
from src.utils import *


def make_operation_object(operation: Dict) -> Operation:
    """
    Создаёт объект операции из словаря с информацией о ней
    :param operation: словарь с информацией об оперции
    :return: объект оперции
    """
    date = operation["date"]
    description = operation["description"]

    if operation["from"]:
        sender = list(operation["from"].split())
        sender = bank_account_to_string(operation["from"]) if sender[0] == "Счет" \
            else card_number_to_string(operation["from"])
    else:
        sender = ""

    recipient = list(operation["to"].split())
    recipient = bank_account_to_string(operation["to"]) if recipient[0] == "Счет" \
        else card_number_to_string(operation["to"])

    amount = format_operation_amount(operation["operationAmount"])

    new_operation = Operation(date=date,
                              description=description,
                              sender=sender,
                              recipient=recipient,
                              amount=amount)
    return new_operation


def get_five_last_operations(file_name: str) -> List[Operation]:
    """
    Возвращает 5 последних операций в виде объектов операций
    :param file_name: файл, где хранится информация об операциях
    :return: список из объектов 5 последних выполненных операций
    """
    all_operations = load_operations(file_name)
    all_operations = fill_omissions(all_operations)

    last_operations = get_last_five_executed_operations(all_operations)
    return list(map(make_operation_object, last_operations))


def string_last_operations(file_name="operations.json") -> str:
    """
    Склеивает строковые представления 5 последних операций
    :param file_name: файл, где хранится информация об операциях
    :return: склеенные с пропуском строки строковые представления 5 последних выполненных операций
    """
    last_operations = get_five_last_operations(file_name)

    return "\n\n".join(map(str, last_operations))


if __name__ == "__main__":
    print(string_last_operations())
