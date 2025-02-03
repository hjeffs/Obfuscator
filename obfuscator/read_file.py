import pandas as pd
from io import StringIO

def read_file(file_content, file_extension):
    # print('in read_file.py')

    # Elif block to read file type
    if file_extension == 'csv':
        # Create temp file from content
        temporary_file = StringIO(file_content) 
        return pd.read_csv(temporary_file)
    elif file_extension == 'json':
        temporary_file = StringIO(file_content) 
        return pd.read_json(temporary_file)
    elif file_extension == 'parquet':
        # Read file_content as parquet has been set to BytesIO in s3_parser
        return pd.read_parquet(file_content)
    
    # Raise Type Error as no other file types are accepted
    raise TypeError("Invalid File Type", '<<< Read File Error')