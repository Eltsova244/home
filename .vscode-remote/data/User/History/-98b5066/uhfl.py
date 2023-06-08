months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]


def is_valid_date(date_str):
    try:
        if "." in date_str:
            day, month, year = map(int, date_str.split("."))
        else:
            parts = date_str.split()
            day, month, year = int(parts[0]),months.index(parts[1]) + 1, int(parts[2])
        if month < 1 or month > 12 or day < 1 or day > 31 or year < 1:
            return False
        return True
    except:
        return False


def convert_to_iso(date_str):
    if "." in date_str:
     day, month, year = map(int, date_str.split("."))
    else:
     parts = date_str.split()
     day, month, year = int(parts[0]),months.index(parts[1]) + 1, int(parts[2])
    return f"{year:04d}-{month:02d}-{day:02d}"


while True:
   date_str = input("Дата: ")
   if is_valid_date(date_str):
      iso_date = convert_to_iso(date_str)
      print(iso_date)
      break
