from math import sqrt
n = int(input())
primes = []
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(a[0], a[1]+1):
        if j!=1:
            for k in primes:
                if k > int(sqrt(j)+1):
                    primes.append(j)
                    break
                if (j % k == 0):
                    break
            else:
                primes.append(j)
    for sym in primes:
        print(sym)
    primes.clear()
