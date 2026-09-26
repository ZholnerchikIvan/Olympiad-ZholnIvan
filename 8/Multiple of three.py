a = str(input())

alist = list(a)
acheck = list(a)
intlist = list()

for i in range(len(alist)):
    s = alist[i]
    for j in range(10):
        if j != s:
            acheck[i] = str(j)
            if int("".join(acheck)) % 3 == 0:
                intlist.append(str("".join(acheck)))
        acheck = list(a)

intlist = list(map(int, intlist))

K = max(intlist)

print(K)