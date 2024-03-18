from aws_cdk import aws_lambda as _lambda


class Layers:
    def __init__(self, scope) -> None:

        self.layer = _lambda.LayerVersion.from_layer_version_arn(
            scope,
            id="Layer",
            layer_version_arn="",
        )
