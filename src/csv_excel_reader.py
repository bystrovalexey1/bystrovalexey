from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
csv_file = BASE_DIR / "data" / "transactions.csv"
xlcx_file = BASE_DIR / "data" / "transactions_excel.xlsx"


def transaction_read_csv(csv_file: str) -> list[dict]:
    """Функция принимает на вход путь до файла csv и возвращает список словарей с транзакциями"""
    try:
        with open(csv_file, encoding="utf-8") as file:
            pd.read_csv(file)
    except ValueError:
        return []
    except FileNotFoundError:
        return []
    else:
        with open(csv_file, encoding="utf-8") as file:
            operations = pd.read_csv(file, delimiter=";")
            return operations.to_dict(orient="records")


def transaction_read_xlcx(xlcx_file: str) -> list[dict]:
    """Функция принимает на вход путь до файла excel и возвращает список словарей с транзакциями"""
    try:
        pd.read_excel(xlcx_file)
    except ValueError:
        return []
    except FileNotFoundError:
        return []
    else:
        operations = pd.read_excel(xlcx_file)
        return operations.to_dict(orient="records")
