n = int(input())
if n <= 999:
    print((n // 100 % 10) + (n // 10 % 10) + (n % 10))
