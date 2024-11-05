import os

import pytest

from src.utils import file_opening


@pytest.fixture
def filename():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")


@pytest.fixture
def filename_empty():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations_empty.json")


def test_file_opening_empty(filename_empty):
    assert file_opening(filename_empty) == []


def test_file_opening(filename):
    assert file_opening(filename)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
