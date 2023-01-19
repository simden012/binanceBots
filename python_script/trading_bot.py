from binance_class import user123

symbols = ['BTCBUSD','OCEANBUSD', 'GALABUSD', 'AGIXBUSD', 'APTBUSD', 'SOLBUSD', 
'AVAXBUSD', 'ZILBUSD', 'PHBBUSD', 'MANABUSD', 'SANDBUSD', 'SRMBUSD', 'ANCBUSD', 'FTTBUSD',
'TORNBUSD', 'MIRBUSD', 'FXSBUSD', 'SLPBUSD']

interval = '15m'

while True:
    for symbol in symbols:

        price = user123.get_price(symbol)

        

        
