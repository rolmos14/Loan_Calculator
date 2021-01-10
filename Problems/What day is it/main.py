hour_offset = int(input())

if -12 <= hour_offset <= -11:
    print("Monday")
elif -10 <= hour_offset <= 13:
    print("Tuesday")
else:
    print("Wednesday")
