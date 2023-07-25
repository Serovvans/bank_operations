from src.operation import Operation
from src.utils import format_date, card_number_to_string,\
    bank_account_to_string, format_operation_amount


def test_operation(test_data, test_string_operation):
    """
    Тестирует строковое представление об операции
    :param test_string_operation:
    :return:
    """
    operation = test_data[0]
    date = format_date(operation["date"])
    description = operation["description"]

    sender = list(operation["from"].split())
    sender = bank_account_to_string(operation["from"]) if sender[0] == "Счет"\
        else card_number_to_string(operation["from"])

    recipient = list(operation["to"].split())
    recipient = bank_account_to_string(operation["to"]) if recipient[0] == "Счет"\
        else card_number_to_string(operation["to"])

    amount = format_operation_amount(operation["operationAmount"])

    new_operation = Operation(date=date,
                              description=description,
                              sender=sender,
                              recipient=recipient,
                              amount=amount)

    assert str(new_operation) == test_string_operation
