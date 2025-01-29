import pytest
import pandas as pd
from src.obfuscate_csv import obfuscate_csv

""" 
from obfuscate_data import obfuscate_data
replaced with
from src.obfuscate_data import obfuscate_data 
in obfuscate_csv.py to run test suite
"""

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

def test_obfuscate_csv_no_field():
    # Arrange 
    input_file = './files/testdata_10students.csv'
    pii_fields = []
    output_file = './files/obfuscated_file.csv'

    # Act 
    obfuscate_csv(input_file, pii_fields)   

    expected_df = pd.read_csv(input_file)
    print(expected_df, '<<< EXPECTED')

    result_df = pd.read_csv(output_file)
    print(result_df, '<<< RESULT')

    # Assert
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_obfuscate_csv_empty_field():
    # Arrange 
    input_file = './files/testdata_10students.csv'
    pii_fields = ['']
    output_file = './files/obfuscated_file.csv'

    # Act 
    obfuscate_csv(input_file, pii_fields)

    expected_df = pd.read_csv(input_file)
    print(expected_df, '<<< EXPECTED')

    result_df = pd.read_csv(output_file)
    print(result_df, '<<< RESULT')

    # Assert
    pd.testing.assert_frame_equal(result_df, expected_df)