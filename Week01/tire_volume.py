import datetime
import math
#with stretch challenge 1 and 2

# get the current date
current_date = datetime.date.today()

r = math.pi
width = int(input("Enter the width of the tire in mm (ex 205): "))
a_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

#calculation
numerator = (r * (width**2) * a_ratio) * ((width*a_ratio) + (2540 * diameter))
denominator = 10000000000
volume = float(numerator / denominator)

# stretch challenge 1
if width == 225 and a_ratio == 60 and diameter == 15:
  price = 260.00

elif width == 205 and a_ratio == 60 and diameter == 15:
  price = 190.99

elif width == 195 and a_ratio == 65 and diameter == 15:
  price = 163.99

elif width == 190 and a_ratio <= 60 and diameter <= 15:
  price = 159.99

else:
  price = 149.45

print(f"The price is ${price:.2f}/tire.")
print(f"The approximate volume is {volume:.2f} liters")

# stretch challenge 2
buy_tires = input("Do you want to buy tires with these dimentions? (yes/no): ").strip().lower()

# variable to store the phone number
phone_number = None

if buy_tires == "yes":
  phone_number = input("Please enter your phone number: ").strip()

# open file in append mode and write the data with indentation
with open("volumes.txt", "a") as file:
  # check if the file is empty to avoid extra spaces on the first line
  if file.tell() != 0:
    file.write("            ") #12 spaces
  # write the basic information
  file.write(f"{current_date}, {width}, {a_ratio}, {diameter}, {volume:.2f}")

  #if the user wants to buy tires, append the phone number
  if phone_number:
    file.write(f", {phone_number}")
  file.write("\n")
