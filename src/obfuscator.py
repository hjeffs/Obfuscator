import os
import csv

def obfuscate(file_to_obfuscate, pii_fields, obfuscated_file):
  file_name, file_extension = os.path.splitext(file_to_obfuscate)
  print ("File name:", file_name)
  print ("File Extension:", file_extension)

  try:
    with open(file_to_obfuscate) as input:
        reader = csv.DictReader(input)    # Reads csv into DataFrame
        fields = reader.fieldnames
        
        print ("Starting obfuscation...") # Debug statement
        print ("All fields:", fields)
        print ("Fields to be Obfuscated:", pii_fields)

        obfuscated_data = []

        for row in reader:
          for field in pii_fields:
              if field in row:
                row[field] = '***' # Obfuscated value from brief
          obfuscated_data.append(row)
        
        print("Obfuscated Data:", obfuscated_data)
      
    with open(obfuscated_file, mode='w', newline='') as output:
        writer = csv.DictWriter(output, fieldnames=fields)
        if fields != None:        # Empty file check
          writer.writeheader()
        writer.writerows(obfuscated_data)
    
    return obfuscated_file

  except FileNotFoundError:
    raise FileNotFoundError("Error: Input file not found.")
  except Exception as e:
    print(f'Error: {e}')
    raise e

if __name__ == "__main__":
  obfuscate('./files/testdata_10students.csv', ['name', 'email_address'], './files/obfuscated_file.csv')