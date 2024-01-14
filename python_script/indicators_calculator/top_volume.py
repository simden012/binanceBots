import requests

def get_top_volatility():

    url = 'https://api.binance.com/api/v3/ticker/24hr'
    response = requests.get(url)
    data = response.json()


    #keep only the ones that the symbol contains usdt as their last 4 characters
    data = [item for item in data if item['symbol'][-4:] == 'USDT']
    
    return data
# get_top_volatility()