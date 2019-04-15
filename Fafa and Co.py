n = int(input())
counter = 0
for i in range(1, n):
    if (n-i) % i == 0:
        counter += 1
print(counter)