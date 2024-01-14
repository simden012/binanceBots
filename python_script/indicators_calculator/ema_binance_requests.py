import requests
import pandas as pd


def ema_price(symbol, days, interval):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}"
    data = requests.get(url).json()

    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close',
                                     'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume',
                                     'taker_buy_quote_asset_volume', 'ignore'])

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    df.set_index('timestamp', inplace=True)

    df['ema'] = df['close'].ewm(span=days).mean()

    print(df['ema'])
    return df['ema']


if __name__ == '__main__':

    symbol = 'BTCUSDT'
    days = 7
    interval = '1d'
    ema_price(symbol, days, interval)
