from typing import List

import binance.client as binc

from account import Account
from currencies_enum import Currencies
from spot_balance import SpotBalance


class Client:
    def __init__(self, api_key: str, api_secret: str):
        self._client = binc.Client(api_key, api_secret)

    def get_account(self, currencies: List[Currencies]) -> Account:
        got_account = self._client.get_account()
        balances = got_account['balances']
        account = Account()
        for balance in balances:
            currency = balance['asset']
            if currency in currencies:
                account.balance.append(SpotBalance(currency, float(balance['free'])))
        return account
