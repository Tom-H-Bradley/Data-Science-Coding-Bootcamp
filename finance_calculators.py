import math
#Giving the options for the user to enter firstly
#By using the lower function, this will flatten out any imperfections from the user's entry to make all entries standard
print("Investment - To calculate the amount of interest you'll earn on your investment")
print("Bond - To calculate the amount you'll have to pay on a home loan \n")

calculator = input("Enter either 'investment' or 'bond'. \n")
calculator = calculator.lower()

#Now to set out some conditional statements
#The wider conditional is based on whether or not the user entered investment or bond or maybe something else. The program accounts
#for a a mistype, and asks the user to rerun the program and check their spelling.

if calculator == "investment":
    #Using the float function allows us to convert the string output into a number which can be used by the program. We have used 
    #floats rather than integers because of the nature of the inputs (interest rates are not generally whole numbers).
    #Using strip on the interest variable negates any percentage sign the user may have inputted.
    #An f string is used at the end of this conditional to give a formatted response to the user.
    amount = float(input("Please enter the amount of money you will be depositing below. \n"))
    interest = input("Please enter your interest rate.\n")
    interest = float(interest.strip("%"))
    years = float(input("Please enter the amount of years you will be investing for.\n"))
    i_type = input("Is your investment running on simple or compound interest? \n")
    i_type = i_type.lower()
    if i_type == "simple":
        investment = amount*(1 + years*interest/100)
    elif i_type == "compound":
        investment = amount*math.pow(1 + interest/100, years)
    else:
        print("This interest type is not recognised. Please check your spelling and rerun the program")
    print(f"With {i_type} interest applied to your investment of {amount}, your money will be worth {investment} in {years} years")
elif calculator == "bond":
    #The bond calculation follows a similar formula but does not have a further conditional in it as all the entries by the user
    #will be numbers.
    #We are dividing the interest rate by 1200 to calcuate the equivalent decimal version of an interest percentage,
    #on a monthly basis
    value = float(input("Please enter the present value of the house\n"))
    interest = input("Please enter your interest rate.\n")
    interest = float(interest.strip("%"))
    months = float(input("How many months do you plan on taking to repay the bond?\n"))
    repayment = (interest*value/1200)/(1 - (1 + interest/1200)**(-months))
    print(f"The monthly repayments will be {repayment} on a {months} month repayment plan.")
else:
    print("This is not a valid option. Please check your spelling and rerun the program.")



