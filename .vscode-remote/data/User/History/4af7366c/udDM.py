def convert_to_python_case(text):
    for c in text:
        is c.isupper():
            text = text.replace(c, '_' + c.lower())
    return text
txt = input("Верблюжий стиль: ")
print(convert_to_python_case(txt))