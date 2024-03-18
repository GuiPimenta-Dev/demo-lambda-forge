import json
from .main import lambda_handler


def test_lambda_handler(users_table):
    event = {"body": json.dumps({"name": "John", "age": 30})}
    response = lambda_handler(event, None)
    
    response = json.loads(response["body"])

    user = users_table.get_item(Key={"PK": response["id"]})["Item"]
    assert user["name"] == "John"
    assert user["age"] == 30