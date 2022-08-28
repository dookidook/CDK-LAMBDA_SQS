from aws_cdk import (
    aws_iam as iam,
    aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_lambda_event_sources as _aws_lambda_event_sources,
    core
)


class PythonProject1Stack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "PythonProject1Queue",
            visibility_timeout=core.Duration.seconds(300),
        )

        # making Lambda
        sqs_lambda = _lambda.Function(self, 'sqstrigger',
                                      handler='lambda_handler.handler',
                                      runtime=_lambda.Runtime.PYTHON_3_9,  # type: ignore
                                      code=_lambda.Code.asset('lambda')
                                      )

        sqs_event_source = _aws_lambda_event_sources.SqsEventSource(queue)
        # Link SQS event source to the Lambda function
        sqs_lambda.add_event_source(sqs_event_source)
