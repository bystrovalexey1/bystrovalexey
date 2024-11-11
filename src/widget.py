from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_info: str) -> str:
    """Функция, которая маскирует и номер карты, и номер счета"""
    split_card_or_account_info = card_or_account_info.split(" ")
    hidden_account_or_card_number = ""
    if split_card_or_account_info[-1].isdigit() is True and (
        len(split_card_or_account_info[-1]) == 16 or len(split_card_or_account_info[-1]) == 20
    ):
        if "Счет" in split_card_or_account_info:
            for account_number in split_card_or_account_info:
                if account_number.isalpha():
                    hidden_account_or_card_number += account_number + " "
                elif account_number.isdigit():
                    mask_account_number = get_mask_account(account_number)
                    hidden_account_or_card_number += mask_account_number

        else:
            for card_number in split_card_or_account_info:
                if card_number.isalpha():
                    hidden_account_or_card_number += card_number + " "
                elif card_number.isdigit():
                    mask_card_number = get_mask_card_number(card_number)
                    hidden_account_or_card_number += mask_card_number
        return hidden_account_or_card_number
    return "Некорректный ввод"


def get_date(date_and_time_of_release: str) -> str:
    """Функция возвращает дату в формате ДД.ММ.ГГГГ"""
    formate_date_of_release = date_and_time_of_release[0:10].split("-")
    return ".".join(formate_date_of_release[::-1])


print(get_date("2024-03-11T02:26:18.671407"))
