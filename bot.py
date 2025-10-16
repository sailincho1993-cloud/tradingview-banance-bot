from flask import Flask, request
from binance.client import Client
import os

app = Flask(__name__)

api_key = os.environ.get("BINANCE_API_KEY")
api_secret = os.environ.get("BINANCE_API_SECRET")
client = Client(api_key, api_secret)

@app.route('/')
def home():
    return "✅ Trading Bot Running on Render!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Received: {data}")

    if data['signal'] == "BUY":
        client.order_market_buy(symbol=data['symbol'], quantity=data['qty'])
        return "Buy executed", 200
    elif data['signal'] == "SELL":
        client.order_market_sell(symbol=data['symbol'], quantity=data['qty'])
        return "Sell executed", 200
    else:
        return "Invalid signal", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
