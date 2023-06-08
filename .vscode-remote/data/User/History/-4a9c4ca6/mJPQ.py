import sys

def count_lines(filename):
    if not filename.endswith(".py"):
        print("Ошибка: файл должен иметь расширение .py")
        sys.exit(1)
    try:
        with open(filename, "r") as f:
            count = 0
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                count += 1
            return count
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Ошибка: программа ожидает один аргумент командной строки - имя файла .py")
        sys.exit(1)
    filename = sys.argv[1]
    count = count_lines(filename)
    print(f"{count}")

if __name__ == "__main__":
    main()