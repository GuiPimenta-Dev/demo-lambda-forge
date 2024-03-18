import json
import uuid
from dataclasses import dataclass
import os
import boto3


@dataclass
class Input:
    name: str
    age: int


@dataclass
class Output:
    id: str


def lambda_handler(event, context):
    USERS_TABLE = os.environ.get("USERS_TABLE")
    dynamodb = boto3.resource("dynamodb")
    users_table = dynamodb.Table(USERS_TABLE)

    body = json.loads(event["body"])
    user_id = str(uuid.uuid4())
    users_table.put_item(Item={"PK": user_id, "name": body["name"], "age": body["age"]})

    return {"statusCode": 200, "body": json.dumps({"id": user_id})}
