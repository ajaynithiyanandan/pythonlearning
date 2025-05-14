def print_hello_world():
    print('This prints Hello World!')
    print('''This is a multi-line String.
          I like Python!!
          ''')

def take_input_print():
    input_string = input('Enter a string')
    print('You entered: ' +  input_string)
    
def take_string_convert_int(stringval):
    try:
        intval = int(stringval)
        print('Converted to int: ' + str(intval))
    except ValueError:
        print('Cannot convert to int.')

##################################################################################

print_hello_world()
take_input_print()
take_string_convert_int('2334')
