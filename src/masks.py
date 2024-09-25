def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате ХХХХ ХХ** **** ХХХХ"""
    hidden_chars = [6, 7, 8, 9, 10, 11]
    hidden_card_number = ""
    if len(card_number) == 16 and card_number.isdigit() is True:
        for i, char in enumerate(card_number):
            if i in hidden_chars:
                hidden_card_number += "*"
            else:
                hidden_card_number += char
        blocks = [
            hidden_card_number[0:4],
            hidden_card_number[4:8],
            hidden_card_number[8:12],
            hidden_card_number[12:16],
        ]
        mask_card_number = " ".join(blocks)
        return mask_card_number
    return 'Некорректный ввод'

def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета в формате **ХХХХ"""
    hidden_account_number = account_number[-6:]
    mask_account_number = ""
    if len(account_number) == 20 and account_number.isdigit() is True:
        for i, value in enumerate(hidden_account_number):
            if 0 <= i < 2:
                mask_account_number += "*"
            else:
                mask_account_number += value
        return mask_account_number
    return 'Некорректный ввод'