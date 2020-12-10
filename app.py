#!/usr/bin/env python3

from aws_cdk import core

from s3_cloudfront.s3_cloudfront_stack import S3CloudfrontStack


app = core.App()
S3CloudfrontStack(app, "s3-cloudfront")

app.synth()
