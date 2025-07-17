"""
AWS CDK Stack for S3 Lambda Notifier

This stack creates a complete serverless application with:
- S3 bucket for file storage
- Lambda function to list S3 objects and send notifications
- SNS topic with email subscription
- IAM roles with least-privilege permissions

The Lambda function is triggered manually and sends email notifications
with the list of objects in the S3 bucket.
"""

from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    Duration
)
from constructs import Construct

class S3LambdaNotifierCdkStack(Stack):
    """
    Main CDK Stack for the S3 Lambda Notifier application.
    
    This stack creates all necessary AWS resources for a serverless
    notification system that monitors S3 bucket contents.
    """

    def __init__(self, scope: Construct, construct_id: str, email_address: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create S3 bucket for file storage
        # This bucket will store the files that the Lambda function will list
        bucket = s3.Bucket(self, "NotifierBucket")

        # Create SNS topic for email notifications
        # This topic will receive messages from the Lambda function
        topic = sns.Topic(self, "NotifierTopic")
        
        # Add email subscription to the SNS topic
        # The subscriber will receive email notifications when Lambda publishes messages
        topic.add_subscription(subs.EmailSubscription(email_address))

        # Create Lambda function
        # This function lists all objects in the S3 bucket and sends SNS notifications
        lambda_fn = _lambda.Function(
            self, "NotifierLambda",
            runtime=_lambda.Runtime.PYTHON_3_10,  # Python 3.10 runtime
            handler="lambda_function.lambda_handler",  # Entry point in the Lambda code
            code=_lambda.Code.from_asset("lambda"),  # Source code directory
            timeout=Duration.seconds(60),  # Maximum execution time
            environment={
                "BUCKET_NAME": bucket.bucket_name,  # Pass bucket name to Lambda
                "TOPIC_ARN": topic.topic_arn  # Pass SNS topic ARN to Lambda
            }
        )

        # Grant S3 read permissions to Lambda
        # This allows the Lambda function to list and read objects in the bucket
        bucket.grant_read(lambda_fn)
        
        # Grant SNS publish permissions to Lambda
        # This allows the Lambda function to send messages to the SNS topic
        topic.grant_publish(lambda_fn)
        
        # Add CloudWatch Logs permissions to Lambda
        # This allows the Lambda function to write logs to CloudWatch
        lambda_fn.add_to_role_policy(iam.PolicyStatement(
            actions=["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
            resources=["*"]
        ))
