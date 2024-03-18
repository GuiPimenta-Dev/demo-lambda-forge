from dataclasses import dataclass
import json
from typing import List, Literal, Optional


@dataclass
class Object:
    a_string: str
    an_int: int


@dataclass
class Input:
    a_string: str
    an_int: int
    a_boolean: bool
    a_list: List[str]
    an_object: Object
    a_literal: Literal["a", "b", "c"]
    an_optional: Optional[str]


@dataclass
class Output:
    message: str



def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello World!"})
    }
