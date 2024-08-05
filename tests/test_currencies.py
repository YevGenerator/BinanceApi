from exchanges_enum import *

print(Currencies.NOT)
print(Currencies.USDT)
print(Currencies.BTC)
print(Exchanges.NOT_USDT)
print(Exchanges.BTC_USDT)
print(Exchanges.NOT_USDT.reversed)
print(Exchanges.BTC_USDT.reversed)

print(Exchanges.BTC_USDT.reversed == "USDTBTC")

