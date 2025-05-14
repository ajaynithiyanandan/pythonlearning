
#Print Prime Numbers
def print_primenumbers(n):
    for i in range(2,n+1):
        prime = True
        for j in range(2,int(i ** 0.5) + 1):
            if i%j==0:
                prime=False
                break
        if prime:
            print(i)

def print_number_pertype(numtype,limit):
    print('Printing',numtype,'numbers from 1 to',limit)
    if numtype=="even":
        for i in range(2,limit+1,2):
            print(i)
    elif numtype=="odd":
        for i in range(1,limit+1,2):
            print(i)
######################################

# print_primenumbers(100)
print_number_pertype("even",100)
print_number_pertype("odd",100)