from infra.services import Services


class AuthConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="Auth",
            path="./functions/authorizers",
            description="An authorizer for private lambda functions",
            directory="auth",
        )

        services.api_gateway.create_authorizer(function, name="auth", default=True)
