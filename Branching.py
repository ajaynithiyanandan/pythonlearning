#Test if number is even or odd
numberval = int(input('Enter your number: '))
if numberval%2==0:
    print('Number is even') 
else:
    print('Number is odd')
    
#Password validation
password = input('Enter your password: ')
nnewpassword = input('Re-enter your password: ')
if password == nnewpassword:
    print('Password is valid')
else:
    print('Password is invalid')
    
# Temprature check
temprature = int(input('Enter the temprature: '))
if temprature > 60 and temprature < 80:
    print('Temprature is normal')
elif temprature < 60:
    print('Temprature is low')
elif temprature > 80:
    print('Temprature is high')
