from aws_cdk import aws_dynamodb as dynamo_db
from aws_cdk import aws_iam as iam
from aws_cdk import aws_stepfunctions_tasks as sfn_tasks


class DynamoDB:
    def __init__(self, scope, arns: dict) -> None:

        self.users_table = dynamo_db.Table.from_table_arn(
            scope,
            "UsersTable",
            arns["users_table"],
        )

    @staticmethod
    def add_query_permission(function, table):
        function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:Query"],
                resources=[f"{table.table_arn}/index/*"],
            )
        )
