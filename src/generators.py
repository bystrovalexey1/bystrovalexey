from typing import Generator, Iterator, List


def filter_by_currency(transaction_list: List[dict], currency_code: str = "USD") -> Iterator:
    """Функция для фильтрации списка операций по валюте"""
    try:
        for transaction in transaction_list:
            if transaction["operationAmount"]["currency"]["code"] == currency_code:
                yield transaction
    except KeyError:
        for transaction in transaction_list:
            if transaction["currency_code"] == currency_code:
                yield transaction

def transaction_descriptions(transaction_list: List[dict]) -> Iterator:
    """Функция для последовательного вывода описания банковских операций"""
    for transaction in transaction_list:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator:
    """Функция для генерации номера карты"""
    for number in range(start, end + 1):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number

        format_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield format_card_number
