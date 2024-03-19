import aws_cdk as cdk
from aws_cdk import pipelines as pipelines
from aws_cdk.pipelines import CodePipelineSource
from constructs import Construct
from infra.stages.deploy import DeployStage
from lambda_forge import Steps


class DevStack(cdk.Stack):
    def __init__(self, scope: Construct, **kwargs) -> None:
        name = scope.node.try_get_context("name").title()
        super().__init__(scope, f"Dev-{name}-Stack", **kwargs)

        repo = self.node.try_get_context("repo")
        source = CodePipelineSource.git_hub(f"{repo['owner']}/{repo['name']}", "dev")

        pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            synth=pipelines.ShellStep(
                "Synth",
                input=source,
                install_commands=[
                    "pip install lambda-forge==1.0.86 --extra-index-url https://pypi.org/simple --extra-index-url https://test.pypi.org/simple/",
                    "pip install aws-cdk-lib",
                    "npm install -g aws-cdk",
                ],
                commands=[
                    "cdk synth",
                ],
            ),
            pipeline_name=f"Dev-{name}-Pipeline",
        )

        context = self.node.try_get_context("dev")
        stage = "Dev"

        steps = Steps(self, stage, source)
        show_me_the_dir = steps.show_me_the_dir()
        # unit_tests = steps.run_unit_tests()
        # validate_integration_tests = steps.validate_integration_tests()
        # validate_docs = steps.validate_docs()
        # coverage = steps.run_coverage()
        # generate_docs = steps.generate_docs(name, stage)

        pipeline.add_stage(
            DeployStage(self, stage, context["arns"]),
            pre=[
                show_me_the_dir,
                # coverage,
                # validate_docs,
                # generate_docs,
                # validate_integration_tests,
            ],
        )
