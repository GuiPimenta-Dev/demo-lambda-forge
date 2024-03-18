import json
from dataclasses import dataclass
import os
import boto3

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

    users = users_table.scan()["Items"]

    return {"statusCode": 200, "body": json.dumps({"users": users}, default=str)}
