from functions.docs.swagger.config import SwaggerConfig
from functions.users.list_users.config import ListUsersConfig
from functions.users.delete_user.config import DeleteUserConfig
from functions.users.get_user.config import GetUserConfig
from functions.users.update_user.config import UpdateUserConfig
from functions.users.create_user.config import CreateUserConfig
from functions.authorizers.auth.config import AuthConfig
from functions.private.config import PrivateConfig
from functions.public.config import PublicConfig
from functions.docs.config import DocsConfig
from functions.authorizers.docs_authorizer.config import DocsAuthorizerConfig
from aws_cdk import Stack
from constructs import Construct
from infra.services import Services
from lambda_forge import release

@release
class LambdaStack(Stack):
    def __init__(
        self,
        scope: Construct,
        stage,
        arns,
        **kwargs,
    ) -> None:

        name = scope.node.try_get_context("name")
        super().__init__(scope, f"{name}-CDK", **kwargs)

        self.services = Services(self, stage, arns)

        # Authorizers
        AuthConfig(self.services)
        DocsAuthorizerConfig(self.services)

        # # Docs
        DocsConfig(scope, self.services)
        SwaggerConfig(self.services)

        # # Public
        PublicConfig(self.services)

        # # Private
        PrivateConfig(self.services)

        # # User
        CreateUserConfig(self.services)
        ListUsersConfig(self.services)
        GetUserConfig(self.services)
        UpdateUserConfig(self.services)
        DeleteUserConfig(self.services)
