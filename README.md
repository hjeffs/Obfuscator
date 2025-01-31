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

## Additional Information

This portfolio project was created to spec for [Tech Returners](https://www.techreturners.com/). 

        Harry Jeffs: Data Engineer

[LinkedIn](https://www.linkedin.com/in/harry-jeffs-195545308/)

If you have previously installed this package, used it and now it is failing, try:

    pip uninstall obfuscator

    pip install git+https://github.com/hjeffs/Obfuscator.git --no-cache-dir

This should remove any cached directories and use the up to date package. 

If you are still having problems implementing the package please contact me.