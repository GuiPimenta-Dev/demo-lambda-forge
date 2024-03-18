from infra.services import Services

class SwaggerConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="Swagger",
            path="./functions/docs",
            description="An example with all docs features",
            directory="swagger"
        )

        services.api_gateway.create_endpoint("POST", "/docs", function, public=True)

            