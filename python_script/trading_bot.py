from python_script.Binance_Class.binance_class import user123
from python_script.indicators_calculator.bolling_bands_requests import calculate_bolling_bands
from python_script.indicators_calculator.rsi_binance_requests import calculate_rsi
from bitcoin_analysis import analyze_btc_price
import time

symbols = ['BTCBUSD', 'ETHBUSD', 'GALABUSD', 'AGIXBUSD', 'APTBUSD', 'SOLBUSD',
           'AVAXBUSD', 'ZILBUSD', 'PHBBUSD', 'MANABUSD', 'SANDBUSD', 'SRMBUSD', 'ANCBUSD', 'FTTBUSD',
           'TORNBUSD', 'MIRBUSD', 'FXSBUSD', 'SLPBUSD']

interval = '15m'

money_per_trade = 100
count = 0
while True:
    btc_recent_pourcentage = analyze_btc_price()
    if btc_recent_pourcentage > -1.5:
        for symbol in symbols:

            klines = user123.client.get_klines(
                symbol=symbols[0], interval=interval)

            close_price = [float(kline[4]) for kline in klines]

            lower_band, middle_band, upper_band = calculate_bolling_bands(
                symbol, interval)
            rsi_value = calculate_rsi(symbol, interval, 15)

            current_price = user123.get_price(symbol)
            if current_price < lower_band and rsi_value < 30:
                quantity_buy = user123.cash_to_quantity(
                    symbol, money_per_trade)
                # user123.order_market_buy(symbol, quantity_buy)
                print(f"BOUGHT {quantity_buy} {symbol} at {current_price}$")

            elif current_price > upper_band and rsi_value > 70:
                coin = symbol[:-4]
                quantity_sell = user123.quantity_of(coin)
                # user123.order_market_sell(symbol, quantity_sell)
                print(f"SOLD {quantity_sell} {symbol} at {current_price}$")
            else:
                print(
                    f"NOTHING to do for {symbol} with price at {round(current_price, 3)}$ and rsi at {round(rsi_value, 3)}")
        else:
            print("SELL all positions")
    print("-----SLEEPING FOR 30 SECONDS-----")
    time.sleep(30)
