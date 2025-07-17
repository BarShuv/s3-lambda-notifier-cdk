#!/usr/bin/env python3
"""
Manual Lambda Trigger Script

This script allows manual invocation of the deployed Lambda function for testing purposes.
It uses boto3 to invoke the Lambda function and displays the response.

Usage:
    python manual_trigger.py
    python manual_trigger.py <function-name>
"""

import boto3
import json
import sys

# Default Lambda function name (CDK generates this with a unique suffix)
LAMBDA_FUNCTION_NAME = "S3LambdaNotifierCdkStack-NotifierLambda"

# Allow custom function name as command line argument
if len(sys.argv) > 1:
    LAMBDA_FUNCTION_NAME = sys.argv[1]

# Initialize AWS Lambda client
client = boto3.client("lambda")

# Invoke the Lambda function
# This triggers the function to list S3 objects and send SNS notification
response = client.invoke(
    FunctionName=LAMBDA_FUNCTION_NAME,
    InvocationType="RequestResponse",  # Synchronous invocation
    Payload=json.dumps({})  # Empty payload for this function
)

# Display the response
print("Status code:", response["StatusCode"])
print("Response payload:")
print(response["Payload"].read().decode()) 