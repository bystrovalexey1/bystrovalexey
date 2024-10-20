import json
import os


def file_opening(filename: str) -> list[dict]:
    empty_list_of_transaction = []
    with open(filename, 'r', encoding='utf-8') as file:
        try:
            transactions = json.load(file)
            if transactions == 0 or type(transactions) is not list:
                return empty_list_of_transaction
            else:
                return transactions
        except json.JSONDecodeError:
            print('Invalid JSon data')
            return empty_list_of_transaction

if __name__ == '__main__':
    filename_operations = 'C:\\Users\\Alexey\\PycharmProjects\\pythonProject2\\data\\operations.json'
    print(file_opening(filename_operations))
