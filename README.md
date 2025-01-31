# Obfuscator
General purpose obfuscation tool designed for GDPR obfuscation to process data being ingested to AWS and intercept personally identifiable information (pii). 

## Installation
1. Install the package as a pip module

```
pip install git+https://github.com/hjeffs/Obfuscator.git
```

## Usage
2. Import and invoke the function

```
from obfuscator import functions
functions.obfuscate(file_to_obfuscate, pii_fields)

from obfuscator import obfuscate
obfuscate(s3_location, pii_fields)
```

## Byte-stream
3. obfuscate(s3_location, pii_fields) returns a BytesIO object containing an 
exact copy of the input file but with the sensitive data replaced with obfuscated strings. Save this byte-stream to whatever destination you require.