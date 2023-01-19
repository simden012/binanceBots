from bolling_bands_requests import lower_bolling_band, calculate_bolling_bands
from binance_class import user123
import time

tickers = ['BTCBUSD','OCEANBUSD', 'GALABUSD', 'AGIXBUSD', 'APTBUSD', 'SOLBUSD', 
'AVAXBUSD', 'ZILBUSD', 'PHBBUSD', 'MANABUSD', 'SANDBUSD', 'SRMBUSD', 'ANCBUSD', 'FTTBUSD',
'TORNBUSD', 'MIRBUSD', 'FXSBUSD', 'SLPBUSD']
interval = '15m'

while True:

    for ticker in tickers:
        lower, middle, upper = calculate_bolling_bands(ticker, interval)
        price = user123.get_price(ticker)
        
        difference_lower_mid = middle - lower

        difference_price_lower = abs(price - lower)
        if(difference_price_lower/difference_lower_mid <= 0.5):
            print(f"{ticker} is at {price} and lower is {round(lower,3)}")
        else:
            print(f"NOTHING to do for {ticker} with price at {round(price, 3)}$")

    print("-----SLEEPING FOR 30 SECONDS-----")
    time.sleep(45)
    