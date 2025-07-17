
# S3 Lambda Notifier CDK

[![Build Status](https://github.com/<your-username>/s3-lambda-notifier-cdk/actions/workflows/deploy.yml/badge.svg)](https://github.com/<your-username>/s3-lambda-notifier-cdk/actions)
![Python](https://img.shields.io/badge/python-3.10-blue)
![AWS CDK](https://img.shields.io/badge/aws--cdk-2.x-orange)

## Project Overview

This project deploys an AWS serverless application using AWS CDK (Python). It provisions:
- An S3 bucket
- A Lambda function (Python) that lists all objects in the bucket and sends an email via SNS
- An SNS topic with email subscription
- IAM roles with least-privilege permissions
- Uploads files from `sample_files/` to the S3 bucket during deployment
- Includes a script to manually trigger the Lambda
- GitHub Actions workflow for CI/CD

## Architecture

```mermaid

```

## Features

- **Serverless Architecture**: Utilizes AWS Lambda and S3 for scalable and cost-effective solutions.
- **Email Notifications**: Sends email notifications via SNS when new files are detected.
- **Least Privilege Access**: IAM roles and policies ensure secure access to S3 and SNS.
- **Automated Deployment**: GitHub Actions workflow for CI/CD.
- **Manual Trigger**: Script to manually invoke the Lambda function.

## Project Structure

```
s3-lambda-notifier-cdk/
├── cdk.json
├── requirements.txt
├── sample_files/
│   ├── file1.txt
│   ├── file2.txt
│   └── file3.txt
├── src/
│   ├── s3_lambda_notifier.py
│   └── sns_notifier.py
├── tests/
│   └── test_s3_lambda_notifier.py
└── .github/
    └── workflows/
        └── deploy.yml
```

## Quick Start

1. **Install dependencies:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Bootstrap your AWS environment (first time only):**
   ```bash
   cdk bootstrap
   ```
3. **Deploy the stack:**
   ```bash
   cdk deploy --context email=your-email@example.com
   ```
   Replace `your-email@example.com` with your real email address to receive SNS notifications.

4. **Upload sample files to S3:**
   ```bash
   python upload_sample_files.py
   ```

5. **Confirm your email subscription:**
   After deployment, check your email and confirm the SNS subscription to receive notifications. **You must confirm the subscription from your email inbox before you will receive notifications.**

## Manual Lambda Trigger

You can manually invoke the Lambda function using the provided script (requires AWS credentials configured, e.g., via AWS CLI or environment variables):

```bash
python manual_trigger.py
```

Or specify the Lambda function name:

```bash
python manual_trigger.py S3LambdaNotifierCdkStack-NotifierLambda
```

This script uses `boto3` to invoke the Lambda function directly.

## GitHub Actions CI/CD

- The workflow in `.github/workflows/deploy.yml` deploys the stack on `workflow_dispatch` (manual trigger from the GitHub Actions tab).
- Set the following GitHub repository secrets:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_DEFAULT_REGION`
  - `NOTIFY_EMAIL` (your email for SNS subscription)

To trigger the workflow:
1. Go to the **Actions** tab in your GitHub repository.
2. Select the **Deploy CDK Stack** workflow.
3. Click **Run workflow** (top right) to start a manual deployment.

## Tools/Frameworks Used
- AWS CDK (Python)
- boto3
- GitHub Actions

## sample_files/
- Contains sample `.txt` files that are uploaded to the S3 bucket during deployment.

# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
