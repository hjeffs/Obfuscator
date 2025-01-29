import pandas as pd
import os
from io import StringIO
from obfuscate_data import obfuscate_data

def obfuscate_csv(file_to_obfuscate, pii_fields):
    try:
        open('./files/obfuscated_file.csv', 'w').close() # empty file
        file_name, file_extension = os.path.splitext(file_to_obfuscate)
        print(f'File name: {file_name}', '<<< obs_csv')
        print(f'File type: {file_extension}', '<<< obs_csv')

        # Load csv into dataframe
        # index_col= 0 ignores first column 
        # caused problem obfuscating student_id
        dataframe = pd.read_csv(file_to_obfuscate, index_col=0) 

        # method works for json too
        if file_extension == '.json':
            dataframe = pd.read_json(file_to_obfuscate)

        # Filter fields for whitespace / empty strings
        pii_fields = [field for field in pii_fields if field.strip()]

        # fixes no fields adding in another column
        if not pii_fields:      
            output_csv = StringIO()  
            dataframe.to_csv(output_csv, index=False)  
            dataframe.to_csv('./files/obfuscated_file.csv', index='False')    
            output_csv.seek(0)  
            return output_csv


        # Obfuscate pii_fields
        dataframe = obfuscate_data(dataframe, pii_fields)
        print(dataframe, '<<< CSV (OUTPUT)')

        # Save the obfuscated dataframe to a new csv file using StringIO
        output_csv = StringIO()                         # create file object
        dataframe.to_csv(output_csv, index='False')     # write output
        dataframe.to_csv('./files/obfuscated_file.csv', index='False')     
        output_csv.seek(0)                              # set cursor at index 0

        return output_csv
    except FileNotFoundError:
        raise FileNotFoundError("Error: Input file not found.")
    except Exception as e:
        print(f'Error: {e}')
        raise e
    
if __name__ == "__main__":
    obfuscate_csv('./files/testdata_10students.csv', ['name', 'email_address'])