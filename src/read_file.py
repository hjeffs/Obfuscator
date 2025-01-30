import pandas as pd
from io import StringIO

def read_file(file_content, file_extension):
    temporary_file = StringIO(file_content) # create temp file from content
    if file_extension == 'csv':
        return pd.read_csv(temporary_file)
    elif file_extension == 'json':
        return pd.read_json(temporary_file)
    elif file_extension == 'parquet':
        return pd.read_parquet(temporary_file)
    
    raise TypeError("Invalid File Type")
    