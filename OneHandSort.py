a = list(map(int, input().split()))
lena = len(a)
a.append(-1)
ans = []
for i in range(lena):
    if i == a[i]:
        continue
    else:
        ans.append(i)
        ans.append(a.index(i))
        ans.append(lena)
        a[a.index(i)] = a[i]
        a[i] = i
print(ans)