from functions.authorizers.auth.config import AuthConfig
from functions.docs.config import DocsConfig
from functions.authorizers.docs_authorizer.config import DocsAuthorizerConfig
from aws_cdk import Stack
from constructs import Construct
from functions.private.config import PrivateConfig
from functions.public.config import PublicConfig
from functions.users.create_user.config import CreateUserConfig
from functions.users.delete_user.config import DeleteUserConfig
from functions.users.get_user.config import GetUserConfig
from functions.users.list_users.config import ListUsersConfig
from functions.users.update_user.config import UpdateUserConfig
from infra.services import Services


class LambdaStack(Stack):
    def __init__(
        self,
        scope: Construct,
        stage,
        arns,
        **kwargs,
    ) -> None:

        name = scope.node.try_get_context("name")
        super().__init__(scope, f"{name}-Lambda-Stack", **kwargs)

        self.services = Services(self, stage, arns)

        # Authorizers
        AuthConfig(self.services)

        # Docs
        DocsConfig(scope, self.services)

        # Private
        PrivateConfig(self.services)

        # Public
        PublicConfig(self.services)

        # Users
        CreateUserConfig(self.services)
        ListUsersConfig(self.services)
        GetUserConfig(self.services)
        UpdateUserConfig(self.services)
        DeleteUserConfig(self.services)
