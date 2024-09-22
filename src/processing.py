from typing import List, Dict, Any


def filter_by_state(personal_info: list[dict[str, Any]], state_id: str = 'EXECUTED') -> list[dict[str, Any]]:
    personal_info_filter_by_state = []
    for person_info in personal_info:
        if person_info['state'] == state_id:
            personal_info_filter_by_state.append(person_info)
    return personal_info_filter_by_state


def sort_by_date(personal_info: list[dict[str, Any]], option_for_reverse_list: bool = True) -> list[dict[str, Any]]:
    personal_info_sorted_by_date = sorted(personal_info, key=lambda person_info: person_info['date'], reverse = option_for_reverse_list)
    return personal_info_sorted_by_date



print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], False))