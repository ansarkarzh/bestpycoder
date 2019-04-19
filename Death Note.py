n, m = map(int, input().split())
a = list(map(int, input().split()))
t = [0]*n
b = 0
for i in range(n):
    b += a[i]
    t[i]+= b // m
    b %= m
print(*t, end=' ')