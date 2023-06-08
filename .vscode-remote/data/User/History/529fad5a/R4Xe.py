while True:
    try:
        fueltank = input("Дробь: ")
        z, y = fueltank.split('/')
        fuel = round((int(z) / int(y)) * 100)
        if fuel >= 99:
            print("F")
        elif fuel <= 1:
            print("E")
        else:
            print(str(fuel) + "%")
        break
    except(ValueError, ZeroDivisionError):
        continue