mealprice=float(input("Enter the meal price: "))
noofcustomers=int(input("Enter the number of customers: "))
tippercent=18
taxpercent=6.25
total_price = mealprice + (mealprice*tippercent/100) + (mealprice*taxpercent/100)
print("The total price of the meal is: ", total_price)
print("The total price of the meal per customer is: ", total_price/noofcustomers)