n, k = map(int, input().split())
a, b, c, d = map(int, input().split())
s = int(0)  # Расстояние

if k < 1:
    print('-1')
    exit()


def check():
    global n, k, a, b, c, d, s
    n -= k
    s += (a - c) ** 2 + (b - d) ** 2


while True:
    if n >= k:
        check()
    elif n < 1:
        print(s)
        break
