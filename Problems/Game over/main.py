scores = input().split()

correct = 0
incorrect = 0
for score in scores:
    if score == "C":
        correct += 1
    else:
        incorrect += 1
        if incorrect == 3:
            print("Game over")
            break
else:
    print("You won")

print(correct)
