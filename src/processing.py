from typing import Any


def filter_by_state(personal_info: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция которая фильтрует данные по параметру state"""
    personal_info_filter_by_state = []
    for person_info in personal_info:
        if person_info["state"] == state_id:
            personal_info_filter_by_state.append(person_info)
    return personal_info_filter_by_state


def sort_by_date(personal_info: list[dict[str, Any]], option_for_reverse_list: bool = True) -> list[dict[str, Any]]:
    """Функция сортирует данные по дате"""
    personal_info_sorted_by_date = sorted(
        personal_info, key=lambda person_info: person_info["date"], reverse=option_for_reverse_list
    )
    return personal_info_sorted_by_date
