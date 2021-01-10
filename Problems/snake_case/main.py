phrase = input()

print(phrase[0].lower() + ''.join(f"_{letter.lower()}" if letter.isupper() else letter for letter in phrase[1:]))
