dictionary = {
    "Apple" : 130,
    "Lime" : 20,
    "Avacado" : 50,
    "Banana" : 110,
    "Cantaloupe" : 50,
    "Grapefruit" : 60,
    "Grapes" : 90,
    "Honeydew Melon" : 50,
    "Kivifruit" : 90,
    "Lemon" : 15,
    "Nectarine" : 60,
    "Orange" : 80,
    "Peach" : 60,
    "Pear" : 100,
    "Pineapple" : 50,
    "Plums" : 70,
    "Strawberries" : 50,
    "Sweet Cherries" : 100,
    "Tangerine" : 50,
    "Watermelon" : 80

}
x=input("Фрукт: ")
for fruit, calories in dictionary.items():
    if fruit == x:
        print(f"Калории:{calories}")