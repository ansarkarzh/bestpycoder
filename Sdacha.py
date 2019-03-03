def hi(num, right, left = 0):
    while left <= right:
        p = (left + right)//2
        if a[p] == num:
            return 1
        elif num > a[p]:
            left = p + 1
        elif num < a[p]:
            right = p - 1
    else:
        return 0
n, k= map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
out = []
for i in b:
    opa = hi(i, len(a)-1)
    if opa==1:
        out.append("YES")
    else:
        out.append("NO")
print(*out, sep=' ')