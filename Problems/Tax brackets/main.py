tax_brackets = {132407: 28,
                42708: 25,
                15528: 15,
                0: 0
                }

income = int(input())

for bracket in tax_brackets:
    if income >= bracket:
        percent = tax_brackets[bracket]
        calculated_tax = income * percent / 100
        print(f"The tax for {income} is {percent}%. That is {round(calculated_tax)} dollars!")
        break
