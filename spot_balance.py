from currencies_enum import Currencies


class SpotBalance:
    def __init__(self, currency: Currencies, amount: float):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f'{self.currency}: {self.amount}'

    def __repr__(self):
        return str(self)