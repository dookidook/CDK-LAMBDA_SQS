import json
import pytest

from aws_cdk import core
from python_project1.python_project1_stack import PythonProject1Stack


def get_template():
    app = core.App()
    PythonProject1Stack(app, "python-project1")
    return json.dumps(app.synth().get_stack("python-project1").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
