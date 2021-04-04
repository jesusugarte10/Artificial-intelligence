#jesus Ugarte
#University Of Central Florida
#This app calculates how much time will it take to pay off credit card balance

def scan():
    while True:
        #Try Except code block for exception handling
        try:
            #Try the two lines of codes if there is an exception, throw Value error exception
            N1 = float(input("Please enter Value: "))
            #If code reaches here, there is no error
            break
        except ValueError:
            #If there is any expeption at any point, run this line of code
            print("Invalid Value entered.  Try again...")    
    return N1

def minimum_Payment(balance, apr):

    expected_Minimum_Monthly_Payment = balance

    ##Getting readl summaiton of expected ammount to be paid
    for i in range(0, 12):
        expected_Minimum_Monthly_Payment += (expected_Minimum_Monthly_Payment * (apr/100)/12)

    expected_Minimum_Monthly_Payment/= 12 #Geat real month Average

    print("How Much would you pay a month?")
    monthly_Payment = scan()

    while(monthly_Payment < expected_Minimum_Monthly_Payment):
        print(f"You should pay more than {expected_Minimum_Monthly_Payment} a month")
        print("How Much would you pay a month?")
        monthly_Payment = scan()

    return monthly_Payment

def finalBalance(balance, payment):
    time = 1
    while(balance > 0):
        balance -= payment 
        time += 1

    print(f"It will take you around {time} Months to pay off your card")

def main():
    print("What is the current Credit Card Balance in $$?")
    balance = scan()

    print("What is the Credit Card APR in '%' ?")
    apr = scan()

    #Getting minimum payment
    payment = minimum_Payment(balance, apr)

    finalBalance(balance, payment)

main()