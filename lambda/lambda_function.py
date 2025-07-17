import os
import boto3
import json
import logging

def lambda_handler(event, context):
    """
    AWS Lambda function to list all objects in a specified S3 bucket and send an SNS email notification
    with the object list.
    """
    # Set up logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    bucket_name = os.environ["BUCKET_NAME"]
    topic_arn = os.environ["TOPIC_ARN"]

    s3 = boto3.client("s3")
    sns = boto3.client("sns")

    # List objects in the bucket
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        objects = response.get("Contents", [])
        object_list = [obj["Key"] for obj in objects]
        logger.info(f"Found {len(object_list)} objects in bucket {bucket_name}.")
    except Exception as e:
        logger.error(f"Error listing objects in bucket {bucket_name}: {e}")
        raise

    # Create a human-readable message
    message = f"found {len(object_list)} objects: \n"
    if object_list:
        message += ",\n    ".join(f'"{obj}"' for obj in object_list)
    else:
        message += "    No objects found in the bucket."

    # Publish to SNS
    try:
        sns.publish(
            TopicArn=topic_arn,
            Subject=f"S3 Bucket {bucket_name} Object List",
            Message=message
        )
        logger.info(f"Notification sent to SNS topic {topic_arn}.")
    except Exception as e:
        logger.error(f"Error publishing to SNS topic {topic_arn}: {e}")
        raise

    return {
        "statusCode": 200,
        "body": message
    } 