max_cafe = ""
max_cats = 0

while True:
    cafe_cats = input()
    if cafe_cats == "MEOW":
        break
    else:
        cafe, cats = cafe_cats.split()
        if int(cats) > max_cats:
            max_cafe = cafe
            max_cats = int(cats)

print(max_cafe)
