#Jesus ugarte
#University Of Central Florida
# This program Determines how many coins are neccesary to give exact change
def main():
    print("this app counts how many coins are needed given ammount in $")
    n = scan()
    func(n)

def scan():
    while True:
        #Try Except code block for exception handling
        try:
            #Try the two lines of codes if there is an exception, throw Value error exception
            N1 = float(input("Please enter Ammount in $$: "))
            #If code reaches here, there is no error
            break
        except ValueError:
            #If there is any expeption at any point, run this line of code
            print("Invalid Value entered.  Try again...")    
    return N1

def func(n):
    quarter = 0;
    dime = 0;
    nickel = 0;
    penny = 0

    while n>0:
        if (n >= 0.25):
            quarter = quarter + 1
            n = n - 0.25
        elif (n >= 0.10):
            dime = dime +1 
            n = n - 0.1
        elif (n >= 0.05):
            nickel = nickel + 1
            n = n - 0.05
        else:
            penny = penny + 1
            n = n - 0.01
        n = round(n, 2)

    print(f'we need Q:{quarter} D:{dime} N:{nickel} P:{penny}')

main()                                                                                                                                                                                               