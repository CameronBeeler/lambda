import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    bucketList = []
    for bucket in s3.buckets.all():
        print(bucket.name)
        bucketList.append(bucket.name)
    return { 'statusCode':200, 'body':bucketList }


"""
def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
