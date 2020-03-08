n = int(input())
if 0 <= n < (10 ** 7):
    hours = n % (60 * 24) // 60
    min = n % 60
    print(hours, min)