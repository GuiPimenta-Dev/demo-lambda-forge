from infra.services import Services


class PublicConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="Public",
            path="./functions/public",
            description="A public function",
        )

        services.api_gateway.create_endpoint("GET", "/public", function, public=True)
