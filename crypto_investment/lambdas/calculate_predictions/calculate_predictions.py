import boto3
import decimal
from datetime import datetime, timedelta

def fetch_latest_prices():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CryptoPrices')

    response = table.scan()
    prices = {}
    for item in response['Items']:
        coin = item['Coin']
        price = decimal.Decimal(item['Price (UAH)'])
        prices[coin] = price

    return prices

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CryptoPredictions')

    latest_prices = fetch_latest_prices()

    if not latest_prices:
        return {
            'statusCode': 404,
            'body': 'No latest prices found'
        }

    # Prediction logic
    current_date = datetime.utcnow()
    for i in range(1, 17):  # 16 months of predictions
        future_date = current_date + timedelta(days=30 * i)
        future_date_str = future_date.strftime("%Y-%m")

        for coin, initial_price in latest_prices.items():
            min_value = initial_price * decimal.Decimal(0.8)  # example prediction logic
            max_value = initial_price * decimal.Decimal(1.2)  # example prediction logic

            table.put_item(
                Item={
                    'Month': future_date_str,
                    'Coin': coin,
                    'Min Value (UAH)': min_value,
                    'Max Value (UAH)': max_value
                }
            )

    return {
        'statusCode': 200,
        'body': 'Predictions updated successfully!'
    }
