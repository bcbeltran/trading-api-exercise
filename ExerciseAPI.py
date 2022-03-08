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
    krakenTick = requests.post('https://api.kraken.com/0/public/Ticker', 
    data=json.dumps({"pair": "XXBTZUSD"}),
    headers={'content-type':'application/json'})
    return krakenTick.json()

print('This is the Bitstamp response:')
print('========')
print(bitstamp())
print('This is the BitFinex response:')
print('========')
print(bitfinex())
print('This is the Coinbase response:')
print('========')
print(coinbase())
print('This is the Kraken response:')
print('========')
print(kraken())
