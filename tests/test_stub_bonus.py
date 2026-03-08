import pytest
from unittest.mock import patch
from src.api_helpers import process_api_string_for_funny

@patch("src.api_helpers.fetch_string_from_api")
def test_stub_bonus_funny_response(mock_fetch):
    # This is the TEST STUB (คะแนนพิเศษ)
    # mock_fetch will replace fetch_string_from_api during this test.
    # We stub its return value so it doesn't execute the real function (which raises an error)
    mock_fetch.return_value = "acxz"
    
    result = process_api_string_for_funny("http://dummy-url.com")
    
    assert result == "Funny"
    # Ensure the stub was called with the correct argument
    mock_fetch.assert_called_once_with("http://dummy-url.com")

@patch("src.api_helpers.fetch_string_from_api")
def test_stub_bonus_not_funny_response(mock_fetch):
    # Testing another branch using a different STUB response
    mock_fetch.return_value = "bcxz"
    
    result = process_api_string_for_funny("http://dummy-url.com")
    
    assert result == "Not Funny"
    mock_fetch.assert_called_once_with("http://dummy-url.com")
