from infra.services import Services


class ListUsersConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="ListUsers",
            path="./functions/user",
            description="List all users",
            directory="list_users",
            environment={
                "USERS_TABLE": services.dynamo_db.users_table.table_name,
            },
        )

        services.api_gateway.create_endpoint("GET", "/users", function, public=True)

        services.dynamodb.users_table.grant_read_write_data(function)
