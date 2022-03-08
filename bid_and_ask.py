import time, json, requests

# get bid and ask for Bitcoin from bitstamp
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


# get bid and ask for XRP from bitstamp
def bitstampLastBidPriceXRP():
    bitStampLast = requests.get('https://www.bitstamp.net/api/v2/order_book/xrpusd/')
    return bitStampLast.json()['bids'][0][0]
def bitstampLastBidQuantityXRP():
    bitStampLast = requests.get('https://www.bitstamp.net/api/v2/order_book/xrpusd/')
    return bitStampLast.json()['bids'][0][1]
def bitstampLastAskPriceXRP():
    bitStampLast = requests.get('https://www.bitstamp.net/api/v2/order_book/xrpusd/')
    return bitStampLast.json()['asks'][1][0]
def bitstampLastAskQuantityXRP():
    bitStampLast = requests.get('https://www.bitstamp.net/api/v2/order_book/xrpusd/')
    return bitStampLast.json()['asks'][1][1]

# get tickers from various exchanges
def bitstampXRP():
    bitStampTick = requests.get('https://www.bitstamp.net/api/v2/ticker/xrpusd/')
    return bitStampTick.json()['last']

def bitfinexXRP():
    bitFinexTick = requests.get('https://api.bitfinex.com/v1/ticker/xrpusd')
    return bitFinexTick.json()['last_price']

def coinbaseXRP():
    coinbaseTick = requests.get('https://coinbase.com/api/v2/prices/XRP-USD/buy')
    return coinbaseTick.json()['data']['amount']

def krakenXRP():
    krakenTick = requests.post('https://api.kraken.com/0/public/Ticker', 
    data=json.dumps({"pair": "XXXRPUSD"}),
    headers={'content-type':'application/json'})
    return krakenTick.json()['result']['XXXRPUSD']['c'][0]


# get bid and ask for ETH from bitstamp
def bitstampLastBidPriceETH():
    bitStampLast = requests.get('https://www.bitstamp.net/api/v2/order_book/ethusd/')
    return bitStampLast.json()['bids'][0][0]
def bitstampLastBidQuantityETH():
    bitStampLast = requests.get('https://www.bitstamp.net/api/v2/order_book/ethusd/')
    return bitStampLast.json()['bids'][0][1]
def bitstampLastAskPriceETH():
    bitStampLast = requests.get('https://www.bitstamp.net/api/v2/order_book/ethusd/')
    return bitStampLast.json()['asks'][1][0]
def bitstampLastAskQuantityETH():
    bitStampLast = requests.get('https://www.bitstamp.net/api/v2/order_book/ethusd/')
    return bitStampLast.json()['asks'][1][1]

# get tickers from various exchanges
def bitstampETH():
    bitStampTick = requests.get('https://www.bitstamp.net/api/ticker/ethusd/')
    return bitStampTick.json()['last']

def bitfinexETH():
    bitFinexTick = requests.get('https://api.bitfinex.com/v1/ticker/ethusd')
    return bitFinexTick.json()['last_price']

def coinbaseETH():
    coinbaseTick = requests.get('https://coinbase.com/api/v2/prices/ETH-USD/buy')
    return coinbaseTick.json()['data']['amount']

def krakenETH():
    krakenTick = requests.post('https://api.kraken.com/0/public/Ticker', 
    data=json.dumps({"pair": "XXETHUSD"}),
    headers={'content-type':'application/json'})
    return krakenTick.json()['result']['XXETHUSD']['c'][0]

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

    print('---- BTC Ticker ----')
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

    # XRP info
    bitstampUSDLiveXRP = float(bitstampXRP())
    bitfinexUSDLiveXRP = float(bitfinexXRP())
    #coinbaseUSDLiveXRP = float(coinbaseXRP())
    #krakenUSDLiveXRP = float(krakenXRP())

    print('---- XRP Ticker ----')
    print("Bitstamp Price in USD: ", bitstampUSDLiveXRP)
    #print("Coinbase Price in USD: ", coinbaseUSDLiveXRP)
    print("Bitfinex Price in USD: ", bitfinexUSDLiveXRP)
    #print("Kraken Price in USD: ", krakenUSDLiveXRP)
    print(" ")

    bitstampLastBidPXRP = float(bitstampLastBidPriceXRP())
    bitstampLastBidQXRP = float(bitstampLastBidQuantityXRP())
    bitstampLastAskPXRP = float(bitstampLastAskPriceXRP())
    bitstampLastAskQXRP = float(bitstampLastAskQuantityXRP())

    print('---- Bitstamp XRPUSD orders ----')
    print('Last bid:')
    print("           price: ", bitstampLastBidPXRP)
    print("           quantity: ", bitstampLastBidQXRP)
    print('Last ask:')
    print("           price: ", bitstampLastAskPXRP)
    print("           quantity: ", bitstampLastAskQXRP)
    print(" ")
    print(" ")
    print(" ")

    # ETH info
    bitstampUSDLiveETH = float(bitstampETH())
    bitfinexUSDLiveETH = float(bitfinexETH())
    coinbaseUSDLiveETH = float(coinbaseETH())
    #krakenUSDLiveETH = float(krakenETH())

    print('---- ETH Ticker ----')
    print("Bitstamp Price in USD: ", bitstampUSDLiveETH)
    print("Coinbase Price in USD: ", coinbaseUSDLiveETH)
    print("Bitfinex Price in USD: ", bitfinexUSDLiveETH)
    #print("Kraken Price in USD: ", krakenUSDLiveETH)
    print(" ")

    bitstampLastBidPETH = float(bitstampLastBidPriceETH())
    bitstampLastBidQETH = float(bitstampLastBidQuantityETH())
    bitstampLastAskPETH = float(bitstampLastAskPriceETH())
    bitstampLastAskQETH = float(bitstampLastAskQuantityETH())

    print('---- Bitstamp ETHUSD orders ----')
    print('Last bid:')
    print("           price: ", bitstampLastBidPETH)
    print("           quantity: ", bitstampLastBidQETH)
    print('Last ask:')
    print("           price: ", bitstampLastAskPETH)
    print("           quantity: ", bitstampLastAskQETH)
    print(" ")
    print(" ")
    print(" ")
    time.sleep(3)