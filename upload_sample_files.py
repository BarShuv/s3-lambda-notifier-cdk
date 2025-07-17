#!/usr/bin/env python3
"""
Sample Files Upload Script

This script uploads all files from the local sample_files/ directory to the deployed S3 bucket.
It automatically discovers the bucket name and uploads all files found in the directory.

Usage:
    python upload_sample_files.py
"""

import boto3
import os

# Initialize S3 client
s3 = boto3.client("s3")

# Try to get the bucket name from the stack outputs (if available)
BUCKET_NAME = None

# Fallback: Find the bucket by prefix (since we know the logical name)
# CDK creates buckets with predictable naming patterns
response = s3.list_buckets()
for bucket in response["Buckets"]:
    if "notifierbucket" in bucket["Name"].lower():
        BUCKET_NAME = bucket["Name"]
        break

if not BUCKET_NAME:
    raise Exception("Could not find the S3 bucket. Please set BUCKET_NAME in upload_sample_files.py.")

# Upload all files from the sample_files directory
folder = "sample_files"
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    if os.path.isfile(file_path):
        print(f"Uploading {file_path} to s3://{BUCKET_NAME}/{filename}")
        s3.upload_file(file_path, BUCKET_NAME, filename) 