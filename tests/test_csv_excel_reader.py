from typing import Any
from unittest.mock import mock_open, patch

import pandas as pd

from src.csv_excel_reader import transaction_read_csv, transaction_read_xlcx


@patch("builtins.open", new_callable=mock_open, read_data="amount;currency\n100;USD")
@patch("pandas.read_csv")
def test_get_data_from_csv(mock_read_csv: Any, mock_file: Any) -> None:
    mock_read_csv.return_value = pd.DataFrame({"amount": [100], "currency": ["USD"]})
    transactions = transaction_read_csv("data/transactions.csv")
    assert transactions == [{"amount": 100, "currency": "USD"}]


@patch("builtins.open", side_effect=FileNotFoundError)
def test_not_found_csv(mock_file: Any) -> None:
    transactions = transaction_read_csv("data/transactions.csv")
    assert transactions == []


@patch("builtins.open", new_callable=mock_open, read_data="")
@patch("pandas.read_csv")
def test_value_error_csv(mock_read_csv: Any, mock_file: Any) -> None:
    mock_read_csv.side_effect = ValueError
    transactions = transaction_read_csv("data/transactions.csv")
    assert transactions == []


@patch("builtins.open", new_callable=mock_open, read_data=b"\x3c\x80\x00\x00\x00")
@patch("pandas.read_excel")
def test_get_data_from_excel(mock_read_excel: Any, mock_file: Any) -> None:
    mock_read_excel.return_value = pd.DataFrame({"amount": [100], "currency": ["USD"]})
    transactions = transaction_read_xlcx("data/transactions.xlsx")
    assert transactions == [{"amount": 100, "currency": "USD"}]


@patch("builtins.open", side_effect=FileNotFoundError)
def test_not_found_excel(mock_file: Any) -> None:
    transactions = transaction_read_xlcx("data/transactions.xlsx")
    assert transactions == []
