from src.main import make_operation_object, get_five_last_operations


def test_make_operation_object(test_data, test_string_operation):
    new_operation = test_data[0]
    operation = make_operation_object(new_operation)

    assert str(operation) == test_string_operation


def test_get_five_last_operations(test_data, test_string_operation):
    new_operation = test_data[0]
    operation = make_operation_object(new_operation)

    lst_operations = get_five_last_operations("test_operations.json")
    assert [str(operation)] == list(map(str, lst_operations))
