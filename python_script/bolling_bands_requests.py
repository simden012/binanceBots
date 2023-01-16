import requests
import pandas as pd
import numpy as np
import ta

def bolling_bands(symbol, interval):

    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}"


    data = requests.get(url).json()

    # Convert the klines data to a DataFrame
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 
    'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 
    'taker_buy_quote_asset_volume', 'ignore'])

    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Set timestamp as index
    df.set_index('timestamp', inplace=True)

    bb = ta.volatility.BollingerBands(close=df["close"], window=21, window_dev=2)

    # Create new columns for the Bollinger Bands
    df["bb_upper"] = bb.bollinger_hband()
    df["bb_lower"] = bb.bollinger_lband()
    df["bb_middle"] = bb.bollinger_mavg()

    return float(bb.bollinger_lband()[-1]), float(bb.bollinger_mavg()[-1]), float(bb.bollinger_hband()[-1])
def lower_bolling_band(symbol, interval):

    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}"


    data = requests.get(url).json()

    # Convert the klines data to a DataFrame
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 
    'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 
    'taker_buy_quote_asset_volume', 'ignore'])

    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Set timestamp as index
    df.set_index('timestamp', inplace=True)

    bb = ta.volatility.BollingerBands(close=df["close"], window=21, window_dev=2)

    # Create new columns for the Bollinger Bands
    df["bb_lower"] = bb.bollinger_lband()

    return float(bb.bollinger_lband()[-1])

def calculate_bolling_bands_slope(lower):

    last_four_lower = lower[-5:-1]
    x = [i for i in range(1, 5)]

    slope = np.polyfit(x, last_four_lower, 1)[0]
    
    return slope

# symbol = 'BTCUSDT'
# interval = '15m'

# lower, middle, upper = bolling_bands(symbol, interval)
# slope_lower = calculate_bolling_bands_slope(lower)

# print(f"lower is {lower}")
# print(f"middle is {middle}")
# print(f"upper is {upper}")
# print(f"slope is {slope_lower}")


