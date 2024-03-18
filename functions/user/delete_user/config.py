from infra.services import Services


class DeleteUserConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="DeleteUser",
            path="./functions/user",
            description="Delete an User",
            directory="delete_user",
            environment={
                "USERS_TABLE": services.dynamo_db.users_table.table_name,
            },
        )

        services.api_gateway.create_endpoint(
            "DELETE", "/users/{id}", function, public=True
        )

        services.dynamodb.users_table.grant_read_write_data(function)
