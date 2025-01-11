import csv

def obfuscate(file_to_obfuscate, pii_fields):
  try:
    with open(file_to_obfuscate) as test:
        print ("Starting obfuscation...") # Debug statement
        print ("Fields to be Obfuscated:", pii_fields)
        reader = csv.reader(test, delimiter=',')
        obfuscated_data = []
        indexes_to_obfuscate =[]

        for row in reader:
          for column in pii_fields:
              if column in row:
                print(column, '<<< column')
                print(row.index(column), '<<< index')
                indexes_to_obfuscate.append(row.index(column))
          print(row)
          
          for index in indexes_to_obfuscate:
              row[index] = '***' # Obfuscated value from brief
          obfuscated_data.append(row)
        
        print(obfuscated_data)

  except FileNotFoundError:
    print("Error: file not found.")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  obfuscate('./files/testdata_10students.csv', ['name', 'email_address'])