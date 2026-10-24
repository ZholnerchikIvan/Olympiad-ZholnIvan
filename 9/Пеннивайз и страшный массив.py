n = int(input())
if n < 1 or n > 100000:
    exit()

a = list(map(int, input().split()))
b = list()

for i in range(n):
    b.append(a[i] + a[n-i-1])

print(" ".join(map(str, b)))
