import aws_cdk as core
import aws_cdk.assertions as assertions

from s3_lambda_notifier_cdk.s3_lambda_notifier_cdk_stack import S3LambdaNotifierCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in s3_lambda_notifier_cdk/s3_lambda_notifier_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = S3LambdaNotifierCdkStack(app, "s3-lambda-notifier-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
