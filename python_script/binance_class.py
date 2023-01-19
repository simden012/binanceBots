from binance.client import Client
from client_binance import api_key, secret_key

class binance_user:
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self.client = Client(self.api_key , self.secret_key)

    def order_market_buy(self, symbol, quantity):
        server_time = self.client.get_server_time()

        order = self.client.order_market_buy(
            symbol=symbol,
            quantity=quantity,
            recvWindow=60000,
            timestamp = server_time['serverTime']
        )

        if(order['status'] == 'FILLED'):
            print(f"Buy Order for {symbol} was filled for this quantity: {quantity} so {self.quantity_to_price(symbol, quantity)}$")
        return order

    def order_market_sell(self, symbol, quantity):
        server_time = self.client.get_server_time()

        order = self.client.order_market_sell(
            symbol=symbol,
            quantity=quantity,
            recvWindow=60000,
            timestamp = server_time['serverTime']
        )

        if(order['status'] == 'FILLED'):
            print(f"Sell Order for {symbol} was filled for this quantity: {quantity} so {self.quantity_to_price(symbol, quantity)}$")
        return order
    
    def get_price(self, symbol):
        response = self.client.get_symbol_ticker(symbol=symbol)

        return float(response['price'])
    
    def limit_order(self, ticker, side, quantity, price):
        order_limit = self.client.create_order(
            symbol=ticker,
            side=side,
            type='LIMIT',
            timeInForce='GTC',
            quantity=quantity,
            price=price)

        if(order_limit['status'] == 'NEW'):
            print(f"Limit Order for {ticker} was created for this quantity: {quantity} and this price: {price}")
        return order_limit

    def quantity_to_price(self, symbol, quantity):
        price = self.get_price(symbol = symbol)
        return round(price * quantity, 2)
        
    ## Stop Limit Order doesnt work yet
    def stop_limit_order(self, ticker, quantity, stop_price, price):
        order_stop_limit = self.client.create_order(
            symbol=ticker,
            side='SELL',
            type = self.client.ORDER_TYPE_STOP_LOSS_LIMIT,
            timeInForce='GTC',
            quantity=quantity,
            price=price,
            stopPrice=stop_price)

        print(order_stop_limit)

        return order_stop_limit


user123 = binance_user(api_key, secret_key)
# print(simden_user.get_price('ETHBUSD'))
# simden_user.order_market_buy('ETHBUSD', 0.02)
# simden_user.limit_order('AGIXBUSD', 'BUY', 1000, 0.1)
# simden_user.stop_limit_order('ETHBUSD', 0.01, 995, 1000)
