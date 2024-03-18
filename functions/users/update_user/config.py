from infra.services import Services


class UpdateUserConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="UpdateUser",
            path="./functions/users",
            description="Update an User",
            directory="update_user",
            environment={
                "USERS_TABLE": services.dynamo_db.users_table.table_name,
            },
        )

        services.api_gateway.create_endpoint(
            "PUT", "/users/{id}", function, public=True
        )

        services.dynamo_db.users_table.grant_read_write_data(function)
