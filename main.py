import pprint

from client import Client
from currencies_enum import Currencies
from exchanges_enum import Exchanges

api_key = "PlvfwINanqTLZqCScHMbpyFFeWIZzao1CgIjgd3nrQCycQttsunTLRSRjVvazE1S"
api_secret = "5G2worK6d247G7QkebMw94PhSDwPopd7IScPf91IvVfbPsxU63bs7HLfaPr8kOaa"
client = Client(api_key,  api_secret)
account = client.get_account([Currencies.USDT, Currencies.BTC, Currencies.NOT])
pprint.pprint(account.balance)


