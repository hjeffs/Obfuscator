import pandas as pd
import os
from io import BytesIO, StringIO
from obfuscate_data import obfuscate_data

def obfuscate_csv(file_content, pii_fields):
    try:
        print("in OBFUSCATE")
        #open('./files/obfuscated_file.csv', 'w').close() # empty file
        #file_name, file_extension = os.path.splitext(file_to_obfuscate)
        #print(f'File name: {file_name}', '<<< obs_csv')
        #print(f'File type: {file_extension}', '<<< obs_csv')

        # Load csv into dataframe
        temporary_file = StringIO(file_content) # create temp file from content
        dataframe = pd.read_csv(temporary_file)
        #dataframe = pd.read_csv(file_to_obfuscate)
        

        # Filter fields for whitespace / empty strings
        pii_fields = [field for field in pii_fields if field.strip()]

        # fixes no fields adding in another column
        if not pii_fields:      
            byte_stream = BytesIO() 
            dataframe.to_csv(byte_stream, index=False, index_label=False)  
            dataframe.to_csv('./files/obfuscated_file.csv', index=False, index_label=False)    
            #output_csv.seek(0)  
            byte_stream.seek(0)
            return byte_stream


        # Obfuscate pii_fields
        dataframe = obfuscate_data(dataframe, pii_fields)
        print(dataframe, '<<< CSV (OUTPUT)')

        # Save the obfuscated dataframe to a new csv file using StringIO
        #output_csv = StringIO()                         # create file object
        byte_stream = BytesIO() 
        dataframe.to_csv(byte_stream, index=False, index_label=False) 
        #dataframe.to_csv(output_csv, index=False, index_label=False)     # write output
        # False for index and index_label to make the same csv shape     
        dataframe.to_csv('./files/obfuscated_file.csv', index=False, index_label=False)
        dataframe.to_csv('./files/s3_test.csv', index=False, index_label=False)  
        #output_csv.seek(0)                              # set cursor at index 0
        byte_stream.seek(0)

        return byte_stream
    except FileNotFoundError:
        raise FileNotFoundError("Error: Input file not found.", '<<< obs_csv error')
    except Exception as e:
        print(f'Error: {e}', '<<< obs_csv error')
        raise e
    
if __name__ == "__main__":
    obfuscate_csv('./files/testdata_10students.csv', ['name', 'email_address'])