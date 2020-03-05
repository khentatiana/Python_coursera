dollar = int(input())
penny = int(input())
quantity = int(input())
if 0 <= dollar < 10000 and 0 <= penny < 10000 and 0 <= quantity < 10000:
    price = (dollar * 100 + penny) * quantity
    print(price // 100, price % 100)
