import csv

def obfuscate(file_to_obfuscate, pii_fields):
  try:
    with open(file_to_obfuscate) as input:
        reader = csv.DictReader(input)
        fields = reader.fieldnames
        print ("Starting obfuscation...") # Debug statement
        print ("All fields:", fields)
        print ("Fields to be Obfuscated:", pii_fields)

        obfuscated_data = []

        for row in reader:
          for field in pii_fields:
              if field in row:
                # print(field, '<<< field')
                row[field] = '***' # Obfuscated value from brief
                obfuscated_data.append(row)
          # print(row)
        
        print(obfuscated_data)

  except FileNotFoundError:
    print("Error: file not found.")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  obfuscate('./files/testdata_10students.csv', ['name', 'email_address'])