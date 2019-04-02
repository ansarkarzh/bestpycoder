n, m, k = map(int, input().split())
counter = 0
if n >= m:
    print(1)
elif m <= m-n+k:
    print('NO')
else:
    while m > 0:
        m = m - n
        if m <= 0:
            counter += 1
            break
        m += k
        counter += 1
    print(counter)
