s = input()
names = set()

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        names.add(s[i:j])

for name in sorted(names):
    print(name)
