from currencies_enum import Currencies
from enum import Enum


class Exchanges(Enum):
    BTC_USDT = Currencies.BTC, Currencies.USDT
    NOT_USDT = Currencies.NOT, Currencies.USDT

    def __str__(self):
        return self.value[0] + self.value[1]

    @property
    def reversed(self):
        return self.value[1] + self.value[0]


