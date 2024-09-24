def process_data(data):
    processed_data = []
    for coin in data:
        processed_data.append({
            'name': coin['name'],
            'symbol': coin['symbol'],
            'price': coin['current_price'],
            'market_cap': coin['market_cap']
        })
    return processed_data

