import json
import uuid
from .main import lambda_handler


def test_lambda_handler(users_table):

    user_id = str(uuid.uuid4())
    users_table.put_item(Item={"PK": user_id, "name": "Jhon Doe", "age": 30})

    event = {"pathParameters": {"user_id": user_id}}
    lambda_handler(event, None)

    user = users_table.get_item(Key={"PK": user_id}).get("Item")
    assert user is None
