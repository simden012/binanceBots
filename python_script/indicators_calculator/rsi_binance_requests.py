import requests

#calculate the rsi for a certain symbol

def calculate_rsi(symbol, interval, limit):

    # Get the historical price data for symbol from the Binance API

    url = "https://api.binance.com/api/v3/klines"

    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    response = requests.get(url, params=params)
    data = response.json()
    
    # Extract the closing prices from the data
    close_prices = [float(item[4]) for item in data]

    gains =[]
    losses = []

    for i in range(1, len(close_prices)):
        change = close_prices[i] - close_prices[i-1]
        if change > 0:
            gains.append(change)
        elif change < 0:
            losses.append(abs(change))

    average_gain = sum(gains) / len(gains)
    average_loss = sum(losses) / len(losses)

    rs = average_gain / average_loss

    rsi = 100 - (100 / (1 + rs))

    return rsi

def statement_from_rsi(rsi, symbol):
    if rsi < 30:
        print(f"The RSI is low, this is a good time to buy. for {symbol}")
    elif rsi > 70:
        print(f"The RSI is high, this is a good time to sell. for {symbol}")
    else:
        print(f"Your judgment is required. The RSI is in the middle of the range. for {symbol}")
    return None


if __name__ == "__main__":
    symbols = ['OCEANUSDT', 'GALAUSDT', 'AGIXBUSD', 'APTBUSD', 'SOLBUSD']
    interval = "1d"
    limit = 20
    for symbol in symbols:
        rsi_value = calculate_rsi(symbol, interval, limit)
        print(rsi_value)
        statement_from_rsi(rsi_value, symbol)

