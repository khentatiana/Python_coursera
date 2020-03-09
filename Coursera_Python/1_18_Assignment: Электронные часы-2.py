N = int(input())
n = N % (3600 * 24)
if n > 0:
    hours = n // 3600
    min = n % 3600 // 60
    sec = n % 60
    print(hours,':', min // 10, ':', sec // 10, sec % 10, sep='')
