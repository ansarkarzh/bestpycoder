n = int(input())
values = []
a = []
out = 0
for i in range(n):
    a.append(list(map(int, input().split())))
empty = input()
colours = list(map(int, input().split()))
for i in range(n):
    for j in range(i+1, n):
        if a[i][j] == 1 and colours[i] != colours [j]:
            out += 1
print(out)

