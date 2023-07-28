from src.utils import load_operations, get_last_five_executed_operations


def test_load_operations(test_objects):
    assert load_operations("test_operations.json") == test_objects, "Данные считаны неверно"


def test_get_last_five_executed_operations(test_objects):
    operations = get_last_five_executed_operations(test_objects)
    assert all(operation.state == "EXECUTED" for operation in operations), "Отобраны невыполненные операции"
    assert len(operations) <= 5, "Отобрано излишнее количество операций"
