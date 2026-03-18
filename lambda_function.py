import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')

BUCKET_NAME = 'lambda-s3-cleanup-bucket-123'

def lambda_handler(event, context):
    
    # Calculate date 30 days ago
    days_30_ago = datetime.now(timezone.utc) - timedelta(days=30)

    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    if 'Contents' in response:
        for obj in response['Contents']:
            file_name = obj['Key']
            last_modified = obj['LastModified']

            # Check if file is older than 30 days
            if last_modified < days_30_ago:
                s3.delete_object(
                    Bucket=BUCKET_NAME,
                    Key=file_name
                )

                print(f"Deleted file: {file_name}")

    return {
        'statusCode': 200,
        'body': 'Cleanup completed'
    }
