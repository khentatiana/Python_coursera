v = int(input())
t = int(input())

if (0 < t < 1000) & (-1000 < v < 0):
    dist = 109 - ((-1 * v * t) % 109)
    print(dist)

if t < 0 & (0 < v < 1000):
    dist = (v * t) % 109
    print(dist)
