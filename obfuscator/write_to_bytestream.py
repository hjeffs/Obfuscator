from io import BytesIO

def write_to_bytestream(dataframe, file_extension):
    print('in write_to_bytestream.py')

    # Create bytestream 
    byte_stream = BytesIO()

    # Elif block to send bytestream data as correct type
    if file_extension == 'csv':
        # False for index and index_label to make the same csv shape     
        dataframe.to_csv(byte_stream, index=False, index_label=False)
        # dataframe.to_csv('./files/s3_test.csv', index=False, index_label=False) 
    elif file_extension == 'json':
        # orient="records" outputs a list of dictionaries, same json shape 
        dataframe.to_json(byte_stream, orient="records") 
        # dataframe.to_json('./files/s3_test.json', orient="records", indent=2) 
    elif file_extension == 'parquet':
        # parameters will likely need adjusting for parquet too
        dataframe.to_parquet(byte_stream)
        # dataframe.to_parquet('./files/s3_test.parquet')

    return byte_stream