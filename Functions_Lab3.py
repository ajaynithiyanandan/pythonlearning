######### Functions Code #######

def print_n_m(n,m):
    for i in range(n,m):
        print(i)


def increment(n):
    return n+1
def decrement(n):
    return n-1
# n=5, m=2
def addition(n,m):
    if n<=m:        
        for i in range(0,m):
            n=increment(n)
        return n
    elif n>m:
        for i in range(0,n):
            m=increment(m)
        return m
def subtraction(n,m):
    if n<=m:        
        for i in range(0,m):
            n=decrement(n)
        return n
    elif n>m:
        for i in range(0,n):
            m=decrement(m)
        return m
    

def multiplication(n, m):
    result = 0
    for i in range(n):
        for j in range(m):
            result = increment(result)
    return result



######### Functions Calls #########
firstnumber = int(input("Enter first number: "))
secondnumber = int(input("Enter second number: "))
# print("Add " + str(addition(firstnumber,secondnumber)))
# print("Subtract " + str(subtraction(firstnumber,secondnumber)))
print("Multiply " + str(multiplication(firstnumber,secondnumber)))