import boto3
import json
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
from datetime import datetime

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    s3 = boto3.client('s3')

    prices_table = dynamodb.Table('CryptoPrices')
    predictions_table = dynamodb.Table('CryptoPredictions')
    s3_bucket_name = 'crypto-visualizations'

    def fetch_actual_values():
        response = prices_table.scan()
        items = response['Items']
        actual_values = []
        for item in items:
            actual_values.append({
                'Date': item['Date'],
                'Coin': item['Coin'],
                'Price (UAH)': float(item['Price (UAH)'])
            })
        return pd.DataFrame(actual_values)

    def fetch_predicted_values():
        response = predictions_table.scan()
        items = response['Items']
        predicted_values = []
        for item in items:
            predicted_values.append({
                'Month': item['Month'],
                'Coin': item['Coin'],
                'Min Value (UAH)': float(item['Min Value (UAH)']),
                'Max Value (UAH)': float(item['Max Value (UAH)'])
            })
        return pd.DataFrame(predicted_values)

    actual_values_df = fetch_actual_values()
    predicted_values_df = fetch_predicted_values()

    # Convert dates to datetime objects
    actual_values_df['Date'] = pd.to_datetime(actual_values_df['Date'], errors='coerce')
    actual_values_df = actual_values_df.dropna(subset=['Date'])  # Drop rows where Date conversion failed
    actual_values_df['Actual Value (UAH)'] = actual_values_df.groupby('Date')['Price (UAH)'].transform('sum')
    actual_values_df = actual_values_df.drop_duplicates(subset=['Date'])

    # Convert months to datetime objects
    predicted_values_df['Month'] = pd.to_datetime(predicted_values_df['Month'], format='%Y-%m', errors='coerce')
    predicted_values_df = predicted_values_df.dropna(subset=['Month'])  # Drop rows where Month conversion failed

    def visualize_investments(predicted_df, actual_df):
        plt.figure(figsize=(14, 7))
        for coin in predicted_df['Coin'].unique():
            coin_predicted_df = predicted_df[predicted_df['Coin'] == coin]
            plt.plot(coin_predicted_df['Month'], coin_predicted_df['Min Value (UAH)'], label=f'{coin} Predicted Min Value', linestyle='--')
            plt.plot(coin_predicted_df['Month'], coin_predicted_df['Max Value (UAH)'], label=f'{coin} Predicted Max Value', linestyle='--')

        plt.plot(actual_df['Date'], actual_df['Actual Value (UAH)'], label='Actual Value', color='red', marker='o')
        plt.xlabel('Time (Months)')
        plt.ylabel('Amount of Money (UAH)')
        plt.title('Investment Value Over Time')
        plt.legend()
        plt.grid(True)

        # Save the plot to a BytesIO object
        img_data = BytesIO()
        plt.savefig(img_data, format='png')
        img_data.seek(0)

        # Upload the plot to S3
        s3.upload_fileobj(img_data, s3_bucket_name, 'investment_plot.png')

    visualize_investments(predicted_values_df, actual_values_df)

    return {
        'statusCode': 200,
        'body': json.dumps('Visualization created and uploaded to S3 successfully!')
    }
