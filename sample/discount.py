from datetime import datetime

DISCOUNT_RATE = 0.10
TAX_RATE = 0.06

current_date = datetime.now()
day_of_week = current_date.weekday() 

subtotal = 0.0

print("Enter the products. To finish, enter 0 as the price.")

while True:
    price = float(input("Product price: "))
    
    if price == 0:
        break  
    
    quantity = int(input("Quantity: "))
    
    subtotal += price * quantity  

print(f"\nSubtotal: ${subtotal:.2f}")

if day_of_week in [1, 2]:  
    if subtotal >= 50:
        discount = round(subtotal * DISCOUNT_RATE, 2)
        print(f"Discount applied: ${discount:.2f}")
        subtotal -= discount
    else:
        missing_amount = 50 - subtotal
        print(f"If you spend ${missing_amount:.2f} more, you'll receive a 10% discount.")


sales_tax = round(subtotal * TAX_RATE, 2)
print(f"Sales tax: ${sales_tax:.2f}")

total = subtotal + sales_tax
print(f"Total to pay: ${total:.2f}")

#Completed 