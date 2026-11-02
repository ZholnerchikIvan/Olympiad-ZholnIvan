n = int(input())
a = sorted(list(map(int, input().split())))

for i in range(n):
    if i + 1 != a[i]:
        if i == 0:
            print(0)
            break
        else:
            print(a[i - 1] + 1)
            break
