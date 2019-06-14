import requests 

from flask import Flask, request
from flask_restful import Resource, Api


# Profits route
class Profits(Resource):
    def get(self):
        # Define coins
        coins = [
            {'id': 'bitcoin', 'invested': 1000, 'amount': 1, 'price_eur': 0, 'worth': 0, 'made_loss': 0},
            {'id': 'ethereum', 'invested': 3000, 'amount': 3, 'price_eur': 0, 'worth': 0, 'made_loss': 0}
        ]
        
        # Define sync data
        sync = {'total_worth': 0, 'total_invested': 0}

        sync_success = False

        # Foreach coin, get data from Coin Market Cap, calculate profits
        for coin in coins:
            # Get coin data
            request = requests.get("https://api.coinmarketcap.com/v1/ticker/" + coin['id'] + "/?convert=EUR") 

            if request:
                request_json = request.json()

                if request_json:
                    coin_data = request_json[0]

                    if coin_data:
                        price_eur = float(coin_data['price_eur'])

                        if price_eur:
                            coin['price_eur'] = price_eur

                            calculated_worth = price_eur * coin['amount']
                            invested = coin['invested']

                            coin['worth'] = calculated_worth
                            coin['made_loss'] = calculated_worth - invested

                            # Calculate total word/invested
                            sync['total_worth'] += calculated_worth
                            sync['total_invested'] += invested

                            sync_success = True
        
        # If sync is successful, return sync data, otherwise return error
        if sync_success:
            return {'status': 200, 'type': 'success', 'response': {'coins': coins, 'sync': sync}}

        return {'status': 500, 'type': 'error', 'response': "An error occurred while calculating profits/ Please try again."}


# Set up API
app = Flask(__name__)
api = Api(app)

api.add_resource(Profits, '/')

if __name__ == '__main__':
     app.run(port='8082')