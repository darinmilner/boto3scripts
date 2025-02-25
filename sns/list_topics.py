import boto3
import botocore


def list_topics():
    """
    Prints a list of SNS Topics ARNs
    """
    try:
        sns_resource = boto3.resource("sns")

        topics = sns_resource.topics.all()

        for topic in topics:
            print(f"Topic Arn {topic.arn}")
    except botocore.exceptions.ClientError as e:
        print(e.response["Error"]["Message"])


def list_subscriptions():
    """
    Prints a list of SNS Topic Subscriptions ARNs
    """
    try:
        sns_resource = boto3.resource("sns")

        subscriptions = sns_resource.subscriptions.all()

        for subscription in subscriptions:
            print(f"Subscriptiuon ARN {subscription.arn}")

    except botocore.exceptions.ClientError as e:
        print(e.response["Error"]["Message"])


list_topics()
list_subscriptions()
