n = int(input())
b = list(map(int, input().split()))
b.sort()
half = n//2
first = sum(b[:half])
second = sum(b[half:])
print(second-first)
