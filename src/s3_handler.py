import boto3
from file_check import file_check
from botocore import UNSIGNED

s3 = boto3.client('s3', config=boto3.session.Config(signature_version=UNSIGNED))

def s3_handler(s3_location, pii_fields):
    try:
        print('in S3 HANDLER')
        # Extract bucket name and file key from S3 location
        s3_parts = s3_location.replace("s3://", "").split("/", 1)
        bucket_name = s3_parts[0]
        file_key = s3_parts[1]
        file_parts = file_key.split(".")
        file_extension = file_parts[-1]

        # Download the file from S3
        s3_object = s3.get_object(Bucket=bucket_name, Key=file_key)
        file_content = s3_object['Body'].read().decode('utf-8')

        # Obfuscate the file (file_content, pii_fields) args
        # obfuscated_file = obfuscate(file_content, pii_fields, file_extension)
        obfuscated_file = file_check(file_content, pii_fields, file_extension)

        # Upload the obfuscated CSV back to S3
        #obfuscated_file_key = f"obfuscated_{file_key}"
        #s3.put_object(Bucket=bucket_name, Key=obfuscated_file_key, Body=obfuscated_file.getvalue())

        print(obfuscated_file.getvalue())
        return obfuscated_file

    except Exception as e:
        print(f'Error: {e}')
        raise e
    
if __name__ == '__main__':
    s3_handler('s3://xno-bazaar-listing-images/testdata_10students.csv', ['name', 'email_address'])