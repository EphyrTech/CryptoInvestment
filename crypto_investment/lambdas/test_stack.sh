#!/bin/bash

# Variables
PROFILE="yggdrasil"
REGION="us-east-1"
STACK_NAME="CryptoInvestmentStack"

# Fetch function names from stack outputs
FETCH_PRICES_FUNCTION=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='FetchPricesFunctionName'].OutputValue" --output text --profile $PROFILE --region $REGION)
CALCULATE_PREDICTIONS_FUNCTION=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='CalculatePredictionsFunctionName'].OutputValue" --output text --profile $PROFILE --region $REGION)
VISUALIZE_DATA_FUNCTION=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='VisualizeDataFunctionName'].OutputValue" --output text --profile $PROFILE --region $REGION)

# Trigger FetchPricesFunction
echo "Triggering FetchPricesFunction..."
aws lambda invoke --function-name $FETCH_PRICES_FUNCTION output_fetch_prices.txt --profile $PROFILE --region $REGION
cat output_fetch_prices.txt

# Trigger CalculatePredictionsFunction
echo "Triggering CalculatePredictionsFunction..."
aws lambda invoke --function-name $CALCULATE_PREDICTIONS_FUNCTION output_calculate_predictions.txt --profile $PROFILE --region $REGION
cat output_calculate_predictions.txt

# Trigger VisualizeDataFunction
echo "Triggering VisualizeDataFunction..."
aws lambda invoke --function-name $VISUALIZE_DATA_FUNCTION output_visualize_data.txt --profile $PROFILE --region $REGION
cat output_visualize_data.txt

# Verify DynamoDB tables
echo "Verifying DynamoDB tables..."
aws dynamodb scan --table-name CryptoPrices --profile $PROFILE --region $REGION > output_dynamodb_prices.json
aws dynamodb scan --table-name CryptoPredictions --profile $PROFILE --region $REGION > output_dynamodb_predictions.json
aws dynamodb scan --table-name CryptoConfig --profile $PROFILE --region $REGION > output_dynamodb_config.json

echo "DynamoDB Prices Table:"
cat output_dynamodb_prices.json
echo "DynamoDB Predictions Table:"
cat output_dynamodb_predictions.json
echo "DynamoDB Config Table:"
cat output_dynamodb_config.json

# Verify S3 bucket
echo "Verifying S3 bucket..."
aws s3 ls s3://crypto-visualizations --profile $PROFILE --region $REGION > output_s3.txt

echo "S3 Bucket Contents:"
cat output_s3.txt

echo "Test completed. Check output files for results."
