from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
  """Verify that the make_full_name function works correctly.
    Parameters: none
    Return: nothing
    """
  # call the make_full_name function and verify if it returns a string
  # in the form 'family_name; given_name'
  assert make_full_name("Sally", "Brown") == "Brown; Sally"
  assert make_full_name("Joseph-Dann", "Almeria") == "Almeria; Joseph-Dann"
  assert make_full_name("Alexandria", "Supercalifragilisticexpialidocious") == "Supercalifragilisticexpialidocious; Alexandria"

def test_extract_family_name():
  """Verify that the extract_family_name function works correctly.
    Parameters: none
    Return: nothing
    """
  # call the extract_family_name function and verify if it returns a string
  # in the form of person's family name
  assert extract_family_name("Brown; Sally") == "Brown"
  assert extract_family_name("Almeria; Joseph-Dann") == "Almeria"
  assert extract_family_name("Supercalifragilisticexpialidocious; Alexandria") == "Supercalifragilisticexpialidocious"

def test_extract_given_name():
  """Verify that the extract_given_name function works correctly.
    Parameters: none
    Return: nothing
    """
  # call the extract_given_name function and verify if it returns a string
  # in the form of person's given name
  assert extract_given_name("Brown; Sally") == "Sally"
  assert extract_given_name("Almeria; Joseph-Dann") == "Joseph-Dann"
  assert extract_given_name("Supercalifragilisticexpialidocious; Alexandria") == "Alexandria"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])