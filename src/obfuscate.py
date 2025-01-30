import pandas as pd
from read_file import read_file
from obfuscate_data import obfuscate_data
from write_to_bytestream import write_to_bytestream

def obfuscate(file_content, pii_fields, file_extension):
    try:
        print("in OBFUSCATE")
        # Call read_file to create dataframe
        dataframe = read_file(file_content, file_extension)

        # Filter fields for whitespace / empty strings
        pii_fields = [field for field in pii_fields if field.strip()]

        # Obfuscate pii_fields
        dataframe = obfuscate_data(dataframe, pii_fields)
        print(dataframe, '<<< (OUTPUT)')

        byte_stream = write_to_bytestream(dataframe, file_extension)
        byte_stream.seek(0)

        return byte_stream
    except FileNotFoundError:
        raise FileNotFoundError("Error: Input file not found.", '<<< obs error')
    except Exception as e:
        print(f'Error: {e}', '<<< obs_csv error')
        raise e
    
if __name__ == "__main__":
    with open("./files/testdata_10students.csv", "r", encoding="utf-8") as f:
        csv_string = f.read()
    obfuscate(csv_string, ['name', 'email_address'], 'csv')