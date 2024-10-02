from address import extract_city, \
  extract_state, extract_zipcode
import pytest

def test_extract_city():
  """Verify that the extract_city function works correctly.
    Parameters: none
    Return: nothing
    """
  assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
  assert extract_city("123 Main St, Los Angeles, CA 90001") == "Los Angeles"
  assert extract_city("456 Elm St, Austin, TX 73301") == "Austin"

def test_extract_state():
  """Verify that the extract_state function works correctly.
    Parameters: none
    Return: nothing
    """
  assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
  assert extract_state("123 Main St, Los Angeles, CA 90001") == "CA"
  assert extract_state("456 Elm St, Austin, TX 73301") == "TX"

def test_extract_zipcode():
  """Verify that the extract_zipcode function works correctly.
    Parameters: none
    Return: nothing
    """
  assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
  assert extract_zipcode("123 Main St, Los Angeles, CA 90001") == "90001"
  assert extract_zipcode("456 Elm St, Austin, TX 73301") == "73301"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])