import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def file_opening(filename: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    empty_list_of_transaction = []
    try:
        logger.info(f"Выполняем поиск файла {filename}")
        with open(filename, "r", encoding="utf-8") as file:
            logger.info(f"Открытие json файла {filename}")
            try:
                logger.info("Конвертируем json файл в python")
                transactions = json.load(file)
                if transactions == 0 or type(transactions) is not list:
                    logger.warning("Пустой файл или не верный тип, возвращаем пустой список")
                    return empty_list_of_transaction
                else:
                    logger.info("Успешная конвертация")
                    return transactions
            except json.JSONDecodeError:
                logger.error("Ошибка конвертации")
                print("Invalid JSon data")
                return empty_list_of_transaction
    except FileNotFoundError:
        logger.error("Ошибка, файл не найден")
        return []
