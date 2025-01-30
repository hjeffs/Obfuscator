import pandas as pd
from io import BytesIO

def write_to_bytestream(dataframe, file_extension):
    byte_stream = BytesIO()

    if file_extension == 'csv':
        # False for index and index_label to make the same csv shape     
        dataframe.to_csv(byte_stream, index=False, index_label=False) # write output
        dataframe.to_csv('./files/s3_test.csv', index=False, index_label=False) # test
    elif file_extension == 'json':
        dataframe.to_json(byte_stream)
        dataframe.to_json('./files/s3_test.json') # test
    elif file_extension == 'parquet':
        dataframe.to_parquet(byte_stream)

    return byte_stream