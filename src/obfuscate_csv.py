import pandas as pd
from io import StringIO
from obfuscate_data import obfuscate_data

def obfuscate_csv(file_to_obfuscate, pii_fields):
    try:
        # Load csv into dataframe
        dataframe = pd.read_csv(file_to_obfuscate)

        # Filter fields for whitespace / empty strings
        pii_fields = [field for field in pii_fields if field.strip()]

        # fixes no fields adding in another column
        if not pii_fields:      
            output_csv = StringIO()  
            dataframe.to_csv(output_csv, index=False)  
            output_csv.seek(0)  
            return output_csv


        # Obfuscate pii_fields
        dataframe = obfuscate_data(dataframe, pii_fields)
        print(dataframe, '<<< CSV')

        # Save the obfuscated dataframe to a new csv file using StringIO
        output_csv = StringIO()                         # create file object
        dataframe.to_csv(output_csv, index='False')     # write output
        output_csv.seek(0)                              # set cursor at index 0

        return output_csv
    except FileNotFoundError:
        raise FileNotFoundError("Error: Input file not found.")
    except Exception as e:
        print(f'Error: {e}')
        raise e
    
if __name__ == "__main__":
  obfuscate_csv('./files/testdata_10students.csv', ['name', 'email_address'])