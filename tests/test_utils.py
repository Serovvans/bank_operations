from bank_operations.utils import load_operations, fill_omissions, card_number_to_string, \
    bank_account_to_string


def test_load_operations(test_data):
    assert load_operations("test_operations.json") == test_data


def test_fill_omissions():
    assert fill_omissions([{"to": "president"}])[0].get("from") == ""
    assert fill_omissions([{"to": "", "from": "someone"}])[0].get("from") == "someone"
    assert len(fill_omissions([{"to": ""}, {"from": "someone", "to": ""}])) == 2


def test_card_number_to_string():
    assert card_number_to_string("1596837868705199") == "1596 83** **** 5199"
    assert card_number_to_string("") == ""


def test_bank_account_to_string():
    assert bank_account_to_string("64686473678894779589") == "**9589"
    assert bank_account_to_string("") == ""
