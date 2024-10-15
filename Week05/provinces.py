def main():
  province_list = read_list("provinces.txt")
  print(province_list)

  # Remove the first element from the list.
  province_list.pop(0)

  # Remove the last element from the list.
  province_list.pop()

  # Replace all occurrences of "AB" in the list with "Alberta".
  for i in range(len(province_list)):
    if province_list[i] == "AB":
      province_list[i] = "Alberta"
  
  count = province_list.count("Alberta")
  print()
  print(f"Alberta occurs {count} times in the modified list.")


def read_list(filename):
  """Reads the content of a text file into a list and
  return the list. Each element in the list will contain
  one line of text from the text file.
  PARAMETER filename: the name of the text file to read
  return a list of strings"""

  text_list = []

  with open(filename, "rt") as text_file:
    for line in text_file:
      clean_line = line.strip()
      text_list.append(clean_line)
  return text_list

# Call main to start this program.
if __name__ == "__main__":
    main()