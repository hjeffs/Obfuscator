import pytest
import csv
from src.obfuscate_csv import obfuscate_csv

def test_obfuscate_csv_no_file():
    # Arrange
    file_to_obfuscate = ''
    pii_fields = ['name', 'email_address']

    # Act & Assert
    with pytest.raises(FileNotFoundError):
        obfuscate_csv(file_to_obfuscate, pii_fields)

def test_obfuscate_csv_bad_file():
    # Arrange
    input_file = 'non_existent_file.csv'
    pii_fields = ['name', 'email_address']

    # Act & Assert
    with pytest.raises(FileNotFoundError):
      obfuscate_csv(input_file, pii_fields)

def test_obfuscate_csv_empty_file():
    # Arrange
    input_file = './files/empty.csv'
    pii_fields = ['name', 'email_address']

    # Act & Assert
    with pytest.raises(Exception):
        obfuscate_csv(input_file, pii_fields)