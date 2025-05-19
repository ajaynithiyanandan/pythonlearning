#Write a program to generate Fibonacci series up to n terms.

# Fibonacci series is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

def generate_fibonacci():
    n=int(input("Enter the number of terms in the Fibonacci series: "))
    print("Fibonacci series:")
    for i in range(n):
        val = fibonacci(i)
        if val>n:
            break
        print(val, end=" ")

    
    
def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

generate_fibonacci()