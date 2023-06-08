import sys
from PIL import Image,ImageOps

def apply_shirt(input_file, output_file):
 if not input_file.endswith((".jpg", ".jpeg", ".png")):
    print("Ошибка: входной файл должен иметь расширение .jpg, .jpeg или .png")
    sys.exit(1)
 if not output_file.endswith((".jpg", ".jpeg", ".png")):
    print("Ввод и вывод имеют разные расширения")
    sys.exit(1)
 if input_file.split(".")[-1] != output_file.split(".")[-1]:
    print("Ввод и вывод имеют разные расширения")
    sys.exit(1)

 try:
   shirt = Image.open("shirt.png")
   input_image = Image.open(input_file)
 except FileNotFoundError:
   print(f"Файл {input_file} не существует")
   sys.exit(1)

 size = shirt.size
 input_image = ImageOps.fit(input_image, size)

 input_image.paste(shirt, (0, 0), shirt)

 input_image.save(output_file)

 if__name__ == "__main__":
  if len(sys.argv) < 3:
    print("Слишком мало аргументов в командной строке")
  if len(sys.argv) > 4:
    print("Слишком много аргументов в командной строке")
  if len(sys.argv) != 3:
    print("Ошибка: нужно указать имена входного и выходного файлов")
    sys.exit(1)

 input_file = sys.argv[1]
 output_file = sys.argv[2]
 apply_shirt(input_file, output_file)