from src.operation import Operation


def test_card_number_to_string():
    assert Operation.card_number_to_string("Visa Classic 1596837868705199") == "Visa Classic 1596 83** **** 5199",\
        "Неверно замаскирован номер карты"
    assert Operation.card_number_to_string("") == "", "Замаскированный номер пустой строки должен быть пустой строкой"


def test_bank_account_to_string():
    assert Operation.bank_account_to_string("Счет 64686473678894779589") == "Счет **9589", \
        "Неверно замаскирован номер счета"
    assert Operation.bank_account_to_string("") == "", "Замаскированный номер счета из пустой строки должен быть " \
                                                       "пустой строкой"


def test_format_date(test_objects):
    operation = test_objects[0]
    assert operation.get_date().year == 2019, "Неверно получен год из строковой даты"
    assert operation.get_date().month == 8, "Неверно получен месяц из строковой даты"
    assert operation.get_date().day == 26, "Неверно получен день из строковой даты"
    assert operation.get_date().hour == 10, "Неверно получен час из строковой даты"


def test_format_operation_amount(test_objects):
    operation = test_objects[0]
    assert operation.get_amount() == "31957.58 руб.", "Сумма операции неверно представлена в виде строки"


def test_get_sender(test_objects):
    assert test_objects[0].get_sender() == "", "Пропуск отправителя должен отображаться пустой строкой"
    assert test_objects[1].get_sender() == "Visa Platinum 1246 37** **** 3588", "Неверно получна замаскированная " \
                                                                                "карта отправителя"
    assert test_objects[2].get_sender() == "Счет **1657", "Неверно получен замаскированный номер счета отправителя"


def test_get_recipient(test_objects):
    assert test_objects[0].get_recipient() == "Счет **9589", "Неверно получен замаскированнй номер счета получателя"
    assert test_objects[2].get_recipient() == "Maestro 3806 65** **** 3662", "Неверно получена замаскированная карта " \
                                                                             "получателя"


def test_string_view_operation(test_string_operation, test_objects):
    assert str(test_objects[0]) == test_string_operation, "Операция неверно представлена в виде строки"
