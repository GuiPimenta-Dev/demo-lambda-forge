from infra.services import Services

class UpdateUserConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="UpdateUser",
            path="./functions/user",
            description="Update an User",
            directory="update_user"
        )

        services.api_gateway.create_endpoint("PUT", "/user/{id}", function, public=True)

            