n, s = map(int, input().split())
a = list(map(int, input().split()))
counter = 0
a.sort()
for i in range(len(a)):
    if a[i] <= s:
        s -= a[i]
    else:
        print(int(i))
        break