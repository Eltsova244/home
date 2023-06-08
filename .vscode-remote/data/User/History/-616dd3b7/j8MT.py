greeting = input("Greeting: ")
value_to_print = value(greeting)
print(f"${value_to_print}")

def value(greeting):
    greeting = greeting.lower().strip()
    """if 'hello' in greeting:
        retern 0"""
    elif 'h' == greeting[0]:
        return 20