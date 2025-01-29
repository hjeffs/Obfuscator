import os
from obfuscate_csv import obfuscate_csv

def file_check(file_to_obfuscate, pii_fields):
    file_name, file_extension = os.path.splitext(file_to_obfuscate)
    print(f'File name: {file_name}', '<<< FILE CHECK')
    print(f'File type: {file_extension}', '<<< FILE CHECK')
    if file_extension == '.csv':
       output_file = obfuscate_csv(file_to_obfuscate, pii_fields)

    #if file_extension == '.json':
       #output_file = obfuscate_csv(file_to_obfuscate, pii_fields)
       #output_file = obfuscate_json(file_to_obfuscate, pii_fields)

    #if file_extension == '.parquet':
       #output_file = obfuscate_parquet(file_to_obfuscate, pii_fields)

    return output_file

if __name__ == "__main__":
  file_check('./files/testdata_10students.csv', ['student_id', 'email_address'])