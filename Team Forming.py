n = int(input())
counter = 0
a = list(map(int, input().split()))
a.sort()
for i in range(0, n, 2):
    counter += a[i+1]-a[i]
print(counter)