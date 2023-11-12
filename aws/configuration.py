
# The profile
PROFILE = 'LabInstanceProfile'
REGION='us-east-1'
AVAILABILITY_ZONE = 'us-east-1a'

EC2_CONFIG = {
    'ImageId': 'ami-0ee23bfc74a881de5',
    'service_name': 'ec2',
    'security_group': 'my_sec_group',
    'key_pair': 'key_pair_lab2',
    'instance_type': 'm4.large',
    'worker' :{
    "TagSpecifications": [
        {
            "ResourceType": "instance",
            "Tags": [
                        {'Key': 'lab', 'Value': 'lab2', },
                        {'Key': 'type', 'Value': 'worker', }
            ]
        }
    ]
        
    }, 
    'orchestrator': {
           "TagSpecifications": [
        {
            "ResourceType": "instance",
            "Tags": [
                        {'Key': 'lab', 'Value': 'lab2', },
                        {'Key': 'type', 'Value': 'orchestrator', }
            ]
        }
    ]

        
    }
}


IAM_CONFIG = {
    'service_name': 'iam',
    'role': 'LabRole'
}

ECS_CONFIG = {
    'service_name': 'ecs',
}

CODE_DEPLOY_CONFIG = {
    'service_name': 'codedeploy',
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
            's3Location':{
                'bucket': '',
                'key': '',
                'bundleType': 'zip'

            }
        },
    'worker' : {
        'application_name': 'lab2_worker',
        'group_name' : 'worker_group',
        
        'EC2TagFilters': [
            {
                'Key': 'lab',
                'Value': 'lab2',
                'Type': 'KEY_AND_VALUE'
            },
                        {
                'Key': 'type',
                'Value': 'worker',
                'Type': 'KEY_AND_VALUE'
            },
        ]
    },
    'orchestrator': {
        'application_name': 'lab2_orchestrator',
        'group_name' : 'orchestrator_group',
        
        'EC2TagFilters': [
            {
                'Key': 'lab',
                'Value': 'lab2',
                'Type': 'KEY_AND_VALUE'
            },
            {
                'Key': 'type',
                'Value': 'orchestrator',
                'Type': 'KEY_AND_VALUE'
            },
        ]
    }
}


S3_CONFIG = {
    'service_name': 's3',
    'worker': {
    'bucket': 'lab2-worker-bucket',
    },
    'orchestrator': {
    'bucket': 'lab2-worker-orchestrator',
    },
    
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
