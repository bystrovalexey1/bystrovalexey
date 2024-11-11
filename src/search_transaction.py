import collections
import re


def search_transaction(transaction_list: list[dict], substr: str) -> list[dict]:
    """Функция, которая возвращает список операций, у которых есть в описании подстрока"""
    pattern = rf"{substr}"
    transactions = []
    for transaction in transaction_list:
        for el in transaction.values():
            res = re.findall(pattern, str(el), flags=re.IGNORECASE)
            if res:
                transactions.append(transaction)
    return transactions


def search_transaction_cathegory(transaction_list: list[dict], cathegory_list: list) -> dict:
    """Функция, которая возвращает количество операций в каждой категории"""
    cathegory_counter = collections.Counter()
    for transaction in transaction_list:
        description = transaction.get("description", "").lower()
        for cathegory in cathegory_list:
            if cathegory.lower() in description:
                cathegory_counter[cathegory] += 1
    return dict(cathegory_counter)
