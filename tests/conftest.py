import pytest
import os
import json


@pytest.fixture(scope="session")
def test_data():
    """
    Фикстура с 2 примерами операций
    :return:
    """
    return [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
        },
        {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
        }
    ]


@pytest.fixture(scope="session")
def test_string_operation():
    """
    Фикстура примера текстового вывода операции
    :return:
    """
    return "26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб."


@pytest.fixture(scope="session", autouse=True)
def create_file(test_data):
    """
    Создаёт файл с примерами данных и удаляет его после выполнения тестов
    :param test_data: Пример данных об операциях
    :return:
    """
    file = os.path.join("data", "test_operations.json")
    with open(file, "w") as f:
        json.dump(test_data, f)

    yield
    os.remove(file)
