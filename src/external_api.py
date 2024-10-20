from utils import file_opening
from dotenv import load_dotenv
import requests
import os


load_dotenv()
API_KEY = os.getenv("API_KEY")
def get_amount(transaction: dict) -> float:
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    else:
        response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={currency}&amount={amount}",
            headers={"apikey": f"{API_KEY}"}
        )
        result = response.json()
        return result["result"]


if __name__ == "__main__":
    transaction_example = {
    "id": 667307132,
    "state": "EXECUTED",
    "date": "2019-07-13T18:51:29.313309",
    "operationAmount": {
      "amount": "97853.86",
      "currency": {
        "name": "руб.",
        "code": "EUR"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 1308795367077170",
    "to": "Счет 96527012349577388612"
  }
    print(get_amount(transaction_example))