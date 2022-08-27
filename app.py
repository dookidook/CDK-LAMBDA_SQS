#!/usr/bin/env python3

from aws_cdk import core

from python_project1.python_project1_stack import PythonProject1Stack


app = core.App()
PythonProject1Stack(app, "python-project1")

app.synth()
