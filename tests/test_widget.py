import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_or_account, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ],
)
def test_mask_account_card(card_or_account: str, expected: str) -> None:
    """Проверка маскировки карты или счета, когда все введено корректно"""
    assert mask_account_card(card_or_account) == expected


@pytest.mark.parametrize(
    "card_or_account, expected",
    [
        ("", "Некорректный ввод"),
        ("Visa Gold 59998426353", "Некорректный ввод"),
        ("Maestro1596837868705199", "Некорректный ввод"),
        ("Счет 346363", "Некорректный ввод"),
        ("Счет73654108430135874305", "Некорректный ввод"),
        ("Счет", "Некорректный ввод"),
        ("Visa", "Некорректный ввод"),
    ],
)
def test_mask_account_card_invalid(card_or_account: str, expected: str) -> None:
    """Проверка вывода 'Некорректный ввод', когда счет или карта введены некорректно"""
    assert mask_account_card(card_or_account) == expected


def test_get_date() -> None:
    """Проверка вывода даты выпуска карты в формате ДД.ММ.ГГГГ, если дата введена корректно"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize(
    "date, expected",
    [
        ("", "Некорректный ввод"),
        ("T02:26:18.671407", "Некорректный ввод"),
        ("2024.03.11T02:26:18.671407", "Некорректный ввод"),
    ],
)
def test_get_date_invalid(date: str, expected: str) -> None:
    """Проверка вывода 'Некорректный ввод', если дата введена некорректно"""
    assert get_date(date) == expected
