from infra.services import Services

class DeleteUserConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="DeleteUser",
            path="./functions/user",
            description="Delete an User",
            directory="delete_user"
        )

        services.api_gateway.create_endpoint("DELETE", "/user/{id}", function, public=True)

            