import pandas as pd
from read_file import read_file
from obfuscate_data import obfuscate_data
from write_to_bytestream import write_to_bytestream
from s3_parser import s3_parser

def obfuscate(s3_location, pii_fields):
    try:
        print("in obfuscate.py")
        # Parse s3 input
        [file_content, file_extension] = s3_parser(s3_location)

        # Call read_file to create dataframe
        dataframe = read_file(file_content, file_extension)

        # Filter fields for whitespace and/or empty strings
        pii_fields = [field for field in pii_fields if field.strip()]

        # Obfuscate pii_fields
        dataframe = obfuscate_data(dataframe, pii_fields)
        print(dataframe, '<<< DATA (OUTPUT)', 'in obfuscate.py')

        # Write to bytesteam to return
        byte_stream = write_to_bytestream(dataframe, file_extension)
        byte_stream.seek(0)
        
        print(f'{byte_stream} in obfuscate.py')
        return byte_stream
    except FileNotFoundError:
        raise FileNotFoundError("Error: Input file not found.", '<<< obfuscate.py error')
    except Exception as e:
        print(f'Error: {e}', '<<< obfuscate.py error')
        raise e
    
if __name__ == "__main__":
    obfuscate('s3://obfuscator/testdata_10students.parquet', ['name', 'email_address'])