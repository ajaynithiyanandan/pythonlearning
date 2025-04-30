unitprice = input("Enter the unit price of the item:    ")
qty = input('Enter the quantity of item bought: ')
tax=6.25
total=float(unitprice)*int(qty)
total_tax=total*tax/100
total_price=float(total+total_tax)
print("The total price of the item is: ", total_price)
cashpaid=input('Enter the cash paid by customer: ')
change=float(float(cashpaid)-total_price)
print("The change to be returned to the customer is: ", change)