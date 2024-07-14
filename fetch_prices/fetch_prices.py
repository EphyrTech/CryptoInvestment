import boto3
import requests
from decimal import Decimal
from datetime import datetime

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CryptoPrices')

    # Get the current date and time
    current_time = datetime.utcnow().isoformat()

    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,notcoin&vs_currencies=uah')
    prices = response.json()

    # Convert prices to Decimal
    for coin, price in prices.items():
        prices[coin] = Decimal(str(price['uah']))

    table.put_item(
        Item={
            'Date': current_time,
            'Coin': 'bitcoin',
            'Price (UAH)': prices['bitcoin']
        }
    )

    table.put_item(
        Item={
            'Date': current_time,
            'Coin': 'ethereum',
            'Price (UAH)': prices['ethereum']
        }
    )

    table.put_item(
        Item={
            'Date': current_time,
            'Coin': 'notcoin',
            'Price (UAH)': prices['notcoin']
        }
    )

    return {
        'statusCode': 200,
        'body': 'Prices updated successfully!'
    }
