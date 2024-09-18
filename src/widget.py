from masks import get_mask_card_number, get_mask_account


def mask_account_card(card_or_account_info: str) -> str:
    """ Функция, которая маскирует и номер карты, и номер счета """
    split_card_or_account_info = card_or_account_info.split(' ')
    hidden_account_or_card_number = ''
    if 'Счет' in split_card_or_account_info:
        for account_number in split_card_or_account_info:
            if account_number.isalpha():
                hidden_account_or_card_number += account_number + ' '
            elif account_number.isdigit():
                mask_account_number = get_mask_account(account_number)
                hidden_account_or_card_number += mask_account_number

    else:
        for card_number in split_card_or_account_info:
            if card_number.isalpha():
                hidden_account_or_card_number += card_number + ' '
            if card_number.isdigit():
                mask_card_number = get_mask_card_number(card_number)
                hidden_account_or_card_number += mask_card_number

    return hidden_account_or_card_number


def get_date(date_and_time_of_release: str) -> str:
    """Функция возвращает дату в формате ДД.ММ.ГГГГ"""
    date_of_release = date_and_time_of_release[0:9]
    year_month_day = date_of_release.split("-")
    day_month_year = year_month_day[::-1]
    formate_date_of_release = '.'.join(day_month_year)
    return formate_date_of_release
