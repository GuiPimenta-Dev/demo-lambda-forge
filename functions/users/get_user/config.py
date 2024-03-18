from infra.services import Services


class GetUserConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="GetUser",
            path="./functions/users",
            description="Get an User",
            directory="get_user",
            environment={
                "USERS_TABLE": services.dynamo_db.users_table.table_name,
            },
        )

        services.api_gateway.create_endpoint(
            "GET", "/users/{id}", function, public=True
        )

        services.dynamo_db.users_table.grant_read_write_data(function)
