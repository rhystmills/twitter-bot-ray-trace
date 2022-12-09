# 🤖 twitter-bot-ray-trace

Twitter bot that posts raytrayed graphics from [Gif Galaxy (1993) shovelware](http://cd.textfiles.com/gifgalaxy/PIC/). Python bot designed to run on AWS Lambda, scheduled by CloudWatch events. Lives here: [@ray__trace](https://twitter.com/ray__trace)

Fork and add any list of urls to make your own gif bot.

## How to run

The following secrets should be set in a env file in the root:

```
# Environment variables, store credentials here
CONSUMER_KEY="API / Consumer Key here",
CONSUMER_SECRET="API / Consumer Secret here",
ACCESS_TOKEN="Access Token here",
ACCESS_TOKEN_SECRET="Access Token Secret here"
```

To use a virtual environment:
```
pip3 install virtualenv
```
Then creating the virtual environment:
```
pip3 venv
```
Then activate it whenever used with:
```
source ./venv/bin/activate
```

To install dependencies:
```p
pip3 install -r requirements.txt
```

To test:
```
lambda invoke -v
```

To upload to s3:
```
lambda deploy
```

PIL does not play nicely with AWS Lambda. I uninstalled it locally and made sure the Lambda used an `arn` that made it available from [Klayers](https://github.com/keithrozario/Klayers).


You need a config.yaml in the root, with the following structure:

```
region: eu-west-1

function_name: my-lambda-name
handler: service.handler
description: my description
runtime: python3.9
# role: lambda_basic_execution
role: basic_s3_upload
bucket_name: 'my-bucket-name'
s3_key_prefix: 'lambda/'

# if access key and secret are left blank, boto will use the credentials
# defined in the [default] section of ~/.aws/credentials.
aws_access_key_id: idgohere
aws_secret_access_key: keygohere

# Build options
build:
  source_directories: lib # a comma delimited list of directories in your project root that contains source to package.
```
