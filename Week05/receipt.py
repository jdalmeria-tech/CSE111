import csv
from datetime import datetime, timedelta

def main():
    PRODUCT_NUM_INDEX = 0
    NAME_PRODUCT_INDEX = 1
    PRICE_INDEX = 2
    SALES_TAX_RATE = 0.06

    try:
        # Read the products.csv file into a dictionary
        products_dict = read_dictionary("products.csv", PRODUCT_NUM_INDEX)
        
        # Store name at the top of the receipt
        print("=== Welcome to JD's ===")

        print("\nOrdered Items")
        total_items = 0
        subtotal = 0

        # Open the request.csv file and process its contents
        with open("request.csv", "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            # Loop through each row in the request.csv file
            for row in reader:
                product_number = row[0]  
                quantity_requested = int(row[1])

                # Look up the product in the products_dict
                product_info = products_dict.get(product_number)
                
                if product_info:
                    product_name = product_info[NAME_PRODUCT_INDEX]
                    product_price = float(product_info[PRICE_INDEX])

                    # Print the product name, requested quantity, and product price in the correct format
                    print(f"{product_name}: {quantity_requested} @ {product_price:.2f}")
                    total_items += quantity_requested
                    subtotal += quantity_requested * product_price
                else:
                    print(f"Product number {product_number} not found in products dictionary.")

        # Print the total number of ordered items and subtotal
        print(f"\nTotal Items: {total_items}")
        print(f"Subtotal: ${subtotal:.2f}")

        # Compute and print the sales tax
        sales_tax = subtotal * SALES_TAX_RATE
        print(f"Sales Tax: ${sales_tax:.2f}")

        # Compute and print the total amount due
        total = subtotal + sales_tax
        print(f"Total Amount Due: ${total:.2f}")

        # Print thank you message
        print("\nThank you for shopping with us!")

        # Get the current date and time from the system
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime("%a %b %d")
        formatted_time = current_datetime.strftime("%I:%M %p")
        print(f"\nDate and Time: {formatted_date} {formatted_time}")

        # Compute and print days until New Year's Sale (Jan 1)
        new_year = datetime(current_datetime.year + 1, 1, 1)
        days_until_new_year = (new_year - current_datetime).days
        print(f"Reminder: Only {days_until_new_year} days until the New Year's Sale!")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except PermissionError as perm_error:
        print(f"Error: {perm_error}")
    except KeyError as key_error:
        print(f"Error: Product {key_error} not found in products dictionary.")

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary."""
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list

    return dictionary

# Call main to start the program
if __name__ == "__main__":
    main()
