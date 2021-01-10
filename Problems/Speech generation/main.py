digit_to_name = {0: 'zero',
                 1: 'one',
                 2: 'two',
                 3: 'three',
                 4: 'four',
                 5: 'five',
                 6: 'six',
                 7: 'seven',
                 8: 'eight',
                 9: 'nine',
                 }

phone_num = input()

for digit in phone_num:
    print(digit_to_name[int(digit)])
