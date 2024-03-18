from infra.services import Services

class CreateUserConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="CreateUser",
            path="./functions/user",
            description="Create a User",
            directory="create_user"
        )

        services.api_gateway.create_endpoint("POST", "/user", function)

            