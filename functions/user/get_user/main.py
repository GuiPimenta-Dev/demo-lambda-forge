import json
from dataclasses import dataclass
import os
import boto3

@dataclass
class Path:
    pass


@dataclass
class Input:
    pass


@dataclass
class Output:
    message: str


def lambda_handler(event, context):
    USERS_TABLE = os.environ.get("USERS_TABLE")
    dynamodb = boto3.resource("dynamodb")
    users_table = dynamodb.Table(USERS_TABLE)

    user_id = event["pathParameters"].get("user_id")
    user = users_table.get_item(Key={"PK": user_id}).get("Item")

    return {"statusCode": 200, "body": json.dumps(user,  default=str)}
