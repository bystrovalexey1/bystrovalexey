from unittest.mock import patch

import pytest

from src.external_api import get_amount


@pytest.fixture
def transaction_fix_rub():
    return {
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {"amount": "97853.86", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612",
    }


@pytest.fixture
def transaction_fix():
    return {
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {"amount": "97853.86", "currency": {"name": "евро", "code": "EUR"}},
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612",
    }


def test_get_amount_rub(transaction_fix_rub):
    assert get_amount(transaction_fix_rub) == 97853.86


@patch("requests.get")
def test_get_amount_mock(mock_get, transaction_fix):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 97853.86},
        "info": {"timestamp": 1729446844, "rate": 104.178889},
        "date": "2024-10-20",
        "result": 10194306.419162,
    }
    assert get_amount(transaction_fix) == 10194306.419162
