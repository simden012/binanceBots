from binance_class import user123

def analyze_btc_price():
    klines = user123.client.get_klines(symbol = 'BTCUSDT', interval='5m')
    current_price = user123.get_price('BTCUSDT')
    totalPercentageDiff = 0

    for kline in klines[-3:]:
        open_price = float(kline[1])
        close_price = float(kline[4])
        
        percentage_diff = ((close_price - open_price) / open_price) * 100
        print(f"Price difference for 5-minute candle: {percentage_diff:.2f}%")

    percentage_diff_current = ((current_price - open_price) / open_price) * 100
    totalPercentageDiff += percentage_diff_current
    if percentage_diff_current < 0:
        print(f"Current price is {percentage_diff_current:.2f}% lower than the last 5-minute candle")
    else:
        print(f"Current price is {percentage_diff_current:.2f}% higher than the last 5-minute candle")
    return totalPercentageDiff
analyze_btc_price()