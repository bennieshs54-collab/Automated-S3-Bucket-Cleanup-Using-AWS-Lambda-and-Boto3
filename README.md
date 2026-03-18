# Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

## Objective
This project demonstrates how to automatically delete files older than 30 days from an AWS S3 bucket using AWS Lambda and Python (Boto3).

## Services Used
- AWS S3
- AWS Lambda
- AWS IAM
- CloudWatch Logs
- Python (Boto3)

## Steps Implemented

1. Created an S3 bucket.
2. Uploaded test files.
3. Created an IAM role with S3 access.
4. Created a Lambda function using Python.
5. Implemented Boto3 code to delete files older than 30 days.
6. Manually triggered the Lambda function.
7. Verified deletion in S3 bucket.

## Lambda Function Logic

- Connect to S3 using Boto3
- List all objects in the bucket
- Check LastModified date
- Delete objects older than 30 days
- Log deleted file names

## Output Example

Deleted file: oldfile1.txt  
Deleted file: oldfile2.txt

## Result

After execution, only files newer than 30 days remain in the S3 bucket.

## Author
Your Name
