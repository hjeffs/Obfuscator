import csv
import pytest
from src.obfuscator import obfuscate

def test_obfuscate():
    # Arrange
    input_file = 'files\testdata_1student.csv'
    pii_fields = ['name', 'email_address']
    output_file = 'files\obfuscated_file.csv'

    # Act
    obfuscate(input_file, pii_fields, output_file)

    # Assert
    with open(output_file, mode='r') as test:
        reader = csv.DictReader(test)
        for row in reader:
            assert row['name'] == '***', "Name is obfuscated"
            assert row['email_address'] == '***', "Email is obfuscated"
            assert row['student_id'] != '***', "Student ID is not obfuscated"

def test_obfuscate_no_file():
    # Arrange
    input_file = 'non_existent_file.csv'
    pii_fields = ['name', 'email_address']
    output_file = 'files\obfuscated_file.csv'

    # Act & Assert
    with pytest.raises(FileNotFoundError):
      obfuscate(input_file, pii_fields, output_file)