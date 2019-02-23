import math
n=int(input())
primes=[]
for i in range(n):
    a=list(map(int, input().split()))
    for j in range(2, a[1]+1):
        for k in primes:
            if k>int(math.sqrt(j)+1):
                primes.append(j)
                break
            if (j%k==0):
                break
        else:
            primes.append(j)
    for sym in primes:
        if sym>=a[0]:
            print(sym)
    primes.clear()
