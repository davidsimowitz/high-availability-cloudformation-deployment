Deploy a High-Availability Web App using CloudFormation
=======================================================


Udacity - Cloud DevOps Engineer Nanodegree
------------------------------------------
Deploy Infrastructure as Code Project: Deploy a High-Availability Web App using CloudFormation

In this project, you’ll deploy web servers for a highly available web app using CloudFormation. You will write the code that creates and deploys the infrastructure and application for an Instagram-like app from the ground up. You will begin with deploying the networking components, followed by servers, security roles and software. The procedure you follow here will become part of your portfolio of cloud projects. You’ll do it exactly as it’s done on the job - following best practices and scripting as much as possible.


Infrastructure Diagram
----------------------

![High-Availability Web Application Infrastructure Diagram](https://github.com/davidsimowitz/high-availability-deployment/blob/master/project-infrastructure-diagram.jpeg)


Requirements
------------

+ A Web Browser such as [Chrome](https://www.google.com/chrome/browser/) or [Firefox](https://www.mozilla.org/en-US/firefox/new/) is installed.

+ An [AWS Account](https://aws.amazon.com/)

+ The [AWS Command Line Interface](https://aws.amazon.com/cli/) for running the Cloudformation script

+ [Python 3](https://www.python.org/downloads/) and [click](https://pypi.org/project/click/) if using the supplied deployment script.


Usage
-----

+ Run the CloudFormation script from the terminal(bash) using one of the following methods:
  * If you have Python 3 (Python 3.6+) installed, use the supplied deployment script:
      ```bash
      $ ./deploy.py -c create config.json
      ```
  * Using the supplied shell script:
      ```bash
      $ ./create.sh Udacity-IaC-Project infrastructure.yml parameters.json
      ```
  * Directly from the terminal:
      ```bash
      $ aws cloudformation create-stack --stack-name Udacity-IaC-Project --template-body file://infrastructure.yml --parameters file://parameters.json --capabilities "CAPABILITY_IAM" "CAPABILITY_NAMED_IAM" --region=us-west-2
      ```

+ To update the CloudFormation stack (after it has been created and only after the template/parameters have been modified) use one of the following methods:
  * If you have Python 3 (Python 3.6+) installed, use the supplied deployment script:
      ```bash
      $ ./deploy.py -c update config.json
      ```
  * Using the supplied shell script:
      ```bash
      $ ./update.sh Udacity-IaC-Project infrastructure.yml parameters.json
      ```
  * Directly from the terminal:
      ```bash
      $ aws cloudformation update-stack --stack-name Udacity-IaC-Project --template-body file://infrastructure.yml --parameters file://parameters.json --capabilities "CAPABILITY_IAM" "CAPABILITY_NAMED_IAM" --region=us-west-2
      ```

+ Access the high availability web app using the [DNS name address](http://DEV-LOAD-BALANCER-us-west-2-1571534536.us-west-2.elb.amazonaws.com) of the application load balancer.


Files
-----

+ config.json
+ create.sh
+ delete.sh
+ deploy.py
+ infrastructure.yml
+ parameters.json
+ project-infrastructure-diagram.jpeg
+ project-infrastructure-diagram.pdf
+ README.md
+ update.sh


Application Load Balancer URL
-----------------------------

+ http://DEV-LOAD-BALANCER-us-west-2-1571534536.us-west-2.elb.amazonaws.com


Delete CloudFormation Stack
---------------------------

+ To delete the CloudFormation stack use one of the following methods:
  * If you have Python 3 (Python 3.6+) installed, use the supplied deployment script:
      ```bash
      $ ./deploy.py -c delete config.json
      ```
  * Using the supplied shell script:
      ```bash
      $ ./delete.sh Udacity-IaC-Project
      ```
  * Directly from the terminal:
      ```bash
      $ aws cloudformation delete-stack --stack-name Udacity-IaC-Project
      ```
