import math


def get_loan_principal():
    return float(input("Enter the loan principal:\n"))


def get_monthly_payment():
    return float(input("Enter the monthly payment:\n"))


def get_num_payments():
    return int(input("Enter the number of periods:\n"))


def get_monthly_interest():
    annual_interest = float(input("Enter the loan interest:\n"))
    # Calculate monthly interest rate
    return annual_interest / 100 / 12


what_to_calc = input('What do you want to calculate?\n' +
                     'type "n" - for number of monthly payments,\n' +
                     'type "a" - for annuity monthly payment amount,\n' +
                     'type "p" - for loan principal:\n')

if what_to_calc == "n":
    P = get_loan_principal()
    A = get_monthly_payment()
    i = get_monthly_interest()

    # Calculate number of months
    n = math.ceil(math.log(A / (A - i * P), 1 + i))

    # Convert to years and months
    years = n // 12
    months = n % 12
    year_str = "year" if years < 2 else "years"
    month_str = "months" if months > 1 else "month"
    print("It will take ",
          f"{years} {year_str} and " if years != 0 else "",
          f"{months} {month_str} " if months != 0 else "",
          "to repay this loan!",
          sep="")

elif what_to_calc == "a":
    P = get_loan_principal()
    n = get_num_payments()
    i = get_monthly_interest()

    # Calculate monthly payment
    A = math.ceil(P * i * (1 + i) ** n / ((1 + i) ** n - 1))
    last_payment = P - (n - 1) * A
    print(f"Your monthly payment = {A}",
          " and the last payment = " + str(last_payment) if last_payment != A and last_payment > 0 else "",
          "!",
          sep="")

else:  # what_to_calc == "p"
    A = get_monthly_payment()
    n = get_num_payments()
    i = get_monthly_interest()

    # Calculate loan principal
    P = A / (i * (1 + i) ** n / ((1 + i) ** n - 1))
    print(f"Your loan principal {round(P)}!")
