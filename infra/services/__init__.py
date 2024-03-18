from infra.services.dynamo_db import DynamoDB
from infra.services.api_gateway import APIGateway
from infra.services.aws_lambda import AWSLambda


class Services:
    def __init__(self, scope, stage, arns) -> None:
        self.api_gateway = APIGateway(scope, stage)
        self.aws_lambda = AWSLambda(scope, stage)
        self.dynamo_db = DynamoDB(scope, arns)
