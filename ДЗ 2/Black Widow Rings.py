t = int(input())
r = []
R = []
result = []
for i in range(t):
    n = int(input())
    for j in range(n):
        ra, Ra = map(int, input().split())
        r.append(ra)
        R.append(Ra)
    maxim = max(r)
    R[r.index(maxim)] = 0
    if max(R) < maxim:
        result.append(r.index(maxim)+1)
    else:
        result.append(-1)
for i in range(len(result)):
    print(result[i])
