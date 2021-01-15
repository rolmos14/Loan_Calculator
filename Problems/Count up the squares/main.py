total_sum = 0
sum_squares = 0

while True:
    num = int(input())
    total_sum += num
    sum_squares += num ** 2
    if total_sum == 0:
        break

print(sum_squares)
