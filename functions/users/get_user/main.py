import json
from dataclasses import dataclass
import os
import boto3

@dataclass
class Path:
    id: str


@dataclass
class Input:
    pass


@dataclass
class Output:
    id: str
    name: str
    age: int


def lambda_handler(event, context):
    USERS_TABLE = os.environ.get("USERS_TABLE")
    dynamodb = boto3.resource("dynamodb")
    users_table = dynamodb.Table(USERS_TABLE)

    user_id = event["pathParameters"].get("user_id")
    user = users_table.get_item(Key={"PK": user_id}).get("Item")

    user = { "id": user["PK"], "name": user["name"], "age": user["age"]}
    return {"statusCode": 200, "body": json.dumps(user,  default=str)}
