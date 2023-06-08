def main():
    v = feet2meter(input("Сколько футов:"))
    print(f""Это будет {v:.2f} метров.")
def feet2meter(v):
    return (float(v.strip('ft')))*0.3048
main()