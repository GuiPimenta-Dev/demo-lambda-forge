import json
import uuid
from .main import lambda_handler


def test_lambda_handler(users_table):
    user_id = str(uuid.uuid4())
    users_table.put_item(Item={"PK": user_id, "name": "Jhon Doe", "age": 30})

    response = lambda_handler(None, None)

    body = json.loads(response["body"])

    assert body == {
        "users": [
            {"id": user_id, "name": "Jhon Doe", "age": "30"}
        ]
    }
