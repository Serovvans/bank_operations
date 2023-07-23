from bank_operations.utils import fill_omissions


def test_fill_omissions():
    assert fill_omissions([{"to": "president"}])[0].get("from") == ""
    assert fill_omissions([{"to": "", "from": "someone"}])[0].get("from") == "someone"
    assert len(fill_omissions([{"to": ""}, {"from": "someone", "to": ""}])) == 2
