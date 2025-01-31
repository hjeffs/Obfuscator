import pandas as pd
from io import StringIO

def read_file(file_content, file_extension):
    print('in read_file.py')

    # Create temp file from content
    temporary_file = StringIO(file_content) 

    # Elif block to read file type
    if file_extension == 'csv':
        return pd.read_csv(temporary_file)
    elif file_extension == 'json':
        return pd.read_json(temporary_file)
    elif file_extension == 'parquet':
        return pd.read_parquet(temporary_file)
    
    # Raise Type Error as no other file types are accepted
    raise TypeError("Invalid File Type", '<<< Read File Error')