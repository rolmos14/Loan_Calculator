sentence = input()

vowels = "aeiou"

for letter in sentence:
    if letter.isalpha():
        if letter in vowels:
            print("vowel")
        else:
            print("consonant")
    else:
        break
