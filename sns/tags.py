"""
Adds tags to an SNS Topic
"""

import boto3
import botocore


def add_tags_all_topics(key, value):
    """
    Loops through all topics and add the tags specified
    Prints the ARN of the tagged topic

    Args:
        key (str): The Tag Key
        value (str): The Tag Value
    """
    try:
        sns_client = boto3.client("sns")
        # Loop through all topics
        topics = sns_client.list_topics()
        for topic in topics["Topics"]:
            topic_arn = topic["TopicArn"]
            print(f"Tagging topic {topic_arn}")

            sns_client.tag_resource(
                ResourceArn=topic_arn,
                Tags=[
                    {
                        "Key": key,
                        "Value": value,
                    }
                ],
            )
    except botocore.exceptions.ClientError as e:
        print(e.response["Error"]["Message"])
    except botocore.exceptions.ParamValidationError as e:
        print(e)


while True:
    try:
        print("1 - Add Tag")
        print("2 -  Exit")

        option = int(input("Select An Option "))
        if option == 1:
            key = input("Enter the taq key ")
            value = input("Enter a value ")
            add_tags_all_topics(key, value)
        elif option == 2:
            print("Exiting")
            break
        else:
            print("Input a valid option ")
    except ValueError as val_error:
        print(val_error)
        break
    except KeyboardInterrupt:
        print("Keyboard Interrupt! Shutting Down! ")
        break
