from bolling_bands_requests import lower_bolling_band
from order_market import get_price
from binance_class import simden_user
import time

tickers = ['BTCBUSD','OCEANBUSD', 'GALABUSD', 'AGIXBUSD', 'APTBUSD', 'SOLBUSD', 
'AVAXBUSD', 'ZILBUSD', 'PHBBUSD', 'MANABUSD', 'SANDBUSD', 'SRMBUSD', 'ANCBUSD', 'FTTBUSD',
 'TORNBUSD', 'MIRBUSD', 'FXSBUSD', 'SLPBUSD']
interval = '15m'

while True:

    for ticker in tickers:
        lower = lower_bolling_band(ticker, interval)
        price = simden_user.get_price(ticker)
        
        difference = abs(price - lower)
        if(difference/lower <= 0.015):
            print(f"{ticker} is at {price} and lower is {lower}")
        else:
            print(f"NOTHING to do for {ticker} with price at {round(price, 3)}$")

    print("-----SLEEPING FOR 30 SECONDS-----")
    time.sleep(30)
    