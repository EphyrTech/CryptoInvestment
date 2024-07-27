#!/bin/bash

# Variables
S3_BUCKET="crypto-watcher"
PROFILE="yggdrasil"
REGION="us-east-1"
STACK_NAME="CryptoInvestmentStack"
TEMPLATE_FILE="template.yaml"
PACKAGED_TEMPLATE_FILE="packaged.yaml"

# Function to check if the S3 bucket exists
bucket_exists() {
  aws s3 ls "s3://${S3_BUCKET}" --profile "${PROFILE}" --region "${REGION}" 2>&1 | grep -q 'NoSuchBucket'
}

# Create S3 bucket if it doesn't exist
if bucket_exists; then
  echo "Creating S3 bucket: ${S3_BUCKET}"
  aws s3 mb "s3://${S3_BUCKET}" --profile "${PROFILE}" --region "${REGION}"
else
  echo "S3 bucket ${S3_BUCKET} already exists."
fi

# Build the SAM application
echo "Building the SAM application..."
sam build --profile "${PROFILE}" --region "${REGION}"


# Package the SAM template
echo "Packaging SAM template..."
sam package --template-file "${TEMPLATE_FILE}" --s3-bucket "${S3_BUCKET}" --output-template-file "${PACKAGED_TEMPLATE_FILE}" --profile "${PROFILE}" --region "${REGION}"

# Deploy the SAM template
echo "Deploying SAM template..."
sam deploy --template-file "${PACKAGED_TEMPLATE_FILE}" --stack-name "${STACK_NAME}" --capabilities CAPABILITY_IAM --profile "${PROFILE}" --region "${REGION}"

echo "Deployment complete."
