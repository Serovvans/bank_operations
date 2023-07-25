from bank_operations.utils import load_operations, fill_omissions, card_number_to_string, \
    bank_account_to_string, format_date, format_operation_amount, get_last_five_executed_operations


def test_load_operations(test_data):
    assert load_operations("test_operations.json") == test_data


def test_fill_omissions():
    assert fill_omissions([{"to": "president"}])[0].get("from") == ""
    assert fill_omissions([{"to": "", "from": "someone"}])[0].get("from") == "someone"
    assert len(fill_omissions([{"to": ""}, {"from": "someone", "to": ""}])) == 2


def test_card_number_to_string():
    assert card_number_to_string("Visa Classic 1596837868705199") == "Visa Classic 1596 83** **** 5199"
    assert card_number_to_string("") == ""


def test_bank_account_to_string():
    assert bank_account_to_string("Счет 64686473678894779589") == "Счет **9589"
    assert bank_account_to_string("") == ""


def test_format_date():
    assert format_date("2019-08-26T10:50:58.294041").get("year") == 2019
    assert format_date("2019-08-26T10:50:58.294041").get("month") == 8
    assert format_date("2019-08-26T10:50:58.294041").get("day") == 26
    assert format_date("2019-08-26T10:50:58.294041").get("time") == 10*60*60 + 50*60 + 58.294041


def test_format_operation_amount():
    amount = {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    }
    assert format_operation_amount(amount) == "31957.58 руб."


def test_get_last_five_executed_operations(test_data):
    operations = get_last_five_executed_operations(test_data)
    assert all(operation["state"] == "EXECUTED" for operation in operations)
    assert len(operations) <= 5
