greeting = input("Greeting: ")
value_to_print = value(greeting)
print(f"${value_to_print}")

def value(greeting):
    greeting = greeting.lower().strip()