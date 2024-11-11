import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате ХХХХ ХХ** **** ХХХХ"""
    hidden_chars = [6, 7, 8, 9, 10, 11]
    hidden_card_number = ""
    if len(card_number) == 16 and card_number.isdigit() is True:
        logger.info("Проверка номера карты на кол-во символов и тип символов")
        for i, char in enumerate(card_number):
            if i in hidden_chars:
                logger.info("Меняет символ на * и добавляет в отформатированный номер карты")
                hidden_card_number += "*"
            else:
                logger.info("Добавляет цифру в отформатированный номер карты")
                hidden_card_number += char
        blocks = [
            hidden_card_number[0:4],
            hidden_card_number[4:8],
            hidden_card_number[8:12],
            hidden_card_number[12:16],
        ]
        logger.info("Приводит номер к нужномк формату и возвращает его")
        mask_card_number = " ".join(blocks)
        return mask_card_number
    logger.warning("Введен не 16 значный номер карты или не все цифры")
    return "Некорректный ввод"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета в формате **ХХХХ"""
    hidden_account_number = account_number[-6:]
    mask_account_number = ""
    if len(account_number) == 20 and account_number.isdigit() is True:
        logger.info("Проверка правильного ввода номера счета")
        for i, value in enumerate(hidden_account_number):
            if 0 <= i < 2:
                logger.info("Добавление в отформатированный номер счета вместо цифры - *")
                mask_account_number += "*"
            else:
                logger.info("Добавление в отформатированный номер счета цифры")
                mask_account_number += value
        logger.info("Возвращаем отформатированный номер счета")
        return mask_account_number
    logger.warning("Введен не 20 значный номер счета или не все цифры")
    return "Некорректный ввод"
