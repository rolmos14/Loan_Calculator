animal_price = {("sheep", "sheep"): 6769,
                ("cow", "cows"): 3848,
                ("pig", "pigs"): 1296,
                ("goat", "goats"): 678,
                ("chicken", "chickens"): 23
                }

user_money = int(input())

num_animals = 0

for (animal, animals), price in animal_price.items():
    if user_money >= price:
        num_animals = user_money // price
        print(num_animals, animal if num_animals == 1 else animals, sep=" ")
        break

if num_animals == 0:
    print("None")
