import sys

def count_lines(filename):
    if not filename.endswith(".py"):
        print("Ошибка: файл должен иметь расширение .py")
        sys.exit(1)

    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        sys.exit(1)

    count = 0
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            count += 1

    return count

if name == "main":
    if len(sys.argv) != 2:
        print("Ошибка: нужно указать имя файла")
        sys.exit(1)

    filename = sys.argv[1]
    count = count_lines(filename)
    print(f"{count}")