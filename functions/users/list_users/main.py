import json
from dataclasses import dataclass
import os
from typing import List
import boto3

@dataclass
class Input:
    pass


@dataclass
class User:
    id: str
    name: str
    age: int

@dataclass
class Output:
    users: List[User]


def lambda_handler(event, context):
    USERS_TABLE = os.environ.get("USERS_TABLE")
    dynamodb = boto3.resource("dynamodb")
    users_table = dynamodb.Table(USERS_TABLE)

    users = users_table.scan()["Items"]

    return {"statusCode": 200, "body": json.dumps({"users": users}, default=str)}
