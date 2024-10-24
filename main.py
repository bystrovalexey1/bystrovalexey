from src.masks import get_mask_card_number, get_mask_account
from src.utils import file_opening
import os


file_opening('data/operations.json')
get_mask_card_number('700079228606361')
get_mask_account('73654108430135287430')