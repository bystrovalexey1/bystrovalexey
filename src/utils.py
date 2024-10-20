import json


def file_opening(filename: str) -> list[dict]:
    """ Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях """
    empty_list_of_transaction = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            try:
                transactions = json.load(file)
                if transactions == 0 or type(transactions) is not list:
                    return empty_list_of_transaction
                else:
                    return transactions
            except json.JSONDecodeError:
                print("Invalid JSon data")
                return empty_list_of_transaction
    except FileNotFoundError:
        return []
