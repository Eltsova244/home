months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентяорь", "октябрь", "ноябрь", "декабрь"]
While True:
    date = input("Date: ")
    try:
        month, day, year = date_str.split("/"))
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
           break
        expect:
             try:
            old_month, old_day, year = date.split(" ")
            for i in range(len(months)):
                if old_month == monts[i]:
                    month = i + 1
            day = old_day.replace(",","")
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
    except:
       print()
       pass
print(f"{year}-{month})

       return True
    except:
        return False

def convert_to_iso (date_str):
    if "." in date str:
        day, month, year = map(int, date_str.split("."))
    else:
        parts = date_str.split()
        day, month, year = int(parts [e]), months. index(parts [1]) + 1, int (parts [2])
    return f"{year:04d}-{month:02d}-{day: 02d}"

while True:
    date str = input("Дата: ")
    if is_valid_date (date_str):
        iso_date = convert_to_iso(date_str)
        print(iso_date)
        break
    else:
       print("Неправильный формат даты. Попробуйте еще раз.")