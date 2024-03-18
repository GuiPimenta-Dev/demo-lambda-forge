from infra.services import Services

class ListUsersConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="ListUsers",
            path="./functions/user",
            description="List all users",
            directory="list_users"
        )

        services.api_gateway.create_endpoint("GET", "/user", function, public=True)

            