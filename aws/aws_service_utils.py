"""
AWS service utils file
"""

import boto3

# create the aws service (ec2, ami, elb,..)
def create_aws_service(service, region):
    aws_service = boto3.client(
            service_name=service,
            region_name=region,
        )
    print(f'Service {service} is created')
    return aws_service
