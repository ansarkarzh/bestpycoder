n = int(input())
if n == 1:
    print(3)
else:
    a = 3
    for i in range(n-1):
        a *= 2
    print(a)