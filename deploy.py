#!/usr/bin/env python


"""
AWS CloudFormation deployment script

COMMAND is either 'CREATE', 'UPDATE', or 'DELETE'.

CONFIG_FILE contains the infrastructure stack details in
the following JSON format:

{
    "name": "STACK_NAME",
    "region": "REGION",
    "template": "CLOUDFORMATION_TEMPLATE_FILE.yml",
    "parameters": "CLOUDFORMATION_PARAMETERS_FILE.json"
}
"""


import click
import json
import os


def deploy_stack(config_file, command):
    """deploy infrastructure as specified in CloudFormation template"""
    try:
        with open(config_file) as config:
            stack = json.load(config)
    except (FileNotFoundError, IsADirectoryError, PermissionError) as err:
        click.echo(f"ERROR: {err}")
    else:
        exec(f'{command}_stack(**stack)')


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


def delete_stack(name, **kwargs):
    """delete specified stack"""
    os.system(f'aws cloudformation delete-stack'
                  f' --stack-name {name}')


@click.command()
@click.argument('config-file')
@click.option('-c', '--command', required=True, default='update',
               type=click.Choice(['create', 'update', 'delete'],
               case_sensitive=False))
def cli(*, config_file, command):
    """Deploy infrastructure specified in CONFIG_FILE

    CONFIG_FILE contains the infrastructure stack details in JSON format.
    """
    deploy_stack(config_file, command)


if __name__ == '__main__':
    cli()
