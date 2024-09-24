from datetime import datetime
# I have included stretch challenge 1 and 2

current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
# day_of_week = 0
# testing if it is not Tue or Wed

subtotal = 0
#stretch challenge 2
while True:
  price = float(input("Please enter the price (enter 0 to finish): "))
  if price == 0:
      break
  quantity = int(input("Please enter the quantity: "))
  subtotal += price * quantity

# check if discount applies for Tuesdays and Wednesdays

if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
    discount = subtotal * 0.1
    subtotal -= discount
    print(f"Discount amount: ${discount:.2f}")

else:
    # stretch challenge 1: check if its Tue or Wed and subtotal is less than $50
    if day_of_week == 1 or day_of_week == 2:
        if subtotal < 50:
            additional_amount_needed = 50 - subtotal
            print(f"You need to purchase an additional amount of ${additional_amount_needed:.2f} to receive a discount.")

sales_tax = subtotal * 0.06
total = subtotal + sales_tax

print(f"Sales tax amount: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")
