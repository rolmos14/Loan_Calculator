string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

num_of_vowels = 0

for char in string:
    if char in vowels:
        num_of_vowels += 1

print(num_of_vowels)
