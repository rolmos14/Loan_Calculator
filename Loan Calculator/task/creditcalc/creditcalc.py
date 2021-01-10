import math
import argparse
import sys


def monthly_interest(annual_interest):
    # Calculate monthly interest rate
    return annual_interest / 100 / 12


def overpayment(p, **kwargs):
    if kwargs.get("acc"):
        return int(kwargs["acc"] - p)
    else:
        return int(kwargs["n"] * kwargs["A"] - p)


# Create parser object and arguments
parser = argparse.ArgumentParser(description="This program computes annuity and differentiated payments.")
parser.add_argument("--type", choices=["annuity", "diff"], help="Type of payment to be calculated. \
                                                                This parameter is always REQUIRED.")
parser.add_argument("--payment", help="Monthly payment amount. Not compatible with --type=diff.")
parser.add_argument("--principal", help="Loan principal amount.")
parser.add_argument("--periods", help="Number of months needed to repay the loan.")
parser.add_argument("--interest", help="Loan annual interest. This parameter is always REQUIRED.")

# Get arguments and check for: missing, incompatibilities, number of parameters or negative values
args = parser.parse_args()
if args.type is None or args.interest is None or \
        (args.type == "diff" and args.payment is not None) or \
        len(sys.argv) < 5:
    print("Incorrect parameters")
    exit()
for arg in args.__dict__.values():
    if arg != "annuity" and arg != "diff" and arg is not None:
        if float(arg) < 0:
            print("Incorrect parameters")
            exit()

# Declare loan variables if corresponding parameter is present
if args.principal is not None:
    P = float(args.principal)
if args.periods is not None:
    n = int(args.periods)
i = monthly_interest(float(args.interest))  # interest is always required
if args.payment is not None:
    A = int(args.payment)

# Calculate differentiated payments
if args.type == "diff":

    # Calculate months 1st to nth
    accumulated_payments = 0
    P_n = P / n
    for m in range(1, n + 1):
        D = math.ceil(P_n + i * (P - (P * (m - 1) / n)))
        print(f"Month {m}: payment is {D}")
        accumulated_payments += D

    # Calculate overpayment
    print(f"\nOverpayment = {overpayment(P, acc=accumulated_payments)}")

# Calculate annuity payment
else:  # args.type == "annuity"
    if args.principal is not None:
        if args.periods is not None:

            # Calculate annuity payment
            A = math.ceil(P * i * (1 + i) ** n / ((1 + i) ** n - 1))
            print(f"Your annuity payment = {A}!")

            # Calculate overpayment
            print(f"\nOverpayment = {overpayment(P, n=n, A=A)}")

        else:  # args.payment is not None

            # Calculate number of months
            n = math.ceil(math.log(A / (A - i * P), 1 + i))

            # Convert to years and months
            years = n // 12
            months = n % 12
            year_str = "year" if years < 2 else "years"
            month_str = "months" if months > 1 else "month"
            print("It will take",
                  f" {years} {year_str} " if years != 0 else "",
                  "and" if years != 0 and months != 0 else "",
                  f" {months} {month_str} " if months != 0 else "",
                  "to repay this loan!",
                  sep="")

            # Calculate overpayment
            print(f"\nOverpayment = {overpayment(P, n=n, A=A)}")

    else:  # args.payment is not None

        # Calculate loan principal
        P = A / (i * (1 + i) ** n / ((1 + i) ** n - 1))
        print(f"Your loan principal {round(P)}!")

        # Calculate overpayment
        print(f"\nOverpayment = {overpayment(P, n=n, A=A)}")
