# lambda-curator - An Elasticsearch Curator bootstrapper for AWS Lambda.

This is a simple bootstrapper for running the [Elasticsearch Curator](https://github.com/elastic/curator) as an _AWS Lambda_-function. Lambda functions can be triggered using _CloudWatch Events_ making it a suitable environment for running Curator tasks. 

__Note__: Currently Lambda functions have a maximum execution time of 300 seconds so long-running Curator tasks are not suitable for running as Lambda functions.

## Setup
### Environment variables
- __ES_HOST__: the base url of the Elasticsearh cluster (default: http://localhost).
- __ES_PORT__: the Elasticseach cluster port (default: 9200).
- __DRY_RUN__: set Curator _--dry-run_ flag (default: True)
- __FUNCTION_NAME__: the lambda function name (default: lambda-curator).
- __IAM_ROLE__: the lambda function execution role.

### AWS CLI
The [AWS CLI](https://aws.amazon.com/cli/) needs to be installed in order to push/update the _lambda-curator_ function. As a minimum the following variables need to be set:
- __AWS_ACCESS_KEY_ID__: the aws access key id.
- __AWS_SECRET_ACCESS_KEY__: the aws secret access key.
- __AWS_REGION__: the aws region.


## Add actions.yml
Add an actions.yml file with the actions to be triggered by the lambda function.

## Package function
```
make package
```
This will create a _FUNCTION_NAME.zip_ including the bootstrap.py (and all Curator dependencies) and actions.yml.

## Push package to function
```
make awspush
```
This will create and publish the lambda-curator function.

## Update package function
```
make awsupdate
```
This will update any existing lambda-curator function.

## Connecting to an AWS Elasticsearch cluster
The lambda-curator function will sign all requests with the AWS credentials of the execution role (IAM_ROLE). Giving this role access to your AWS Elasticsearch cluster using IAM will authenticate all lambda-curator actions _automagically_.