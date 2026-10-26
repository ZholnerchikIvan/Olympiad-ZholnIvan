n = int(input())
a = list(map(int, input().split()))

count = {}

for x in a:
    if x not in count:
        count[x] = 0
    count[x] += 1

numbers = list(count.keys())

numbers.sort(key=lambda x: (count[x], x))

answer = []

for x in numbers:
    for i in range(count[x]):
        answer.append(x)

print(*answer)
