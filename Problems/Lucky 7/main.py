# Read number of numbers and add them to a list
n = int(input())
numbers = [int(input()) for _ in range(n)]

for num in numbers:
    if num % 7 == 0:  # multiple of 7
        print(pow(num, 2))
