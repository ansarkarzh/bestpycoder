n = int(input())
l = list(map(int, input().split()))
k = int(input())
lst = []
S = [0, 1, 2, 1, 2]
for i in range(5, k+1):
    lst.append(S[i - 1])
    for j in range(n):
        lst.append(S[i - l[j]])
    S.append(1 + min(lst))
    lst.clear()
if S[-1]<=k:
    print(S[-1])
else:
    print(-1)