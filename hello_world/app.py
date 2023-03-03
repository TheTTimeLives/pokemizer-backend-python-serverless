import json

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function"""

    return {
        "statusCode": 200,
        "headers": {
        "Access-Control-Allow-Origin": "*"
    },
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
