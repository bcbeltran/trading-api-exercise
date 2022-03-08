import time, json, requests

# get bid and ask from bitstamp
def bitstampLastBidPrice():
    bitStampLast = requests.get('https://www.bitstamp.net/api/v2/order_book/btcusd/')
    return bitStampLast.json()['bids'][0][0]
def bitstampLastBidQuantity():
    bitStampLast = requests.get('https://www.bitstamp.net/api/v2/order_book/btcusd/')
    return bitStampLast.json()['bids'][0][1]
def bitstampLastAskPrice():
    bitStampLast = requests.get('https://www.bitstamp.net/api/v2/order_book/btcusd/')
    return bitStampLast.json()['asks'][1][0]
def bitstampLastAskQuantity():
    bitStampLast = requests.get('https://www.bitstamp.net/api/v2/order_book/btcusd/')
    return bitStampLast.json()['asks'][1][1]

# get tickers from various exchanges
def bitstamp():
    bitStampTick = requests.get('https://www.bitstamp.net/api/ticker/')
    return bitStampTick.json()['last']

def bitfinex():
    bitFinexTick = requests.get('https://api.bitfinex.com/v1/ticker/btcusd')
    return bitFinexTick.json()['last_price']

def coinbase():
    coinbaseTick = requests.get('https://coinbase.com/api/v2/prices/BTC-USD/buy')
    return coinbaseTick.json()['data']['amount']

def kraken():
    krakenTick = requests.post('https://api.kraken.com/0/public/Ticker', 
    data=json.dumps({"pair": "XXBTZUSD"}),
    headers={'content-type':'application/json'})
    return krakenTick.json()['result']['XXBTZUSD']['c'][0]

# print('This is the Bitstamp Last Bid Price response:')
# print('========')
# print(bitstampLastBidPrice())
# print('This is the Bitstamp Last Bid Quantity response:')
# print('========')
# print(bitstampLastBidQuantity())
# print('This is the Bitstamp Last Ask Price response:')
# print('========')
# print(bitstampLastAskPrice())
# print('This is the Bitstamp Last Ask Quantity response:')
# print('========')
# print(bitstampLastAskQuantity())

while True:
    bitstampUSDLive = float(bitstamp())
    bitfinexUSDLive = float(bitfinex())
    coinbaseUSDLive = float(coinbase())
    krakenUSDLive = float(kraken())

    print('---- Ticker ----')
    print("Bitstamp Price in USD: ", bitstampUSDLive)
    print("Coinbase Price in USD: ", coinbaseUSDLive)
    print("Bitfinex Price in USD: ", bitfinexUSDLive)
    print("Kraken Price in USD: ", krakenUSDLive)
    print(" ")

    bitstampLastBidP = float(bitstampLastBidPrice())
    bitstampLastBidQ = float(bitstampLastBidQuantity())
    bitstampLastAskP = float(bitstampLastAskPrice())
    bitstampLastAskQ = float(bitstampLastAskQuantity())

    print('---- Bitstamp BTCUSD orders ----')
    print('Last bid:')
    print("           price: ", bitstampLastBidP)
    print("           quantity: ", bitstampLastBidQ)
    print('Last ask:')
    print("           price: ", bitstampLastAskP)
    print("           quantity: ", bitstampLastAskQ)
    print(" ")
    print(" ")
    print(" ")
    time.sleep(3)