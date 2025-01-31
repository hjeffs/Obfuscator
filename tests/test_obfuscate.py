import pytest
import io
import pandas as pd
from unittest.mock import patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "obfuscator")))
from obfuscate import obfuscate

# Mocking dependencies
@pytest.fixture
def mock_s3_parser():
    with patch("obfuscate.s3_parser", return_value=(b"col1,col2\nvalue1,value2", "csv")) as mock:
        yield mock

@pytest.fixture
def mock_read_file():
    with patch("obfuscate.read_file", return_value=pd.DataFrame({"col1": ["value1"], "col2": ["value2"]})) as mock:
        yield mock

@pytest.fixture
def mock_obfuscate_data():
    with patch("obfuscate.obfuscate_data", return_value=pd.DataFrame({"col1": ["XXXXX"], "col2": ["value2"]})) as mock:
        yield mock

@pytest.fixture
def mock_write_to_bytestream():
    mock_stream = io.BytesIO()
    with patch("obfuscate.write_to_bytestream", return_value=mock_stream) as mock:
        yield mock

# Unit tests
def test_obfuscate_success(mock_s3_parser, mock_read_file, mock_obfuscate_data, mock_write_to_bytestream):
    byte_stream = obfuscate("s3://bucket/file.csv", ["col1"])
    assert isinstance(byte_stream, io.BytesIO)

def test_obfuscate_empty_pii_fields(mock_s3_parser, mock_read_file, mock_obfuscate_data, mock_write_to_bytestream):
    byte_stream = obfuscate("s3://bucket/file.csv", [" ", ""])
    assert isinstance(byte_stream, io.BytesIO)

def test_obfuscate_file_not_found():
    with patch("obfuscate.s3_parser", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            obfuscate("s3://bucket/missing.csv", ["col1"])

def test_obfuscate_generic_exception():
    with patch("obfuscate.s3_parser", side_effect=Exception("Unexpected error")):
        with pytest.raises(Exception, match="Unexpected error"):
            obfuscate("s3://bucket/error.csv", ["col1"])

# PEP-8 compliance test
def test_pep8_compliance():
    import subprocess
    result = subprocess.run(["flake8", "obfuscator/obfuscate.py"], capture_output=True, text=True)
    assert result.returncode == 0, f"PEP-8 violations:\n{result.stdout}"

# Security vulnerabilities test
def test_security_vulnerabilities():
    import subprocess
    result = subprocess.run(["bandit", "-r", "obfuscator/obfuscate.py"], capture_output=True, text=True)
    assert "No issues identified." in result.stdout or result.returncode == 0, f"Security issues found:\n{result.stdout}"