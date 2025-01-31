# [Harry Jeffs](https://hjeffs.github.io): Obfuscator
General purpose obfuscation tool designed for GDPR obfuscation to process data being ingested to AWS and intercept personally identifiable information via given fields (pii_fields). 

## Installation
1. Install the package as a pip module

```
pip install git+https://github.com/hjeffs/Obfuscator.git
```

## Usage
2. Setup s3 location and pii_fields

    s3_location should be a string as below:
    ```
    s3_location = 's3://obfuscator/testdata_10students.json'
    ```
    pii_fields should be a list of strings as below:
    ```
    pii_fields = ['name', 'email_address']
    ```

3. Import and invoke the function

    ```
    from obfuscator import obfuscate

    bytestream = obfuscate(s3_location, pii_fields)
    print(bytestream.getvalue())
    ```

## Byte-stream

    obfuscate(s3_location, pii_fields) 

Returns a BytesIO object containing an 
exact copy of the input file but with the sensitive data replaced with obfuscated strings. 

Manipulate this byte-stream to however you require.

## Invocation from Command Line
Create a test script for Command Line Invocation, the script should look like this:

```
from obfuscator import obfuscate
import argparse

# Create the argument parser
parser = argparse.ArgumentParser(description="Process S3 location and PII fields.")

# Add arguments
parser.add_argument("s3_location", type=str, help="S3 bucket location")
parser.add_argument("pii_fields", nargs="+", help="List of PII fields to process")

# Parse the arguments
args = parser.parse_args()

# Command line arguments set as s3_location and pii_fields
s3_location = args.s3_location
pii_fields = args.pii_fields

# Print values (for debugging purposes)
print(f"S3 Location: {s3_location}")
print(f"PII Fields: {pii_fields}")

bytestream = obfuscate(s3_location, pii_fields)
print(bytestream.getvalue())
```
Navigate to the script in your command line and run through Installation:
```
pip install git+https://github.com/hjeffs/Obfuscator.git
```
Once obfuscator is installed from the repo:
```
python "c:/Dev/myscripts/test.py" my-s3-bucket/path field1 field2 field3
```
Note the pii_fields (field1 field2 field3) need to be space-separated values and choose your correct file path inside the string. "c:/Dev/myscripts/test.py" is an example. s3_location is the 3rd command line argument and does not need to be string. 

Users should recieve feedback in the command line to confirm success or diagnose errors.

## Additional Information

This portfolio project was created to spec for [Tech Returners](https://www.techreturners.com/). 

    Harry Jeffs: Data Engineer

[LinkedIn](https://www.linkedin.com/in/harry-jeffs-195545308/)

Make sure you are signed into your IAM AWS credentials on the device you are using. Help can be found [here](https://docs.aws.amazon.com/cli/v1/userguide/cli-authentication-user.html).

If you have previously installed this package, used it and now it is failing, try:

```
pip uninstall obfuscator
```
```
pip install git+https://github.com/hjeffs/Obfuscator.git --no-cache-dir
```

This should remove any cached directories and use the up to date package. 

If you are still having problems implementing the package please contact me.