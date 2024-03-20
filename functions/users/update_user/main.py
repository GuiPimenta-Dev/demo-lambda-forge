import json
from dataclasses import dataclass
import os
import boto3


@dataclass
class Path:
    id: str


@dataclass
class Input:
    name: str
    age: int


@dataclass
class Output:
    message: str


#
def lambda_handler(event, context):
    USERS_TABLE = os.environ.get("USERS_TABLE")
    dynamodb = boto3.resource("dynamodb")
    users_table = dynamodb.Table(USERS_TABLE)

    user_id = event["pathParameters"].get("id")
    body = json.loads(event["body"])
    users_table.put_item(Item={"PK": user_id, "name": body["name"], "age": body["age"]})

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "User updated"}, default=str),
    }
