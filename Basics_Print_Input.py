reeivername = input('Enter Receiver\'s name: ')
myfirstname = input('Enter your first name: ')
mylastname = input('Enter your last name:')
location = input('Enter your location:  ')
noprograms = input('Enter the number of programs you have coded: ')
date = input('Enter the date: ')

print('''
Dear ''' + reeivername + '''
This is ''' + myfirstname + ''' I'm writing to let you know that the weather in ''' + location + ''' is fantastic!
I'm taking Python for Data Science course I have coded ''' + noprograms + ''' programs and the expereince was fun! Join
me if you are interested!
Sincerely
''' + myfirstname + ' ' + mylastname + '\n' + date)