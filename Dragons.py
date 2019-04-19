def sortFirst(val):
    return val[0]
counter = 0
a = []
s, n = map(int, input().split())
for i in range(n):
    x, y = map(int, input().split())
    a.append([x,y])
a.sort(key= sortFirst)
for i in range(n):
    if s > a[i][0]:
        s += a[i][1]
        counter += 1
    else:
        break
if counter == n:
    print('YES')
else:
    print('NO')
