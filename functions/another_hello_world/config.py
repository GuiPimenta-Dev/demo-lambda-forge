from infra.services import Services

class AnotherHelloWorldConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="AnotherHelloWorld",
            path="./functions/another_hello_world",
            description="A simple hello word",
            
        )

        services.api_gateway.create_endpoint("GET", "/another_hello_world", function)

            