import os
import boto3
import requests
from decimal import Decimal
from datetime import datetime, timezone
import json
import uuid

def handler(event, context):
    # Fetch environment variables
    table_name = os.getenv('API_CRYPTOWATCHER_CRYPTOPRICETABLE_NAME')

    # Initialize DynamoDB resource
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    # Get the current date and time in UTC
    current_time = datetime.now(timezone.utc).isoformat()
    date_only = datetime.now(timezone.utc).strftime('%Y-%m-%d')  # Correct date format in UTC

    try:
        response = requests.get(
            'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,notcoin&vs_currencies=uah')
        response.raise_for_status()
        prices = response.json()
    except requests.exceptions.RequestException as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error fetching prices: {e}")
        }

    # Convert prices to Decimal and prepare items for batch write
    try:
        items = []
        for coin, price in prices.items():
            item = {
                'id': str(uuid.uuid4()),  # Unique ID for each item
                'Date': date_only,  # Correct date format in UTC
                'Coin': coin,
                'Price': Decimal(str(price['uah'])),
                'createdAt': current_time,
                'updatedAt': current_time,
                '_version': 1,
                '_deleted': False,
                '_lastChangedAt': int(datetime.now(timezone.utc).timestamp() * 1000)
            }
            items.append(item)

        # Batch write to DynamoDB
        with table.batch_writer() as batch:
            for item in items:
                batch.put_item(Item=item)
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error updating DynamoDB: {e}")
        }

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps('Prices updated successfully!')
    }
