from binance_class import user123
from bolling_bands_requests import calculate_bolling_bands
from rsi_binance_requests import rsi

symbols = ['BTCBUSD','OCEANBUSD', 'GALABUSD', 'AGIXBUSD', 'APTBUSD', 'SOLBUSD', 
'AVAXBUSD', 'ZILBUSD', 'PHBBUSD', 'MANABUSD', 'SANDBUSD', 'SRMBUSD', 'ANCBUSD', 'FTTBUSD',
'TORNBUSD', 'MIRBUSD', 'FXSBUSD', 'SLPBUSD']

interval = '15m'

money_per_trade = 100

while True:
    for symbol in symbols:

        klines = user123.client.get_klines(symbol = symbols[0], interval=interval)
        # print(klines)
        close_price = [float(kline[4]) for kline in klines]
        print(close_price)

        lower_band, middle_band, upper_band = calculate_bolling_bands(symbol, interval)

        rsi = rsi(symbol, interval, 15)
        print(rsi)

        current_price = user123.get_price(symbol)

        if current_price < lower_band and rsi < 30:
            quantity = user123.cash_to_quantity(symbol, money_per_trade)
            user123.order_market_buy(symbol, quantity)
            print(f"BOUGHT {quantity} {symbol} at {current_price}$")
        elif current_price > upper_band and rsi > 70:
            
       
