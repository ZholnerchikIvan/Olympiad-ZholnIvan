a = str(input())
b = str(input()).split()
c = int() # Количество
d = int()
t = str()

b.append(0)

for i in range(len(b) - 1):
    r = b[i]
    if b.count(r) > 1:
        b[i] = r * b.count(r)

        for j in range(len(b) - 1):
            if j != i:
                if j == r:
                    del b[j]

del b[len(b) - 1]
d = max(b, key=int)

c = len(b)
print(f'{d} {c}')
