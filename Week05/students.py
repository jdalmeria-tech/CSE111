# done with the core requirements
# also included the stretch challenge
import csv
def main():
  """Read the contents of a CSV file into a
  dictionary and return the dictionary.
  Parameters
      filename: the name of the CSV file to read.
  Return: a dictionary that contains
      the contents of the CSV file.
  """
  # Index of the ID number column in the students.csv file.
  ID_NUM_INDEX = 0
  NAME_INDEX = 1
  # Call the read_dictionary function and store in a variable.
  students_dict = read_dictionary("students.csv", ID_NUM_INDEX)
  
  # Get a student ID from the user.
  id_num = input("Please enter an I-Number (xxxxxxxxx): ")

  # The I-Numbers are stored in the CSV file as digits only (without
  # any dashes), so we remove all dashes from the user's input.
  id_num = id_num.replace("-", "")

  # Determine if the user input is in the correct format.
  if not id_num.isdigit():
    print("I-Number contains an invalid character")
  else:
    if len(id_num) < 9:
      print("Too few digits invalid format")
    elif len(id_num) > 9:
      print("Too many digits, invalid format")
    else:
      # Check if the student ID is in the dictionary.
      if id_num in students_dict:
        # Find the student ID in the dictionary and
        # Retrieve student's full name
        full_name = students_dict[id_num][NAME_INDEX]
        print(full_name)
      else:
        print(f"No such student")


def read_dictionary(filename, key_column_index):
  """Read the contents of a CSV file into a compound
  dictionary and return the dictionary.
  Parameters
      filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
  Return: a compound dictionary that contains
      the contents of the CSV file.
  """
  # Create an empty dictionary that will
  # store the data from the CSV file.
  dictionary = {}
  # Open the CSV file for reading and store a reference
  # to the opened file in a variable named csv_file.
  with open(filename, "rt") as csv_file:
    # Use the csv module to create a reader object
    # that will read from the opened CSV file.
    reader = csv.reader(csv_file)
    # The first row of the CSV file contains column
    # headings and not data, so this statement skips
    # the first row of the CSV file.
    next(reader)
    # Read the rows in the CSV file one row at a time.
    # The reader object returns each row as a list.
    for row_list in reader:
      # If the current row is not blank, add the
      # data from the current to the dictionary.
      if len(row_list) != 0:
        # From the current row, retrieve the data
        # from the column that contains the key.
        key = row_list[key_column_index]
        # Store the data from the current
        # row into the dictionary.
        dictionary[key] = row_list
  #Return the dictionary.
  return dictionary

# Call main to start this program.
if __name__ == "__main__":
    main()