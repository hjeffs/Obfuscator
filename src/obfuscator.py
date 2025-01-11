import csv
import sys

# print(row, flush=True)

def obfuscate(file_to_obfuscate, pii_fields):
  try:
    with open('./files/testdata_10students.csv') as test:
        print ("Starting obfuscation...") # Debug statement
        reader = csv.reader(test, delimiter=',')
        for row in reader:
            print(row, flush=True)
  except FileNotFoundError:
    print("Error: CSV file not found.")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  obfuscate('./files/testdata_10students.csv', 'name')