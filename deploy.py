#!/usr/bin/env python


"""
AWS CloudFormation deploy script
"""


import os


def deploy_stack():
    """deploy infrastructure as specified in CloudFormation template"""
    pass


def create_stack(name, template, parameters, region):
    """create stack as specified in CloudFormation template"""
    os.system(f'aws cloudformation create-stack'
                  f' --stack-name {name}'
                  f' --template-body file://{template}'
                  f' --parameters file://{parameters}'
                  f' --capabilities "CAPABILITY_IAM" "CAPABILITY_NAMED_IAM"'
                  f' --region={region}')


def update_stack(name, template, parameters, region):
    """update stack as specified in CloudFormation template"""
    os.system(f'aws cloudformation update-stack'
                  f' --stack-name {name}'
                  f' --template-body file://{template}'
                  f' --parameters file://{parameters}'
                  f' --capabilities "CAPABILITY_IAM" "CAPABILITY_NAMED_IAM"'
                  f' --region={region}')


def delete_stack(name):
    """delete specified stack"""
    os.system(f'aws cloudformation delete-stack'
                  f' --stack-name {name}')
