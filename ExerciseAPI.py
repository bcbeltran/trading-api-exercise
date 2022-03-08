import time, json, requests

# get tickers from various exchanges
def bitstamp():
    bitStampTick = requests.get('https://www.bitstamp.net/api/ticker/')
    return bitStampTick.json()

def bitfinex():
    bitFinexTick = requests.get('https://api.bitfinex.com/v1/ticker/btcusd')
    return bitFinexTick.json()

def coinbase():
    coinbaseTick = requests.get('https://coinbase.com/api/v2/prices/BTC-USD/buy')
    return coinbaseTick.json()

def kraken():
    krakenTick = requests.get

print(bitstamp())