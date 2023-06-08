directory = {
    "кофе": 20.00,
    "чай": 10.00,
    "булочка": 5.00,
    "салат": 30.40,
    "пирожное": 45.50,
}
sum = 0
while True:
    try:
        item = input("Блюдо: ")
        for key, value in directory.items():
            if key == item:
                sum += value
    except EOFError:
                print()
                break
print(f"Сумма: {sum:.2f}")