
# The profile
PROFILE = 'LabInstanceProfile'
REGION='us-east-1'
AVAILABILITY_ZONE = 'us-east-1a'

EC2_CONFIG = {
    'ImageId': 'ami-0ee23bfc74a881de5',
    'service_name': 'ec2',
    'security_group': 'my_sec_group',
    'key_pair': 'my_key_pair',
    'instance_type': 'm4.large',
}


IAM_CONFIG = {
    'service_name': 'iam',
    'role': 'LabRole'
}


CODE_DEPLOY_CONFIG = {
    'service_name': 'codedeploy',
    'application_name': 'lab2_app',
    'DeploymentConfigName': 'CodeDeployDefault.OneAtATime',
    'AutoRollbackConfiguration': {
            'enabled': True,
            'events': ['DEPLOYMENT_FAILURE']
        },
    'DeploymentStyle': {
            'deploymentType': 'IN_PLACE',
            'deploymentOption': 'WITHOUT_TRAFFIC_CONTROL'
        },
    'Revision': {
            'revisionType': 'S3',
        },
   



}

S3_CONFIG = {
    'service_name': 's3',
    'bucket': 'log8415-lab2-bucket',
    'bucket_policy': {
        "Statement": [
            {
                    "Action": ["s3:PutObject"],
                    "Effect": "Allow",
            },
            {
                "Action": [
                    "s3:Get*",
                    "s3:List*"
                ],
                "Effect": "Allow",
            }
        ]
    }
}


STS_CONFIG = {
    'service_name': 'sts'
}

CLOUD_WATCH_CONFIG = {
    'service_name': 'cloudwatch'

}
