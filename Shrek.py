n = int(input())
b = list(map(int, input().split()))
b.sort()
first = 0
second = 0
half = n//2
for i in range(half):
    first += b[i]
    second += b[i+half]
print(second-first)