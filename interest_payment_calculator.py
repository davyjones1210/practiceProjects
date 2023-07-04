#collect the necessary inputs: principal (loan amount), apr, years
#Calculate monthly payment
#Show to the user

def main():
    print("*This is the monthly loan payment calculator*")
    print("")

    principal = float(input("Enter the loan amount: "))
    apr = float(input("Enter the annual interest rate: "))
    years = int(input("Enter the amount of years: "))

    monthly_interest_rate = apr/1200
    amt_of_months = years*12
    monthly_payment = principal*monthly_interest_rate/(1-(1+monthly_interest_rate)**(-amt_of_months))

    print("The monthly payment for this loan is: $%.2f" %monthly_payment)

main()
