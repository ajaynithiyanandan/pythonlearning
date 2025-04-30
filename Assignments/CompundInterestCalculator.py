depositprincipal = float(input("Enter the deposit principal: "))
noyears = int(input('Enter the number of years: '))
interestrate = float(input('Enter the interest rate: '))
compoundinterest = depositprincipal * (1 + interestrate / 100) ** noyears
print("The compound interest is: ", compoundinterest)
print("The total amount after ", noyears, " years is: ", compoundinterest + depositprincipal)