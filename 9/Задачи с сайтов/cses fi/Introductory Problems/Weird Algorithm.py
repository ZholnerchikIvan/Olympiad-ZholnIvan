n = int(input())

while n > 1:
    if n % 2 == 0:
        n //= 2
        print(n)
    else:
        n *= 3
        n += 1
        print(n)
