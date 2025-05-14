# This program will print all numbers from a starting number to an ending number.
startnumber = int(input('Enter starting number: '))
endnumber = int(input('Enter ending number: '))
# Check if start number is less than end number
if startnumber < endnumber:
    pointer=startnumber
    while pointer <= endnumber:
        print(pointer)
        pointer += 1 # Increment pointer by 1s
        
# Double Number
number=int(input('Enter a number: '))
while number < 10000000:
    number = number * 2 # Double the number
    print(number) # Print the doubled number

for i in range(0,9):
    print(i) # Print the number from 0 to 8