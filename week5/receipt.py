import csv
from datetime import datetime, timedelta

SALES_TAX_RATE = 0.06
D083_ID = "D083"

def read_dictionary(filename, key_column_index):
    dictionary = {}
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader) 
            
            for row in reader:
                product_number = row[key_column_index]
                dictionary[product_number] = row
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        exit()
    except PermissionError:
        print(f"Error: Permission denied when accessing '{filename}'.")
        exit()
    
    return dictionary

def days_until_new_year():
    current_date = datetime.now()
    next_new_year = datetime(current_date.year + 1, 1, 1)
    delta = next_new_year - current_date
    return delta.days

def return_by_date():
    future_date = datetime.now() + timedelta(days=30)
    return future_date.replace(hour=21, minute=0, second=0, microsecond=0)

def apply_discount(quantity, price):
    if quantity > 1:
        discount_price = price / 2
        total_discount = (quantity // 2) * discount_price
        total_price = (quantity - (quantity // 2)) * price + total_discount
        return total_price, total_discount
    else:
        return quantity * price, 0 

def generate_receipt():
    products_dict = read_dictionary("products.csv", 0)
    order_dict = {}
    subtotal = 0
    num_items = 0
    discount_total = 0

    print("Inkom Emporium")
    print("-------------------------")

    try:
        with open("request.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                product_number = row[0]
                quantity = int(row[1])

                if product_number in products_dict:
                    product_name = products_dict[product_number][1]
                    price = float(products_dict[product_number][2])

                    if product_number == D083_ID:
                        total_price, discount = apply_discount(quantity, price)
                        discount_total += discount
                    else:
                        total_price = price * quantity

                    order_dict[product_name] = {
                        'quantity': quantity,
                        'price': price,
                        'total_price': total_price
                    }

                    subtotal += total_price
                    num_items += quantity
                    print(f"{product_name}: {quantity} @ {price:.2f} (Total: {total_price:.2f})")
                else:
                    print(f"Error: Product {product_number} not found in products catalog!")
                    continue
    except FileNotFoundError:
        print("Error: The file 'request.csv' was not found.")
        exit()
    except PermissionError:
        print("Error: Permission denied when accessing 'request.csv'.")
        exit()

    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

    print("-------------------------")
    print(f"Number of Items: {num_items}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")

    if discount_total > 0:
        print(f"Discount on {D083_ID} applied: {discount_total:.2f}")

    print("Thank you for shopping at the Inkom Emporium.")

    current_date_and_time = datetime.now()
    print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")

    print(f"Days until New Year's Sale: {days_until_new_year()} days")

    return_date = return_by_date()
    print(f"Return by: {return_date:%a %b %d %H:%M:%S %Y}")

    coupon_product = list(order_dict.keys())[0]  
    print(f"Coupon: Get 10% off on {coupon_product} on your next purchase!")

if __name__ == "__main__":
    generate_receipt()
