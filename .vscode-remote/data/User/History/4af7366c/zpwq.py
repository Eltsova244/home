x = input("Верблюжий стиль: ")
s2 = ""
for c in x:
    if c.islower():
        s2 += c

print(s2)