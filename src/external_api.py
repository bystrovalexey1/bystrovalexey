import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_amount(transaction: dict) -> float:
    """Функция, которая выводить сумму операции в рублях, если валюта другая, то конвертирует через api"""
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return float(amount)
    else:
        response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={currency}&amount={amount}",
            headers={"apikey": f"{API_KEY}"},
        )
        result = response.json()
        return result["result"]
