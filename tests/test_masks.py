import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number() -> None:
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
    assert get_mask_card_number('1234567891011121') == '1234 56** **** 1121'


@pytest.mark.parametrize('card_number, expected', [('', 'Некорректный ввод'),
                                                   ('21451', 'Некорректный ввод'),
                                                   ('242asfaf22444444', 'Некорректный ввод'),
                                                   ('asdsas', 'Некорректный ввод')
])
def test_get_mask_card_number_invalid(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


def test_get_mask_account() -> None:
    assert get_mask_account('73654108430135874305') == '**4305'
    assert get_mask_account('12345678910111213141') == '**3141'


@pytest.mark.parametrize('account_number, expected', [('', 'Некорректный ввод'),
                                                      ('asfasf2223', 'Некорректный ввод'),
                                                      ('24188848484848812818828', 'Некорректный ввод'),
                                                      ('abcdef98581850585243', 'Некорректный ввод')
])
def test_get_mask_account_invalid(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected
