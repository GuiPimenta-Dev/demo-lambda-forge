from infra.services import Services

class GetUserConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="GetUser",
            path="./functions/user",
            description="Get an User",
            directory="get_user"
        )

        services.api_gateway.create_endpoint("GET", "/user/{id}", function, public=True)

            