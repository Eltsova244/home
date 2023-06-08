amount_due = 50
while amount_due > 0:
    print (f"Нужная сумма: {amount_due}")
    coin = int (input("Вставьте монету: "))
    amount_due -= coin

