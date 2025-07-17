#!/usr/bin/env python3
"""
AWS CDK Application Entry Point

This module defines the main CDK application that deploys the S3 Lambda Notifier stack.
The application creates an S3 bucket, Lambda function, SNS topic, and IAM roles
for a serverless notification system.

Usage:
    cdk deploy --context email=your-email@example.com
"""

import os
import aws_cdk as cdk
from s3_lambda_notifier_cdk.s3_lambda_notifier_cdk_stack import S3LambdaNotifierCdkStack

# Initialize the CDK application
app = cdk.App()

# Get email address for SNS subscription from context or use default
# The email address is used to subscribe to SNS notifications
# You can pass it via: cdk deploy --context email=your-email@example.com
email_address = app.node.try_get_context("email") or "your-email@example.com"

# Instantiate the main stack with the email address
# This creates all AWS resources: S3 bucket, Lambda function, SNS topic, IAM roles
S3LambdaNotifierCdkStack(app, "S3LambdaNotifierCdkStack", email_address=email_address)

# Synthesize the CloudFormation template
# This generates the CloudFormation template that will be deployed to AWS
app.synth()
