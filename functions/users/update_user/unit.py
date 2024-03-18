import json
import uuid
from .main import lambda_handler


def test_lambda_handler(users_table):
    user_id = str(uuid.uuid4())
    users_table.put_item(Item={"PK": user_id, "name": "Jhon Doe", "age": 30})
    
    event = {
            "pathParameters": {
                "id": user_id
            },
            "body": json.dumps({"name": "John Doe", "age": 31})
     }
    response = lambda_handler(event, None)
    response = json.loads(response["body"])

    user = users_table.get_item(Key={"PK": user_id})["Item"]
    assert user["name"] == "John Doe"
    assert user["age"] == 31
