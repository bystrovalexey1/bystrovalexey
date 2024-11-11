import os

from src.csv_excel_reader import transaction_read_csv, transaction_read_xlcx
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.search_transaction import search_transaction
from src.utils import file_opening
from src.widget import get_date, mask_account_card

json_file = file_opening(os.path.join(os.path.dirname(__file__), "data", "operations.json"))
csv_file = transaction_read_csv(os.path.join(os.path.dirname(__file__), "data", "transactions.csv"))
excel_file = transaction_read_xlcx(os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx"))


def hello() -> list[dict]:
    """Фукнкция приветствия"""
    while True:
        print(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:
                1. Получить информацию о транзакциях из JSON-файла
                2. Получить информацию о транзакциях из CSV-файла
                3. Получить информацию о транзакциях из XLSX-файла"""
        )

        user_choice = input("Введите цифру 1, 2 или 3: ")
        if user_choice == "1":
            transaction_file = json_file
            print("Вы выбрали JSON файл")
            return transaction_file
            break
        elif user_choice == "2":
            transaction_file = csv_file
            print("Вы выбрали CSV файл")
            return transaction_file
            break
        elif user_choice == "3":
            transaction_file = excel_file
            print("Вы выбрали XLSX файл")
            return transaction_file
            break
        else:
            print("Введено неверное значение")


def operation_choice(transactions: list[dict]) -> list[dict]:
    """Функция выбора статуса операции и фильтрации по этому статусу"""
    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:"
        )
        user_choice = input()
        if user_choice.upper() == "EXECUTED" or user_choice.upper() == "CANCELED" or user_choice.upper() == "PENDING":
            print(f"Операции отфильтрованы по статусу {user_choice}")
            filter_transaction_list = filter_by_state(transactions, user_choice.upper())
            return filter_transaction_list
            break
        else:
            print(f"Статус операции {user_choice} недоступен.")


def date_filter(filter_transaction_list: list[dict]) -> list[dict]:
    """Сортировка по дате"""
    while True:
        print("Отсортировать операции по дате? Да/Нет")
        user_choice_1 = input()
        if user_choice_1.lower() == "да":
            while True:
                print("Отсортировать по возрастанию или по убыванию?")
                user_choise_2 = input()
                if user_choise_2.lower() == "по возрастанию":
                    is_reverse = False
                    filter_transaction_list = sort_by_date(filter_transaction_list, is_reverse)
                    return filter_transaction_list
                    break
                elif user_choise_2.lower() == "по убыванию":
                    is_reverse = True
                    filter_transaction_list = sort_by_date(filter_transaction_list, is_reverse)
                    return filter_transaction_list
                    break
                else:
                    print("Некорректные данные повторите ввод")
            break
        elif user_choice_1.lower() == "нет":
            return filter_transaction_list
            break
        else:
            print("Некорректный ввод")


def rub_account(filter_transaction_list: list[dict]) -> list[dict]:
    """Фильтрация по рублевым транзакциям"""
    while True:
        print("Выводить только рублевые тразакции? Да/Нет")
        user_choice = input()
        if user_choice.lower() == "да":
            filter_transaction_list = filter_by_currency(filter_transaction_list, "RUB")
            return list(filter_transaction_list)
            break
        elif user_choice.lower() == "нет":
            return filter_transaction_list
            break
        else:
            print("Некорректный ввод")


def sort_by_subs(filter_transaction_list: list[dict]) -> list[dict]:
    """Фильтрация по строке"""
    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_choice_1 = input()
        if user_choice_1.lower() == "да":
            user_choice_2 = input("Введите слово: ")
            filter_transaction_list = search_transaction(filter_transaction_list, user_choice_2)
            return filter_transaction_list
            break
        elif user_choice_1.lower() == "нет":
            return filter_transaction_list
            break
        else:
            print("Некорректный ввод")


def final_res(filter_transaction_list: list[dict]) -> None:
    """Вычисление и вывод результатов по полученному списку транзакций"""
    print("Распечатываю итоговый список транзакций...")
    if len(filter_transaction_list) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(filter_transaction_list)}")
        for transaction in filter_transaction_list:
            description = transaction.get("description")
            date = get_date(transaction.get("date"))
            try:
                mask_from = mask_account_card(transaction["from"])
                print(f"{date} {description} {mask_from} -> ", end="")
            except KeyError:
                print(f"{date} ", end="")

            try:
                mask_to = mask_account_card(transaction["to"])
                amount = transaction["amount"]
            except KeyError:
                amount = transaction["operationAmount"]["amount"]
            try:
                currency = transaction["currency_name"]
            except KeyError:
                currency = transaction["operationAmount"]["currency"]["name"]
            print(f"{mask_to} Сумма: {amount} {currency}")


def main() -> None:
    """Возвращает список транзакций по выбранным условиям"""
    transaction_list = hello()
    filter_transaction_list = operation_choice(transaction_list)
    filter_transaction_list = date_filter(filter_transaction_list)
    filter_transaction_list = rub_account(filter_transaction_list)
    filter_transaction_list = sort_by_subs(filter_transaction_list)
    final_res(filter_transaction_list)


if __name__ == "__main__":
    main()
