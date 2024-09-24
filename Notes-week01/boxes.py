import math

no_items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

result = math.ceil(no_items / items_per_box)

print(f"For {no_items} items, packing {items_per_box} items in each box, you will need {result} boxes.")