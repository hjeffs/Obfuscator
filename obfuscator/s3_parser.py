import boto3
from io import BytesIO

# client to be done as anonymous
#from botocore import UNSIGNED
#s3 = boto3.client('s3', config=boto3.session.Config(signature_version=UNSIGNED))

# local client once user is signed into their AWS credentials
s3 = boto3.client('s3')

def s3_parser(s3_location):
    try:
        # print('in s3_parser.py')
        # Extract bucket name, file key and extension from S3 location
        s3_parts = s3_location.replace("s3://", "").split("/", 1)
        bucket_name = s3_parts[0]
        file_key = s3_parts[1]
        file_parts = file_key.split(".")
        file_extension = file_parts[-1]
    
        # Download the file from S3
        s3_object = s3.get_object(Bucket=bucket_name, Key=file_key)
        
        if file_extension == 'parquet':
            file_content = BytesIO(s3_object['Body'].read())
        else:
            file_content = s3_object['Body'].read().decode('utf-8')


        # Return the file content
        # print([file_content, file_extension])
        return [file_content, file_extension]

    except Exception as e:
        print(f'Error: {e}')
        raise e
    
if __name__ == '__main__':
    s3_parser('s3://obfuscator/testdata_10students.json')