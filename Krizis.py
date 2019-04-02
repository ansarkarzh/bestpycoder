n, s = map(int, input().split())
a = list(map(int, input().split()))
counter = 0
a.sort()
summa = 0
for i in range(len(a)):
    if a[i] + summa <= s:
        summa += a[i]
        counter += 1
    else:
        break
print(counter)
