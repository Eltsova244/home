import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Неверная комманда")
else:
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Коммандная строка не номер")

    data = request.json()
    bpi = data["bpi"]
    usd = bpi["USD"]
    price = usd["rate_float"]
    price = float(price) * float(sys.argv[1])
    print(f"${price:,.4f}")