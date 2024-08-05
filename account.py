from typing import List

from currencies_enum import Currencies
from spot_balance import SpotBalance


class Account:
    def __init__(self):
        self.balance: List[SpotBalance] = []



