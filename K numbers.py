n = int(input())
counter = 0
for i in range(n):
    stroka = int(str(i)[::-1])
    if i + stroka == n:
        counter += 1
print(counter)