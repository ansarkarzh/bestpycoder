a, b, c = input().split()
commons = set()
for i in a:
    if i in b and i in c:
        commons.add(i)
for i in b:
    if i in a and i in c:
        commons.add(i)
for i in c:
    if i in a and i in b:
        commons.add(i)
print(len(commons))
print(*sorted(list(commons)), end = ' ')